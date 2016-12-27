# -*- coding: utf-8 -*-
#__author__ = '10408001'
import numpy as np
import mysql.connector
from setting import Config_2
import random

class DecisionMain():
    FactorValue_F1,FactorValue_FV1=[],[]
    FactorValue_F2,FactorValue_FV2=[],[]
    FactorMatrix,SolutionMatrix,SolutionMatrix_AllFactor =[],[],[]
    conn ,case_name , user_name, weight = None ,None ,None ,None
    evaluate_point, evaluate_1_point, evaluate_seq = None ,None ,None

    def __init__(self):
        self.FactorValue_F1, self.FactorValue_FV1 = [], []
        self.FactorValue_F2, self.FactorValue_FV2 = [], []
        self.FactorMatrix, self.SolutionMatrix, self.SolutionMatrix_AllFactor = [], [], []
        self.onn, self.case_name, self.user_name, self.weight = None, None, None, None
        self.evaluate_point, self.evaluate_1_point, self.evaluate_seq = None, None, None

    def startCalcuate(self,case_id):
        self.__init__()
        self.getCaseName(case_id)
        self.getDesicionInfo(case_id)
        # 參與人決策效力陣列
        PowerOfRoleSet=self.calcWeight(self.weight)
        # 決策方案政策偏好陣列
        SolutionSet = self.getPreference(case_id)
        PreferenceOfSolutionSet = self.calcWeight(SolutionSet)
        # 參與人 首階 決策因子之重要性值資料矩陣
        self.getFactorValue_F1()
        # 首階決策因子權重
        self.FactorValue_FV1 = self.getLevelWeight(self.FactorValue_F1)
        # 參與人 1 各子決策因子
        self.getFactorValue_F2()
        #取得二階決策子因子權重
        self.getFactorValue_FV2(case_id)

        self.setFactorMatrix1(case_id)
        #print self.FactorMatrix
        self.setFactorMatrix2()
        #print self.FactorMatrix
        self.setFactorMatrix3()

        # 各參與人各決策因子下所有方案比序
        self.getSolutionMatrix()
        # 計算决策方案的幾何平均數
        SolutionMatrix_A = []
        self.calcSolutionMatrix(PowerOfRoleSet,SolutionMatrix_A)
        # 計算結果
        SolutionMatrix_A = np.array(SolutionMatrix_A) * PreferenceOfSolutionSet
        #回傳結果
        Result = self.getResult(case_id,SolutionMatrix_A)
        return Result
        # print SolutionMatrix_A
        # print np.max(SolutionMatrix_A)
        # print np.argmax(SolutionMatrix_A)

    # 取得 db 的連線
    def getConnection(self):
        try:
            if (self.conn == None):
                config = Config_2()
                return mysql.connector.connect(user=config.dbUser, password=config.dbPwd,
                                               host=config.dbServer, database=config.dbName)
            else:
                return self.conn
        except mysql.connector.Error:
            print "Connection DB Error"
            raise
        except Exception as e:
            print e.message
            raise

    # 從 db 取得 select 結果
    def getData(self, strSQL):
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            cursor.execute(strSQL)
            data_row = []
            for row in cursor.fetchall():
                data_row.append(row)
            cursor.close()
            return data_row
        except Exception as e:
            print e.message
            raise

    #將計算結果寫回資料庫
    def updateDB(self,case_id,SolutionMatrix_A):
        strResult=''
        for i in range(len(SolutionMatrix_A)):
            strResult += self.case_name[i] + ',' + str(round(SolutionMatrix_A[i],5)) + ';'

        strSql = "UPDATE tb_case SET result='" + strResult + "',isfinish=true  WHERE case_id ='" + case_id + "'"
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            cursor.execute(strSql)
            cursor.close()
            conn.commit()
            return True
        except Exception as e:
            print e.message
            raise e
            return False

    #取該次評估商圈名稱:
    def getCaseName(self,case_id):
        strSQL="SELECT bcircle_name FROM tb_bcircle INNER JOIN tb_case ON\
                tb_bcircle.city_id=tb_case.city_id WHERE tb_case.case_id='" \
                + case_id + "'"
        result=self.getData(strSQL)
        self.case_name=[]
        for row in result:
            self.case_name.append(row[0])

    #取得決策偏好
    def getPreference(self,case_id):
        strSQL = "SELECT Preference FROM tb_case WHERE case_id='" + case_id + "'"
        result = self.getData(strSQL)
        Solutionresult = ''
        Solution = []
        for row in result:
            Solutionresult = row[0]
        strSolution = Solutionresult.split(',')
        for row in strSolution:
            Solution.append(int(row))
        return Solution

    #取該次評估人員，權重及評分
    def getDesicionInfo(self,case_id):
        strSQL = "SELECT tb_evaluate.*,tb_user.user_name FROM tb_evaluate INNER JOIN tb_user \
                 ON tb_evaluate.user_id=tb_user.user_id WHERE tb_evaluate.case_id='" \
                 + case_id + "'"
        result = self.getData(strSQL)
        self.user_name,self.weight,self.evaluate_point,self.evaluate_1_point,self.evaluate_seq=[],[],[],[],[]
        for row in result:
            # print 'user_name='+ str(row[9]),'weight=' + str(row[4]),'evaluate_point=' +row[6], \
            #     'evaluate_1_point=' + row[7],'evaluate_seq=' + row[8]
            self.user_name.append(row[9])
            self.weight.append(row[4])
            self.evaluate_point.append(row[6])
            self.evaluate_1_point.append(row[7])
            self.evaluate_seq.append(row[8])

    # 計算參與人決策效力及政策方案偏好權重
    def calcWeight(self,Weight):
        mSum=0
        tmpWeight=[]
        for i in range(len(Weight)):
            mSum += Weight[i]

        for i in range(len(Weight)):
            tmpWeight.append(float(Weight[i])/mSum)

        return tmpWeight

    # 計算各階層決策因子權重
    def getLevelWeight(self,FactorValue):
        sumAll=np.array(FactorValue).sum()
        tmp=np.array(FactorValue).sum(axis=0)
        result=[]
        for row in tmp:
            result.append(float(row) / float(sumAll))
        return result

    #展開首階權重
    def setFactorMatrix1(self,case_id):
        strSQL = "SELECT evaluate_1_no FROM tb_case WHERE case_id ='" + case_id + "'"
        result = self.getData(strSQL)
        for row in result:
            strCount = str(row[0]).split(',')
        tmpresult = []
        for row in strCount:
            tmpresult.append(int(row))
        tmp=[]
        for i in range(len(tmpresult)):
            for j in range(int(tmpresult[i])):
                tmp.append(self.FactorValue_FV1[i])
        self.FactorMatrix.append(tmp)

    #展開次階權重
    def setFactorMatrix2(self):
        tmp=[]
        for i in range(len(self.FactorValue_FV2)):
            for row in self.FactorValue_FV2[i]:
                tmp.append(row)
        self.FactorMatrix.append(tmp)

    #決策因子各階層權重乘積
    def setFactorMatrix3(self):
        tmp=[]
        for i in xrange(len(self.FactorMatrix[0])):
            tmp.append(self.FactorMatrix[0][i]*self.FactorMatrix[1][i])
        self.FactorMatrix.append(tmp)

    #取得首階決策因子資料
    def getFactorValue_F1(self):
        for i in range(len(self.evaluate_point)):
            strevaluate_point= str(self.evaluate_point[i]).split(',')
            tmpevaluate_point=[]
            for row in strevaluate_point:
                tmpevaluate_point.append(int(row))
            self.FactorValue_F1.append(tmpevaluate_point)

    # 取得二階決策因子資料
    def getFactorValue_F2(self):
        for i in range(len(self.evaluate_1_point)):
            splitevaluate_1_point= str(self.evaluate_1_point[i]).split(';')
            # print self.evaluate_1_point[i]
            tmpevaluate_1_point = []
            for j in splitevaluate_1_point:
                # print j
                strevaluate_1_point = str(j).split(',')
                # tmpevaluate_1_point=[]
                for row in strevaluate_1_point:
                    if row <>'':
                        # print type(row),row
                        tmpevaluate_1_point.append(int(row))
            self.FactorValue_F2.append(tmpevaluate_1_point)

    # 第二階決策權重展開
    def getFactorValue_FV2(self,case_id):
        strSQL="SELECT evaluate_1_no FROM tb_case WHERE case_id ='" + case_id + "'"
        result=self.getData(strSQL)
        for row in result:
            strCount=str(row[0]).split(',')
        arr = np.array(self.FactorValue_F2)
        # self.FactorValue_FV2.append(self.getLevelWeight(arr[:, 4:7]))
        intStart,intEnd=0,0
        for row in strCount:
            intStart = intEnd
            intEnd += int(row)
            self.FactorValue_FV2.append(self.getLevelWeight(arr[:,intStart:intEnd]))

    #計算所有參與人各決策子因子下所有方案比序
    def getSolutionMatrix(self):
        # for row in self.case_name:
        #     print row
        tmpSolutionMatrix=[]
        for result in self.evaluate_seq:
            strResult= result.split(';')
            tmpresult=[]
            for Solutiondata in strResult:
                strSolutiondata = Solutiondata.split(',')
                tmp = []
                for i in range(len(strSolutiondata)):
                    #if row == strSolutiondata[i]:
                    if i > 0 :
                        tmp.append(int(strSolutiondata[i]))
                if tmp<>[]:
                    tmpresult.append(tmp)
            tmpSolutionMatrix.append(tmpresult)
        # tmp=[]
        # 求決策排序平均差
        data = np.array(tmpSolutionMatrix).mean(axis=0)
        for row in data:
            tmp =[]
            for i in range(len(row)):
                tmp.append(row[i])
            self.SolutionMatrix_AllFactor.append(tmp)

        # print self.SolutionMatrix_AllFactor
        # exit()

        #求決策排序平均差-old
        # for row in tmpSolutionMatrix:
        #     print row[0]
        #     # self.SolutionMatrix_AllFactor.append(row[0])
        #     data = np.array(row).sum(axis=0)
        #     #data = np.array(row).mean(axis=1)
        #     tmp=[]
        #     for tmpdata in data:
        #         tmp.append(tmpdata)
        #     self.SolutionMatrix_AllFactor.append(tmp)
        # print self.SolutionMatrix
        # exit()

    # 計算决策方案的幾何平均數
    def calcSolutionMatrix(self,PowerOfRoleSet,SolutionMatrix_A):
        for row in self.SolutionMatrix_AllFactor:
            SolutionMatrix_F, SolutionMatrix_S, SolutionMatrix_V = [], [], []
            for i in range(len(row)):
                # print row[i],self.FactorMatrix[2][i]
                SolutionMatrix_F.append(row[i] * self.FactorMatrix[2][i])
            SolutionMatrix_S = np.array(SolutionMatrix_F).sum()
            SolutionMatrix_V = SolutionMatrix_S * np.array(PowerOfRoleSet)
            tmpSolutionMatrix_A = np.array(SolutionMatrix_V).prod() ** (1 / float(len(PowerOfRoleSet)))
            SolutionMatrix_A.append(tmpSolutionMatrix_A)

    #回傳結果
    def getResult(self,case_id, SolutionMatrix_A):
        result = []
        if self.updateDB(case_id, SolutionMatrix_A) == True:
            tmpresult, tmp = [], []
            intfinal = np.argmax(SolutionMatrix_A)
            for i in range(len(SolutionMatrix_A)):
                r = {"bcircle": self.case_name[i], "score": SolutionMatrix_A[i]}
                tmpresult.append(r)
                if i == intfinal:
                    r = {"CalcuFinal": {"bcircle": self.case_name[i], "score": SolutionMatrix_A[i]}}
                    result.append(r)
            result.append({"ResultSort": tmpresult})
            return result
        else:
            r = {"bcircle": None, "score": None}
            return result.append(r)

