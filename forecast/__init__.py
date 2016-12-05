# -*- coding: utf-8 -*-
#__author__ = '10408001'
from setting import Config_2
from pymongo import MongoClient
from datetime import date,datetime
import mysql.connector
import numpy as np
import json
import uuid
import pyqrcode
import png

#新品風向預測
class ProductForecast():
    conn,TotalSum = None,None
    def __init__(self):
        pass

    #開始計算並寫入 db 回傳成功／失敗
    def StartCalcu(self,strCaseid,strCondition):
        dbScore = self.getScore(strCaseid)
        dbWeight = self.getWeight(strCaseid)
        dbPoint = self.getPoint(strCaseid, dbScore, dbWeight,strCondition)
        result = self.Resultcalcu(dbPoint)
        self.updateSeq(strCaseid, result[0])
        return self.updateResult(strCaseid, result[1])

    #取得 db 連線
    def getConnection(self):
        try:
            if (self.conn == None):
                config = Config_2()
                return mysql.connector.connect(user=config.dbUser, password=config.dbPwd,
                                         host=config.dbServer, database=config.dbName)
            else:
                return self.conn
        except mysql.connector.Error :
            print "Connection DB Error"
            raise
        except Exception as e:
            print e.message
            raise

    #所有計算並要寫入 db 的結果
    def Resultcalcu(self,dbPoint):
        data = np.array(dbPoint)
        tmpData=[]
        tmpData.append(data.mean(axis = 1))
        resultsort = np.argsort(tmpData)
        resultData=[]
        resultData.append(resultsort)
        resultData.append(data.mean(axis = 0))
        self.TotalSum = data.mean(axis=0).sum()
        return resultData

    #取得權重
    def getWeight(self,strCaseid):
        strSQL="Select weight From tb_product_forecast_point where forecast_id='" + strCaseid + "'"
        tmpWeight = self.getData(strSQL)
        dbWeight=[]
        for row in tmpWeight:
            for i in range(len(row)):
                dbWeight.append(row[i])
        return dbWeight

    #取得成本(轉化為分數)
    def getScore(self,strCaseid):
        strSQL = "Select function_score,nfunction_score,service_score From tb_product_forecast where forecast_id='" + strCaseid + "'"
        dbScore, strScore = [], []
        tmpScore = self.getData(strSQL)
        for row in tmpScore:
            for rows in row:
                strPoint = str(rows).split(",")
                for i in range(len(strPoint)):
                    dbScore.append(float(strPoint[i]))

        return dbScore

    #取得評分並計算 權重 * 成本 (轉化為分數) * 評分
    def getPoint(self,strCaseid,dbScore,dbWeight,strCondition):
        intcondition=1
        if strCondition<>"":
            intcondition=self.getMongoData(strCondition)

        strSQL = "Select function_point,nfunction_point,service_point From tb_product_forecast_point where forecast_id='" + strCaseid + "'"
        dbPoint,strPoint = [],[]
        tmpPoint = self.getData(strSQL)
        i=0
        for row in tmpPoint:
            j = 0
            resultPoint = []
            for rows in row:
                strPoint = str(rows).split(",")
                for k in range(len(strPoint)):
                    resultPoint.append(intcondition*float(dbWeight[i])*dbScore[j]*float(strPoint[k]))
                    j+=1
            i += 1
            dbPoint.append(resultPoint)
        return dbPoint

    #從 db 取得 select 結果
    def getData(self,strSQL):
        try:
            self.conn = self.getConnection()
            cursor = self.conn.cursor()
            cursor.execute(strSQL)
            data_row = []
            for row in cursor.fetchall():
                data_row.append(row)
            cursor.close()
            return data_row
        except Exception as e :
            print e.message
            raise

    #取得 MongoDB 關鍵字的新聞筆數
    def getMongoData(self,strCondition):
        try:
            config = Config_2()
            client = MongoClient(config.mgHost, config.mgPort)
            db = client[config.mgDB]
            collect = db[config.mgCollection]
            intResult=collect.find({"content": {"$regex": strCondition}}).count()
            print intResult
            if intResult==0 :
                return 1
            else:
                return intResult
            # return collect.find({"content": {"$regex": strCondition}}).count()
        except Exception as e:
            print e.message
            raise

    #將最絡排序結果寫至 db
    def updateResult(self,strCaseid,result):
        data = json.loads(self.setJsonResult(strCaseid,result))
        strresult=""
        for each in data:
            strresult += each["Product"]["Item"] +'$'+ str(each["Product"]["Value"]) +'%,'

        strresult = strresult[:len(strresult)-1]
        sql=[]
        sql.append("Update tb_product_forecast set score_time=NOW(), result='" + strresult + "', isfinish=true Where forecast_id='" + strCaseid + "'")
        self.updataData(sql)
        return True

    #將評分結果與評分項目整合並排序
    def setJsonResult(self,strCaseid,result):
        self.conn = self.getConnection()
        cursor = self.conn.cursor()
        strSQL = "SELECT function_name, nfunction_name, service_name FROM  tb_product_forecast \
                  WHERE forecast_id ='" + strCaseid + "'"
        strtmp=""
        cursor.execute(strSQL)
        for row in cursor.fetchall():
            strtmp=row[0] + "," + row[1] + "," + row[2]

        cursor.close()
        strItem = strtmp.split(",")
        tmpjson=[]
        for i in range(len(strItem)):
            r = {"Product":{"Item": strItem[i] , "Value": + round(result[i]/self.TotalSum*100,2)}}
            tmpjson.append(r)

        lines = sorted(tmpjson, key=lambda k: k['Product']['Value'], reverse=True)
        return json.dumps(lines)

    #將評分後計算的總成績排序寫至 db
    def updateSeq(self,strCaseid,result):
        result=self.getSortResult(result)
        try:
            self.conn = self.getConnection()
            cursor = self.conn.cursor()
            strSQL="Select forecast_point_id from tb_product_forecast_point WHERE forecast_id='" + strCaseid + "'"
            cursor.execute(strSQL)
            sql=[]
            i=0
            for row in cursor.fetchall():
                sql.append("Update tb_product_forecast_point set score_seq=" + str(result[i]) +\
                           " where forecast_point_id='" + row[0] + "'")
                i += 1
            cursor.close()
            self.updataData(sql)
        except Exception as e :
            print e.message
            raise

    #將"成績排序"從 Numpy 陣列轉換為一般陣列
    def getSortResult(self,result):
        tmpResult=[]
        result=result.tolist()
        for row in result:
            for i in range(len(row)):
                tmpResult.append(row[i])

        return tmpResult

    #使用 sql string 新增／更新資料庫
    def updataData(self,strSQL):
        try:
            self.conn = self.getConnection()
            cursor = self.conn.cursor()
            for row in strSQL:
                cursor.execute(row)
            self.conn.commit()
            cursor.close()
        except Exception as e:
            print e.message()
            raise

