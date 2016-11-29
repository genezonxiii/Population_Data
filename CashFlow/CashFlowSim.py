# -*-  coding: utf-8  -*-
__author__ = '10409003'
import math
import random
import numpy
import mysql.connector
import uuid
from setting import Config_2

class CashFlowSim():
    transData = []
    caseID=""
    def __init__(self):
        self.transData = []
        self.caseID = ""

    def calcAmount(self, typeTrans=0):
        tArr = []
        for trans in self.transData:
            #餘額
            if typeTrans == 0:
                tArr.append(trans[2])
            #收入
            elif typeTrans == 1:
                if trans[2] >= 0:
                    tArr.append(trans[2])
            #支出
            elif typeTrans == 2:
                if trans[2] < 0:
                    tArr.append(trans[2])
        pArr = numpy.array(tArr)
        return [pArr.sum(), pArr.mean(), pArr.std()]


    def loadData(self,strcaseID,blnDel='Y'):
        self.caseID = strcaseID
        config=Config_2()
        db = mysql.connector.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd, database=config.dbName)
        cursor = db.cursor()
        if (blnDel=='Y'):
            strSQL="Delete from tb_finsimu where user_id is Null and action='0' and case_id='" + self.caseID +"'"
            cursor.execute(strSQL)
            db.commit()
        strSQL="SELECT create_date,Amount FROM tb_fincase where case_id='" + self.caseID +"'"
        cursor.execute(strSQL)
        first_row=[]
        for row in cursor.fetchall():
            first_row=[row[0].isoformat(),'NULL',int(row[1]),1]
        strSQL="SELECT tb_finsimu.f_date,tb_account_code.code,tb_finsimu.amount,tb_finsimu.f_type,tb_finsimu.case_id FROM tb_finsimu INNER JOIN tb_account_code ON tb_finsimu.f_kind=tb_account_code.f_kind where case_id='" + self.caseID +"'"
        cursor.execute(strSQL)
        for row in cursor.fetchall():
            self.caseID=row[4]
            temp=[row[0].isoformat(),str(row[1]),int(row[2]),int(row[3])]
            self.transData.append(temp)
        db.commit()
        db.close()
        self.transData.insert(0,first_row)
        self.transData[0][2] += self.calcAmount()[0]
        self.transData = sorted(self.transData, key=lambda t: (t[0], t[3]))

    def getTransDate(self):
        result = []
        for trans in self.transData:
            result.append(trans[0])
        return result

    def simTrans(self, numTrans):
        _transDates = self.getTransDate()
        _sampleDates = numpy.random.choice(_transDates, numTrans, replace=False)

        for tdate in _sampleDates:
            typeTrans = numpy.random.choice(2, 1, p=[0.3, 0.7]) + 1
            (sumV, meanV, stdV) = self.calcAmount(typeTrans)

            val = [math.floor(meanV - stdV / 2), math.floor(meanV + stdV / 2)]
            rangeAmout = [min(val), max(val)]

            self.transData.append(
                [tdate, str(random.randint(1, 9)), random.randint(rangeAmout[0], rangeAmout[1]), 0])

        self.transData = sorted(self.transData, key=lambda t: (t[0], t[3]))

    def simTransByDegree(self , degreeTrans=10):
        self.simTrans(math.floor(len(self.transData) / degreeTrans))

    def removeSimTrans(self):
        tArr = []
        for trans in self.transData:
            if trans[3] != 0:
                tArr.append(trans)

        self.transData = sorted(tArr, key=lambda t: (t[0], t[3]))

    def output(self, simOnly=False):
        output=[]
        for trans in self.transData:
            if simOnly:
                if trans[3] == 0:
                    print('%s\t%s\t%8d\t%d' % (trans[0], trans[1], trans[2], trans[3]))
                    output.append(trans)
            else:
                print('%s\t%s\t%8d\t%d' % (trans[0], trans[1], trans[2], trans[3]))
                output.append(trans)
        self.DataToMysql(output)
        (sumV, meanV, stdV) = self.calcAmount()
        #print sumV
        return sumV

    def DataToMysql(self,output):
        config=Config_2()
        db = mysql.connector.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd, database=config.dbName, charset="utf8")
        cursor = db.cursor()
        for row in output:
            cursor.execute("INSERT INTO tb_finsimu (simulation_id,case_id,f_date,f_type,action,amount,f_kind)"
                       "VALUES(%s,%s,%s,%s,%s,%s,%s)", (str(uuid.uuid4()), str(self.caseID),str(row[0]),1,row[3],row[2],row[1]))
        db.commit()
        db.close()