class DecisionChannel():
    FactorValue_F1,FactorValue_FV1=[],[]
    FactorValue_F2,FactorValue_FV2=[],[]
    FactorMatrix,SolutionMatrix,SolutionMatrix_AllFactor =[],[],[]
    conn ,channel_name , user_name, weight = None ,None ,None ,None
    evaluate_point, evaluate_1_point, evaluate_seq = None ,None ,None

    def __init__(self):
        self.FactorValue_F1, self.FactorValue_FV1 = [], []
        self.FactorValue_F2, self.FactorValue_FV2 = [], []
        self.FactorMatrix, self.SolutionMatrix, self.SolutionMatrix_AllFactor = [], [], []
        self.onn, self.case_name, self.user_name, self.weight = None, None, None, None
        self.evaluate_point, self.evaluate_1_point, self.evaluate_seq = None, None, None

    def startCalcuate(self,channel_id):
        self.__init__()
        self.getChannelName(channel_id)
        self.getDesicionInfo(channel_id)
        # 參與人決策效力陣列
        PowerOfRoleSet=self.calcWeight(self.weight)
        # 決策方案政策偏好陣列
        # PreferenceOfSolutionSet = self.calcWeight([1, 2, 3])
        SolutionSet=[]
        for i in range(len(self.channel_name)):
            SolutionSet.append(random.randint(1,3))
        PreferenceOfSolutionSet = self.calcWeight(SolutionSet)
        # 參與人 首階 決策因子之重要性值資料矩陣
        self.getFactorValue_F1()
        # 首階決策因子權重
        self.FactorValue_FV1 = self.getLevelWeight(self.FactorValue_F1)
        # 參與人 1 各子決策因子
        self.getFactorValue_F2()
        #取得二階決策子因子權重
        self.getFactorValue_FV2(channel_id)

        self.setFactorMatrix1(channel_id)
        #print self.FactorMatrix
        self.setFactorMatrix2()
        #print self.FactorMatrix
        self.setFactorMatrix3()

        # 各參與人各決策因子下所有方案比序
        self.getSolutionMatrix()
        # 計算决策方案的幾何平均數
        SolutionMatrix_A = []
        self.calcSolutionMatrix(PowerOfRoleSet,SolutionMatrix_A)
        # 計算結果
        SolutionMatrix_A = np.array(SolutionMatrix_A) * PreferenceOfSolutionSet
        #回傳結果
        return self.getResult(channel_id,SolutionMatrix_A)

    # 取得 db 的連線
    def getConnection(self):
        try:
            if (self.conn == None):
                config = Config_2()
                return mysql.connector.connect(user=config.dbUser, password=config.dbPwd,
                                               host=config.dbServer, database=config.dbName)
            else:
                return self.conn
        except mysql.connector.Error:
            print "Connection DB Error"
            raise
        except Exception as e:
            print e.message
            raise

    # 從 db 取得 select 結果
    def getData(self, strSQL):
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            cursor.execute(strSQL)
            data_row = []
            for row in cursor.fetchall():
                data_row.append(row)
            cursor.close()
            return data_row
        except Exception as e:
            print e.message
            raise

    #將計算結果寫回資料庫
    def updateDB(self,channel_id,SolutionMatrix_A):
        strResult=''
        for i in range(len(SolutionMatrix_A)):
            strResult += self.channel_name[i] + ',' + str(round(SolutionMatrix_A[i],5)) + ';'

        strSql = "UPDATE tb_case_channel SET result='" + strResult + "',isfinish=true  WHERE channel_id ='" + channel_id + "'"
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            cursor.execute(strSql)
            cursor.close()
            conn.commit()
            return True
        except Exception as e:
            print e.message
            raise e
            return False

    #取該次評估通路名稱:
    def getChannelName(self,channel_id):
        strSQL="SELECT channel_name from tb_case_channel where channel_id='" + channel_id + "'"
        result=self.getData(strSQL)
        self.channel_name=[]
        strResult=''
        for row in result:
            strResult=row[0]
        parserResult=strResult.split(',')
        for row in parserResult:
            self.channel_name.append(row)

    #取該次評估人員，權重及評分
    def getDesicionInfo(self,channel_id):
        strSQL = "SELECT tb_evaluate_channel.*,tb_user.user_name FROM tb_evaluate_channel\
         INNER JOIN tb_user ON tb_evaluate_channel.user_id=tb_user.user_id WHERE \
         tb_evaluate_channel.channel_id='" + channel_id + "'"
        result = self.getData(strSQL)
        self.user_name,self.weight,self.evaluate_point,self.evaluate_1_point,self.evaluate_seq=[],[],[],[],[]
        for row in result:
            # print 'user_name='+ str(row[9]),'weight=' + str(row[4]),'evaluate_point=' +row[6], \
            #     'evaluate_1_point=' + row[7],'evaluate_seq=' + row[8]
            self.user_name.append(row[9])
            self.weight.append(row[4])
            self.evaluate_point.append(row[6])
            self.evaluate_1_point.append(row[7])
            self.evaluate_seq.append(row[8])

    # 計算參與人決策效力及政策方案偏好權重
    def calcWeight(self,Weight):
        mSum=0
        tmpWeight=[]
        for i in range(len(Weight)):
            mSum += Weight[i]

        for i in range(len(Weight)):
            tmpWeight.append(float(Weight[i])/mSum)

        return tmpWeight

    # 計算各階層決策因子權重
    def getLevelWeight(self,FactorValue):
        sumAll=np.array(FactorValue).sum()
        tmp=np.array(FactorValue).sum(axis=0)
        result=[]
        for row in tmp:
            result.append(float(row) / float(sumAll))
        return result

    #展開首階權重
    def setFactorMatrix1(self,channel_id):
        strSQL = "SELECT evaluate_1_no FROM tb_case_channel WHERE channel_id ='" + channel_id + "'"
        result = self.getData(strSQL)
        for row in result:
            strCount = str(row[0]).split(',')
        tmpresult = []
        for row in strCount:
            tmpresult.append(int(row))
        tmp=[]
        for i in range(len(tmpresult)):
            for j in range(int(tmpresult[i])):
                tmp.append(self.FactorValue_FV1[i])
        self.FactorMatrix.append(tmp)

    #展開次階權重
    def setFactorMatrix2(self):
        tmp=[]
        for i in range(len(self.FactorValue_FV2)):
            for row in self.FactorValue_FV2[i]:
                tmp.append(row)
        self.FactorMatrix.append(tmp)

    #決策因子各階層權重乘積
    def setFactorMatrix3(self):
        tmp=[]
        for i in xrange(len(self.FactorMatrix[0])):
            tmp.append(self.FactorMatrix[0][i]*self.FactorMatrix[1][i])
        self.FactorMatrix.append(tmp)

    #取得首階決策因子資料
    def getFactorValue_F1(self):
        for i in range(len(self.evaluate_point)):
            strevaluate_point= str(self.evaluate_point[i]).split(',')
            tmpevaluate_point=[]
            for row in strevaluate_point:
                tmpevaluate_point.append(int(row))
            self.FactorValue_F1.append(tmpevaluate_point)

    # 取得二階決策因子資料
    def getFactorValue_F2(self):
        for i in range(len(self.evaluate_1_point)):
            splitevaluate_1_point= str(self.evaluate_1_point[i]).split(';')
            # print self.evaluate_1_point[i]
            tmpevaluate_1_point = []
            for j in splitevaluate_1_point:
                # print j
                strevaluate_1_point = str(j).split(',')
                # tmpevaluate_1_point=[]
                for row in strevaluate_1_point:
                    if row <>'':
                        # print type(row),row
                        tmpevaluate_1_point.append(int(row))
            self.FactorValue_F2.append(tmpevaluate_1_point)

    # 第二階決策權重展開
    def getFactorValue_FV2(self,channel_id):
        strSQL="SELECT evaluate_1_no FROM tb_case_channel WHERE channel_id ='" + channel_id + "'"
        result=self.getData(strSQL)
        for row in result:
            strCount=str(row[0]).split(',')
        arr = np.array(self.FactorValue_F2)
        # self.FactorValue_FV2.append(self.getLevelWeight(arr[:, 4:7]))
        intStart,intEnd=0,0
        for row in strCount:
            intStart = intEnd
            intEnd += int(row)
            self.FactorValue_FV2.append(self.getLevelWeight(arr[:,intStart:intEnd]))

    #計算所有參與人各決策子因子下所有方案比序
    def getSolutionMatrix(self):
        # for row in self.case_name:
        #     print row
        tmpSolutionMatrix=[]
        for result in self.evaluate_seq:
            strResult= result.split(';')
            tmpresult=[]
            for Solutiondata in strResult:
                strSolutiondata = Solutiondata.split(',')
                tmp = []
                for i in range(len(strSolutiondata)):
                    if i > 0 :
                        tmp.append(int(strSolutiondata[i]))
                if tmp<>[]:
                    tmpresult.append(tmp)
            tmpSolutionMatrix.append(tmpresult)
        # 求決策排序平均差
        data = np.array(tmpSolutionMatrix).mean(axis=0)
        for row in data:
            tmp =[]
            for i in range(len(row)):
                tmp.append(row[i])
            self.SolutionMatrix_AllFactor.append(tmp)

    # 計算决策方案的幾何平均數
    def calcSolutionMatrix(self,PowerOfRoleSet,SolutionMatrix_A):
        for row in self.SolutionMatrix_AllFactor:
            SolutionMatrix_F, SolutionMatrix_S, SolutionMatrix_V = [], [], []
            for i in range(len(row)):
                # print row[i],self.FactorMatrix[2][i]
                SolutionMatrix_F.append(row[i] * self.FactorMatrix[2][i])
            SolutionMatrix_S = np.array(SolutionMatrix_F).sum()
            SolutionMatrix_V = SolutionMatrix_S * np.array(PowerOfRoleSet)
            tmpSolutionMatrix_A = np.array(SolutionMatrix_V).prod() ** (1 / float(len(PowerOfRoleSet)))
            SolutionMatrix_A.append(tmpSolutionMatrix_A)

    #回傳結果
    def getResult(self,channel_id, SolutionMatrix_A):
        result = []
        if self.updateDB(channel_id, SolutionMatrix_A) == True:
            tmpresult, tmp = [], []
            intfinal = np.argmax(SolutionMatrix_A)
            for i in range(len(SolutionMatrix_A)):
                r = {"Channel": self.channel_name[i], "Score": SolutionMatrix_A[i]}
                tmpresult.append(r)
                if i == intfinal:
                    r = {"CalcuFinal": {"Channel": self.channel_name[i], "Score": SolutionMatrix_A[i]}}
                    result.append(r)
            result.append({"ResultSort": tmpresult})
            return result
        else:
            r = {"Channel": None, "Score": None}
            return result.append(r)