#從 Mongodb 讀取新聞
class findNews():
    def __init__(self):
        pass

    def getNews(self):
        try:
            config = Config_2()
            client = MongoClient(config.mgHost, config.mgPort)
            db = client[config.mgDB]
            collect = db[config.mgCollection]
            source=['apple','bbc','chinatimes','ftv','hinet','ltn','sina','tvbs','udn','yahoo']
            ClientData=[]            
            #  for item in collect.find({"title":{ "$exists": "true", "$ne": [] },"source":{ "$exists": "true", "$ne": []}},{"content":0,"_id":0}).sort([('date', -1),('source', -1)]).limit(100):
            for i in range(len(source)):
                for item in collect.find({"title": {"$exists": "true", "$ne": []},"source": source[i]},{"content": 0, "_id": 0}).sort([('date', -1), ('source', -1)]).limit(10):
                    r = {"title": item["title"],"source": item["source"], "link":item["link"]}
                    ClientData.append(r)
            return ClientData

        except Exception as e:
            print e.message
            raise

#產品授權認證機制
class ProductLicense():
    conn,path = None,None
    def __init__(self):
        config = Config_2()
        self.path=config.path

    # 取得 db 連線
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

    #從 db 取得 select 結果
    def getData(self, strSQL):
        try:
            self.conn = self.getConnection()
            cursor = self.conn.cursor()
            cursor.execute(strSQL)
            data_row = []
            for row in cursor.fetchall():
                data_row.append(row)
            cursor.close()
            return data_row
        except Exception as e:
            print e.message
            raise

    #取得產品 Seed
    def getProductSeed(self,productid):
        strSQL = "Select seed From tb_product where product_id='" + productid + "'"
        data = self.getData(strSQL)
        product = None
        for row in data:
            product = str(row[0])
        return product

    #取得通路商 Seed
    def getChannelSeed(self,productid,agentid):
        strSQL = "Select CONCAT(region_code,'-',seed) seed From tb_agent_auth where product_id='"\
                 + productid + "' and agent_id='" + agentid +"'"
        data = self.getData(strSQL)
        channelSeed = None
        for row in data:
            channelSeed=str(row[0])
        return channelSeed

    #產生產品識別碼 fack
    def getProductLicense(self,productid):
        product=self.getProductSeed(productid)
        result=[]
        if product == None :
            r = {'License': None}
            result.append(r)
        else:
            strResult=str(uuid.uuid3(uuid.NAMESPACE_DNS, product)).upper()
            self.genQRcode(self.path,strResult)
            r={'License':strResult}
            result.append(r)
        return result

    #產生通路商授權碼 fack
    def getChannelAuth(self,productid,agentid):
        channelSeed = self.getChannelSeed(productid,agentid)
        result = []
        if channelSeed == None :
            r = {'auth': None}
            result.append(r)
        else:
            strResult = str(uuid.uuid5(uuid.NAMESPACE_DNS, productid+'-'+agentid +'-'+ channelSeed )).upper()
            self.genQRcode(self.path, strResult)
            r = {'auth': strResult}
            result.append(r)
        return result

    #產生服務識別碼
    def getServiceLicense(self,quantity):
        result=[]
        for i in range(quantity):
            strResult=str(uuid.uuid4()).upper()
            self.genQRcode(self.path, strResult)
            r={"ServiceID":strResult}
            result.append(r)
        return result

    #產生 QR Code
    def genQRcode(self,path,data):
        try:
            result = pyqrcode.create(data)
            result.png(path + str(data)+'.png',scale=8)
        except Exception as e:
            print e.message
            raise