class DecisionCompet():
    FactorValue_F1,FactorValue_FV1=[],[]
    FactorValue_F2,FactorValue_FV2=[],[]
    FactorMatrix,SolutionMatrix,SolutionMatrix_AllFactor =[],[],[]
    conn ,competition_name , user_name, weight = None ,None ,None ,None
    evaluate_point, evaluate_1_point, evaluate_seq = None ,None ,None

    def __init__(self):
        self.FactorValue_F1, self.FactorValue_FV1 = [], []
        self.FactorValue_F2, self.FactorValue_FV2 = [], []
        self.FactorMatrix, self.SolutionMatrix, self.SolutionMatrix_AllFactor = [], [], []
        self.onn, self.case_name, self.user_name, self.weight = None, None, None, None
        self.evaluate_point, self.evaluate_1_point, self.evaluate_seq = None, None, None

    def startCalcuate(self,competition_id):
        self.__init__()
        self.getChannelName(competition_id)
        self.getDesicionInfo(competition_id)
        # 參與人決策效力陣列
        PowerOfRoleSet=self.calcWeight(self.weight)
        # 決策方案政策偏好陣列
        SolutionSet=[]
        for i in range(len(self.competition_name)):
            SolutionSet.append(random.randint(1,3))
        PreferenceOfSolutionSet = self.calcWeight(SolutionSet)
        # 參與人 首階 決策因子之重要性值資料矩陣
        self.getFactorValue_F1()
        # 首階決策因子權重
        self.FactorValue_FV1 = self.getLevelWeight(self.FactorValue_F1)
        # 參與人 1 各子決策因子
        self.getFactorValue_F2()
        #取得二階決策子因子權重
        self.getFactorValue_FV2(competition_id)

        self.setFactorMatrix1(competition_id)
        #print self.FactorMatrix
        self.setFactorMatrix2()
        #print self.FactorMatrix
        self.setFactorMatrix3()

        # 各參與人各決策因子下所有方案比序
        self.getSolutionMatrix()
        # 計算决策方案的幾何平均數
        SolutionMatrix_A = []
        self.calcSolutionMatrix(PowerOfRoleSet,SolutionMatrix_A)
        # 計算結果
        SolutionMatrix_A = np.array(SolutionMatrix_A) * PreferenceOfSolutionSet
        #回傳結果
        return self.getResult(competition_id,SolutionMatrix_A)

    # 取得 db 的連線
    def getConnection(self):
        try:
            if (self.conn == None):
                config = Config_2()
                return mysql.connector.connect(user=config.dbUser, password=config.dbPwd,
                                               host=config.dbServer, database=config.dbName)
            else:
                return self.conn
        except mysql.connector.Error:
            print "Connection DB Error"
            raise
        except Exception as e:
            print e.message
            raise

    # 從 db 取得 select 結果
    def getData(self, strSQL):
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            cursor.execute(strSQL)
            data_row = []
            for row in cursor.fetchall():
                data_row.append(row)
            cursor.close()
            return data_row
        except Exception as e:
            print e.message
            raise

    #將計算結果寫回資料庫
    def updateDB(self,competition_id,SolutionMatrix_A):
        strResult=''
        for i in range(len(SolutionMatrix_A)):
            strResult += self.competition_name[i] + ',' + str(round(SolutionMatrix_A[i],5)) + ';'

        strSql = "UPDATE tb_case_competition SET result='" + strResult + "',isfinish=true  WHERE competition_id ='" + competition_id + "'"
        try:
            conn = self.getConnection()
            cursor = conn.cursor()
            cursor.execute(strSql)
            cursor.close()
            conn.commit()
            return True
        except Exception as e:
            print e.message
            raise e
            return False

    #取該次評估競爭者名稱:
    def getChannelName(self,competition_id):
        strSQL="SELECT competition_name from tb_case_competition where competition_id='" + competition_id + "'"
        result=self.getData(strSQL)
        self.competition_name=[]
        strResult=''
        for row in result:
            strResult=row[0]
        parserResult=strResult.split(',')
        for row in parserResult:
            self.competition_name.append(row)

    #取該次評估人員，權重及評分
    def getDesicionInfo(self,competition_id):
        strSQL = "SELECT tb_evaluate_competition.*,tb_user.user_name FROM tb_evaluate_competition \
         INNER JOIN tb_user ON tb_evaluate_competition.user_id=tb_user.user_id WHERE \
         tb_evaluate_competition.competition_id='" + competition_id + "'"
        result = self.getData(strSQL)
        self.user_name,self.weight,self.evaluate_point,self.evaluate_1_point,self.evaluate_seq=[],[],[],[],[]
        for row in result:
            self.user_name.append(row[9])
            self.weight.append(row[4])
            self.evaluate_point.append(row[6])
            self.evaluate_1_point.append(row[7])
            self.evaluate_seq.append(row[8])

    # 計算參與人決策效力及政策方案偏好權重
    def calcWeight(self,Weight):
        mSum=0
        tmpWeight=[]
        for i in range(len(Weight)):
            mSum += Weight[i]

        for i in range(len(Weight)):
            tmpWeight.append(float(Weight[i])/mSum)

        return tmpWeight

    # 計算各階層決策因子權重
    def getLevelWeight(self,FactorValue):
        sumAll=np.array(FactorValue).sum()
        tmp=np.array(FactorValue).sum(axis=0)
        result=[]
        for row in tmp:
            result.append(float(row) / float(sumAll))
        return result

    #展開首階權重
    def setFactorMatrix1(self,competition_id):
        strSQL = "SELECT evaluate_1_no FROM tb_case_competition WHERE competition_id ='" + competition_id + "'"
        result = self.getData(strSQL)
        for row in result:
            strCount = str(row[0]).split(',')
        tmpresult = []
        for row in strCount:
            tmpresult.append(int(row))
        tmp=[]
        for i in range(len(tmpresult)):
            for j in range(int(tmpresult[i])):
                tmp.append(self.FactorValue_FV1[i])
        self.FactorMatrix.append(tmp)

    #展開次階權重
    def setFactorMatrix2(self):
        tmp=[]
        for i in range(len(self.FactorValue_FV2)):
            for row in self.FactorValue_FV2[i]:
                tmp.append(row)
        self.FactorMatrix.append(tmp)

    #決策因子各階層權重乘積
    def setFactorMatrix3(self):
        tmp=[]
        for i in xrange(len(self.FactorMatrix[0])):
            tmp.append(self.FactorMatrix[0][i]*self.FactorMatrix[1][i])
        self.FactorMatrix.append(tmp)

    #取得首階決策因子資料
    def getFactorValue_F1(self):
        for i in range(len(self.evaluate_point)):
            strevaluate_point= str(self.evaluate_point[i]).split(',')
            tmpevaluate_point=[]
            for row in strevaluate_point:
                tmpevaluate_point.append(int(row))
            self.FactorValue_F1.append(tmpevaluate_point)

    # 取得二階決策因子資料
    def getFactorValue_F2(self):
        for i in range(len(self.evaluate_1_point)):
            splitevaluate_1_point= str(self.evaluate_1_point[i]).split(';')
            # print self.evaluate_1_point[i]
            tmpevaluate_1_point = []
            for j in splitevaluate_1_point:
                # print j
                strevaluate_1_point = str(j).split(',')
                # tmpevaluate_1_point=[]
                for row in strevaluate_1_point:
                    if row <>'':
                        # print type(row),row
                        tmpevaluate_1_point.append(int(row))
            self.FactorValue_F2.append(tmpevaluate_1_point)

    # 第二階決策權重展開
    def getFactorValue_FV2(self,competition_id):
        strSQL="SELECT evaluate_1_no FROM tb_case_competition WHERE competition_id ='" + competition_id + "'"
        result=self.getData(strSQL)
        for row in result:
            strCount=str(row[0]).split(',')
        arr = np.array(self.FactorValue_F2)
        intStart,intEnd=0,0
        for row in strCount:
            intStart = intEnd
            intEnd += int(row)
            self.FactorValue_FV2.append(self.getLevelWeight(arr[:,intStart:intEnd]))

    #計算所有參與人各決策子因子下所有方案比序
    def getSolutionMatrix(self):
        tmpSolutionMatrix=[]
        for result in self.evaluate_seq:
            strResult= result.split(';')
            tmpresult=[]
            for Solutiondata in strResult:
                strSolutiondata = Solutiondata.split(',')
                tmp = []
                for i in range(len(strSolutiondata)):
                    if i > 0 :
                        tmp.append(int(strSolutiondata[i]))
                if tmp<>[]:
                    tmpresult.append(tmp)
            tmpSolutionMatrix.append(tmpresult)
        # 求決策排序平均差
        data = np.array(tmpSolutionMatrix).mean(axis=0)
        for row in data:
            tmp =[]
            for i in range(len(row)):
                tmp.append(row[i])
            self.SolutionMatrix_AllFactor.append(tmp)

    # 計算决策方案的幾何平均數
    def calcSolutionMatrix(self,PowerOfRoleSet,SolutionMatrix_A):
        for row in self.SolutionMatrix_AllFactor:
            SolutionMatrix_F, SolutionMatrix_S, SolutionMatrix_V = [], [], []
            for i in range(len(row)):
                # print row[i],self.FactorMatrix[2][i]
                SolutionMatrix_F.append(row[i] * self.FactorMatrix[2][i])
            SolutionMatrix_S = np.array(SolutionMatrix_F).sum()
            SolutionMatrix_V = SolutionMatrix_S * np.array(PowerOfRoleSet)
            tmpSolutionMatrix_A = np.array(SolutionMatrix_V).prod() ** (1 / float(len(PowerOfRoleSet)))
            SolutionMatrix_A.append(tmpSolutionMatrix_A)

    #回傳結果
    def getResult(self,competition_id, SolutionMatrix_A):
        result = []
        if self.updateDB(competition_id, SolutionMatrix_A) == True:
            tmpresult, tmp = [], []
            intfinal = np.argmax(SolutionMatrix_A)
            for i in range(len(SolutionMatrix_A)):
                r = {"Competitor": self.competition_name[i], "Score": SolutionMatrix_A[i]}
                tmpresult.append(r)
                if i == intfinal:
                    r = {"CalcuFinal": {"Competitor": self.competition_name[i], "Score": SolutionMatrix_A[i]}}
                    result.append(r)
            result.append({"ResultSort": tmpresult})
            return result
        else:
            r = {"Competitor": None, "Score": None}
            return result.append(r)


if __name__=="__main__":
    work=[True,False,False]

    if work[0] == True :
        GD = DecisionMain()
        print GD.startCalcuate('09910e5c-4bc6-4253-b166-2401dc76ed65')
    elif work[1] == True :
        GD = DecisionChannel()
        print GD.startCalcuate('b79a6c79-4c07-4060-bbab-d41e6a9b5130')
    elif work[2] == True :
        GD = DecisionCompet()
        print GD.startCalcuate('ce7c2e37-98b0-49cb-bbf7-db51fc9be456')