#財務損益平衡
class CalcuFinance():
    conn = None
    def __init__(self):
        pass

    #取得 db 連線
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

    #從 db 取得 stored procedure 結果
    def getData(self, procedureName, parameter):
        try:
            self.conn = self.getConnection()
            cursor = self.conn.cursor()
            cursor.callproc(procedureName, parameter)
            data_row = []
            for row in cursor.stored_results():
                data_row = row.fetchall()
            cursor.close()
            return data_row
        except Exception as e:
            print e.message
            raise

    #取得損益平衡線
    def startCalcu(self,case_id):
        parameter,data,data1,data2=[],[],[],[]
        parameter.append(case_id)
        data=self.getData('sp_calcu_fincase_rate',parameter)
        data1=self.getData('sp_calcu_fincase_total',parameter)
        data2 = self.getFinDate(case_id)
        result=[]
        self.Combine_Data(result,data,'Income',True)
        self.Combine_Data(result, data, 'Income', False)
        self.Combine_Data(result,data,'Outcome',True)
        self.Combine_Data(result, data, 'Outcome', False)
        self.Combine_Total(result,data1)
        r = {'BalanceDate': data2}
        result.append(r)
        return result

    #取得浴盆曲線
    def getBathtubCurve(self,case_id):
        parameter = []
        parameter.append(case_id)
        data = self.getData('sp_get_bathtub_fincase', parameter)
        return self.calcuFailureRate(data)

    #計算浴盆曲線的失效率
    def calcuFailureRate(self,data):
        FirstAmount = 0
        tmpDate,FirstDate = None , None
        FailureRate = 0
        result  = []
        for row in data:
            tmpDate = row[1]
            r={}
            if row[2]<> 'F':
                # print tmpDate,FirstDate
                d = abs(tmpDate-FirstDate).days
                if d == 0 :
                    d=1
                if row[2] == 'O':
                    FailureRate = round(float(abs(row[0])/1000)/d/365,4)
                elif row[2] =='I':
                    FailureRate = round(float(row[0] * -1 / 1000) / d / 365, 4)
                r = {"FinanceDate": datetime.strftime(tmpDate,"%Y-%m-%d"), "FailureRate": FailureRate}
                result.append(r)

            FirstDate = tmpDate
        return result

    #收入/支出累計加總
    def Combine_Data(self,result,data,type,action):
        Amount,Percent = 0,0
        tempresult=[]
        r={}
        for row in data:
            if type=='Income' and action == True :
                if row[3] == 'I' and row[4] == True:
                    Amount += row[0]
                    Percent += row[1]
                    r = {'Amount': float(Amount),'Percent': round(Percent, 2), 'Date': row[2].strftime('%Y-%m-%d')}
                    tempresult.append(r)
            elif type=='Income' and action == False :
                if row[3] == 'I' and row[4] == False:
                    Amount += row[0]
                    Percent += row[1]
                    r = {'Amount': float(Amount), 'Percent': round(Percent, 2), 'Date': row[2].strftime('%Y-%m-%d')}
                    tempresult.append(r)
            elif type=='Outcome' and action == True:
                if row[3] == 'O' and row[4] == True:
                    Amount += row[0]
                    Percent += row[1]
                    r = {'Amount': float(Amount),'Percent': round(Percent, 2), 'Date': row[2].strftime('%Y-%m-%d')}
                    tempresult.append(r)
            else:
                if row[3] == 'O' and row[4] == False:
                    Amount += row[0]
                    Percent += row[1]
                    r = {'Amount': float(Amount), 'Percent': round(Percent, 2), 'Date': row[2].strftime('%Y-%m-%d')}
                    tempresult.append(r)

        if type == 'Income' and action == True:
            return result.append({'Income_True':tempresult})
        elif type == 'Income' and action == False:
            return result.append({'Income_False': tempresult})
        elif type == 'Outcome' and action == True:
            return result.append({'Outcome_True': tempresult})
        else:
            return result.append({'Outcome_False': tempresult})
            
    #總收入&總支出
    def Combine_Total(self,result,data):
        for row in data:
            if row[1] =='I':
                r={'Income_Total':[{'Total':float(row[0])}]}
                result.append(r)
            else:
                r = {'Outcome_Total': [{'Total': float(row[0])}]}
                result.append(r)

    #找出資金餘額低於安全餘額的日期
    def getFinDate(self,case_id):
        try:
            self.conn = self.getConnection()
            cursor = self.conn.cursor()
            args=[case_id,0]
            result = cursor.callproc('sp_get_findate',args)
            cursor.close()
            if result[1] == None :
                return 'None'
            else:
                return result[1]
        except Exception as e :
            print e.message
            raise


#目標客群
class Persona():
    conn = None
    def __init__(self):
        pass

    #取得 persona 查詢結果
    def getPersona(self,Sex,Age,X3,X4,X5,X6,X7,X8,X9):
        strSQL="SELECT * FROM tb_persona Where "
        strSex=Sex.split(',')
        for i in range(len(strSex)):
            strSQL += " Sex=" + strSex[i] + " or"
        strSQL = strSQL[0:len(strSQL)-2] + " AND"

        strAge=Age.split(',')
        for i in range(len(strAge)):
            strSQL += " Age=" + strAge[i] + " or"
        strSQL = strSQL[0:len(strSQL)-2]

        result=self.getData(strSQL)
        return self.calcuResult(X3,X4,X5,X6,X7,X8,X9,result)

    #計算結果
    def calcuResult(self,X3,X4,X5,X6,X7,X8,X9,result):
        FinalResult = []
        for row in result:
            Score = (abs(float(row[5])-X3)**2 + abs(float(row[6])-X4)**2 + abs(float(row[7])-X5)**2\
                    + abs(float(row[8])-X6)**2 + abs(float(row[9])-X7)**2 + abs(float(row[10])-X8)**2\
                    + (abs(float(row[11])-X9)**2))**(0.5)
            FinalResult.append((row[1], Score))
        #取最短距離
        MinResult = min(FinalResult, key=lambda tup: tup[1])
        #結果排序
        #FinalResult.sort(key=lambda tup: tup[1], reverse=False)
        result = []
        for row in FinalResult:
            if row[1] == MinResult[1]:
                r = {"PersonaCode": row[0], "Score": row[1]}
                result.append(r)
        return result

    # 取得 db 連線
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

    #從 db 取得 select 結果
    def getData(self, strSQL):
        try:
            self.conn = self.getConnection()
            cursor = self.conn.cursor()
            cursor.execute(strSQL)
            data_row = []
            for row in cursor.fetchall():
                data_row.append(row)
            cursor.close()
            return data_row
        except Exception as e:
            print e.message
            raise

#區位選擇
class RegionSelect():
    conn = None
    RegionWeight,CityWeight=[],[]
    def __init__(self):
        self.conn = None
        self.RegionWeight, self.CityWeight = [], []

    def startCalcuate(self,type,area,city,CHK1a,CHK1b,CHK2a,CHK2b,CHK3a,CHK3b,per1,per2,per3):
        self.__init__()
        self.getAreaWeight(type,area)
        self.getCityWeight(type,area,city)
        Result = []
        result = self.getResult(CHK1a,CHK1b,CHK2a,CHK2b,CHK3a,CHK3b,per1,per2,per3)
        Result = sorted(result, key=lambda k: k['Score'], reverse=True)
        return Result

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
            self.conn = self.getConnection()
            cursor = self.conn.cursor()
            cursor.execute(strSQL)
            data_row = []
            for row in cursor.fetchall():
                data_row.append(row)
            cursor.close()
            return data_row
        except Exception as e:
            print e.message
            raise

    #取得各國家各產業基礎權重
    def getAreaWeight(self,type,area):
        if area<>'中國':
            area='東南亞'
        strSQL="Select * From tb_region_weight where type='" + type + "' AND area='" + area +"'"
        result = self.getData(strSQL)
        for row in result:
            for i in range(3,len(row)):
                self.RegionWeight.append(row[i])

    #取得城市權重
    def getCityWeight(self,type,area,city):
        strTB=''
        if type =='零售業':
            strTB='tb_SCORE_RegionSelect_Retail'
        else:
            strTB='tb_SCORE_RegionSelect_Dining'
        strSQL = "Select * From " + strTB + " Where City='" + city + "'"
        result = self.getData(strSQL)
        for row in result:
            tmp=[]
            for i in range(3,len(row)):
                if i ==3:
                    cbd = row[i]
                    tmp.append((row[i]))
                else:
                    tmp.append(row[i])
            self.CityWeight.append(tmp)

    #計算結果
    def getResult(self,chk1a,chk1b,chk2a,chk2b,chk3a,chk3b,per1,per2,per3):
        value1,value2,value2=0,0,0
        result=[]
        for row in self.CityWeight:
            tmp=[]
            r={}
            if self.RegionWeight[0] * chk1a + self.RegionWeight[1] * chk1b < 1:
                value1 = row[1] * chk1a + row[2] * chk1b
            else:
                value1 = row[1] * self.RegionWeight[0] + row[2] * self.RegionWeight[1]
            tmp.append(value1 / 100 * per1)
            if self.RegionWeight[2] * chk2a + self.RegionWeight[3] * chk2b < 1:
                value2 = row[3] * chk2a + row[4] * chk2b
            else:
                value2 = row[3] * self.RegionWeight[2] + row[3] * self.RegionWeight[3]
            tmp.append(value2 / 100 * per2)
            if self.RegionWeight[4] * chk3a + self.RegionWeight[5] * chk3b < 1:
                value3 = row[5] * chk3a + row[6] * chk3b
            else:
                value3 = row[5] * self.RegionWeight[4] + row[5] * self.RegionWeight[4]
            tmp.append(value3 / 100 * per3)
            r={"City":(row[0]),"Score":np.array(tmp).mean()}
            result.append(r)
        return result


if __name__ == '__main__':
    Task=[False,False,False,True,False,False]

    if Task[0]:
        PF = ProductForecast()
        print PF.StartCalcu('e72162f0-70eb-11e6-897a-005056af760c','美金')

    if Task[1]:
        FN = findNews()
        print FN.getNews()

    if Task[2]:
        PL = ProductLicense()
        #產生產品驗證碼
        print PL.getProductLicense('51ca0db0-9be7-11e6-922d-005056af760c')
        #產生經銷商授權碼
        print PL.getChannelAuth('51ca0db0-9be7-11e6-922d-005056af760c','142adb0a-9be5-11e6-922d-005056af760c')
        #產生服務識別碼
        print PL.getServiceLicense(10)

    if Task[3]:
        CF = CalcuFinance()
        #損益平衡
        print CF.startCalcu('57057e3a-9629-4a79-b5e4-19c9361f1b1a')
        #浴盆曲線
        # print CF.getBathtubCurve('0db5ea17-2c92-11e6-b101-000c29c1d067')

    if Task[4]:
        PS = Persona()
        print PS.getPersona('1','1',3,2,2,3,2,3,3)

    if Task[5]:
        RS = RegionSelect()
        print RS.startCalcuate('餐飲業','新加坡','新加坡',1,1,1,1,1,1,33,33,34)