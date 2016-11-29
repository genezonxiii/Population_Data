# -*-  coding: utf-8  -*-
__author__ = '10409003'
import json,urllib
import mysql.connector
import numpy
from setting import Config_2

class Education_M:
    def ParserJson(self,url):
        result = json.load(urllib.urlopen(url))
        data =[]
        resultdata = []
        CountyId = result["Info"][0]
        for each in result['RowDataList']:
            self.CombindData(each, data, CountyId['InCountyId'])
        self.sumData(data, resultdata)
        self.writeDB(resultdata)
        # for result in data:
        #     print result
    def writeDB(self, data):
        try:
            config=Config_2()
            db = mysql.connector.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd, database=config.dbName)
            db.set_charset_collation('utf8')
            cursor = db.cursor()
            for i in data:
                args = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],
                        i[10])
                # print args
                cursor.callproc('p_edu_county_m', args)
            db.commit()
        except mysql.connector.Error as e:
            db.rollback()
            print(str(e))
        except Exception as e:
            db.rollback()
            print(str(e))
        finally:
            cursor.close()
            db.close()
    def CombindData(self,row,data,county):
        INFO_TIME=row['INFO_TIME'][0:3]
        _phd = int(row['M_A15A19_E1314_CNT']) + int(row['M_A20A24_E1314_CNT']) + \
               int(row['M_A25A29_E1314_CNT']) + int(row['M_A30A34_E1314_CNT'])+ \
               int(row['M_A35A39_E1314_CNT']) + int(row['M_A40A44_E1314_CNT'])+ \
               int(row['M_A45A49_E1314_CNT']) + int(row['M_A50A54_E1314_CNT'])+ \
               int(row['M_A55A59_E1314_CNT']) + int(row['M_A60A64_E1314_CNT'])+ \
               int(row['M_A65UP_E1314_CNT'])
        _master=int(row['M_A15A19_E1112_CNT'])+int(row['M_A20A24_E1112_CNT'])+\
                int(row['M_A25A29_E1112_CNT'])+int(row['M_A30A34_E1112_CNT'])+ \
                int(row['M_A35A39_E1112_CNT']) + int(row['M_A40A44_E1112_CNT'])+ \
                int(row['M_A45A49_E1112_CNT']) + int(row['M_A50A54_E1112_CNT'])+ \
                int(row['M_A55A59_E1112_CNT']) + int(row['M_A60A64_E1112_CNT'])+ \
                int(row['M_A65UP_E1112_CNT'])
        _university=int(row['M_A15A19_E2122_CNT'])+int(row['M_A20A24_E2122_CNT'])+\
                    int(row['M_A25A29_E2122_CNT'])+int(row['M_A30A34_E2122_CNT'])+ \
                    int(row['M_A35A39_E2122_CNT']) + int(row['M_A40A44_E2122_CNT'])+ \
                    int(row['M_A45A49_E2122_CNT']) + int(row['M_A50A54_E2122_CNT'])+ \
                    int(row['M_A55A59_E2122_CNT']) + int(row['M_A60A64_E2122_CNT'])+ \
                    int(row['M_A65UP_E2122_CNT'])
        _college=int(row['M_A15A19_E3_4_5_CNT'])+int(row['M_A20A24_E3_4_5_CNT'])+\
                 int(row['M_A25A29_E3_4_5_CNT'])+int(row['M_A30A34_E3_4_5_CNT'])+ \
                 int(row['M_A35A39_E3_4_5_CNT']) + int(row['M_A40A44_E3_4_5_CNT'])+ \
                 int(row['M_A45A49_E3_4_5_CNT']) + int(row['M_A50A54_E3_4_5_CNT'])+ \
                 int(row['M_A55A59_E3_4_5_CNT']) + int(row['M_A60A64_E3_4_5_CNT'])+ \
                 int(row['M_A65UP_E3_4_5_CNT'])
        _senior=int(row['M_A15A19_E6_7_CNT'])+int(row['M_A20A24_E6_7_CNT'])+\
                int(row['M_A25A29_E6_7_CNT'])+int(row['M_A30A34_E6_7_CNT'])+ \
                int(row['M_A35A39_E6_7_CNT']) + int(row['M_A40A44_E6_7_CNT'])+ \
                int(row['M_A45A49_E6_7_CNT']) + int(row['M_A50A54_E6_7_CNT'])+ \
                int(row['M_A55A59_E6_7_CNT']) + int(row['M_A60A64_E6_7_CNT'])+ \
                int(row['M_A65UP_E6_7_CNT'])
        _junior=int(row['M_A15A19_E8_9_CNT'])+int(row['M_A20A24_E8_9_CNT'])+\
                int(row['M_A25A29_E8_9_CNT'])+int(row['M_A30A34_E8_9_CNT'])+ \
                int(row['M_A35A39_E8_9_CNT']) + int(row['M_A40A44_E8_9_CNT'])+ \
                int(row['M_A45A49_E8_9_CNT']) + int(row['M_A50A54_E8_9_CNT'])+ \
                int(row['M_A55A59_E8_9_CNT']) + int(row['M_A60A64_E8_9_CNT'])+ \
                int(row['M_A65UP_E8_9_CNT'])
        _primary=int(row['M_A15A19_E1_2_CNT'])+int(row['M_A20A24_E1_2_CNT'])+\
                 int(row['M_A25A29_E1_2_CNT'])+int(row['M_A30A34_E1_2_CNT'])+ \
                 int(row['M_A35A39_E1_2_CNT']) + int(row['M_A40A44_E1_2_CNT'])+ \
                 int(row['M_A45A49_E1_2_CNT']) + int(row['M_A50A54_E1_2_CNT'])+ \
                 int(row['M_A55A59_E1_2_CNT']) + int(row['M_A60A64_E1_2_CNT'])+ \
                 int(row['M_A65UP_E1_2_CNT'])
        _self=int(row['M_A15A19_E03_CNT'])+int(row['M_A20A24_E03_CNT'])+\
              int(row['M_A25A29_E03_CNT'])+int(row['M_A30A34_E03_CNT'])+ \
              int(row['M_A35A39_E03_CNT']) + int(row['M_A40A44_E03_CNT'])+ \
              int(row['M_A45A49_E03_CNT']) + int(row['M_A50A54_E03_CNT'])+ \
              int(row['M_A55A59_E03_CNT']) + int(row['M_A60A64_E03_CNT'])+\
              int(row['M_A65UP_E03_CNT'])
        _no=int(row['M_A15A19_E04_CNT'])+int(row['M_A20A24_E04_CNT'])+\
            int(row['M_A25A29_E04_CNT'])+int(row['M_A30A34_E04_CNT'])+ \
            int(row['M_A35A39_E04_CNT']) + int(row['M_A40A44_E04_CNT'])+ \
            int(row['M_A45A49_E04_CNT']) + int(row['M_A50A54_E04_CNT'])+ \
            int(row['M_A55A59_E04_CNT']) + int(row['M_A60A64_E04_CNT'])+ \
            int(row['M_A65UP_E04_CNT'])

        data.append((county,_phd,_master,_university,_college,_senior,_junior,
                     _primary,_self,_no,INFO_TIME))

    def sumData(self, data, resultdata):
        strCountID = ''
        strInfo = ''
        arr = []
        mydata = []
        for row in data:
            arr = []
            # print row
            # mydata.append(data[1],data[2])
            for i in range(len(row)):
                strCountID = row[0]
                strInfo = row[10]
                if i > 0 and i < 10:
                    # print row[i]
                    arr.append(row[i])
            mydata.append(arr)

        mydata2 = numpy.array(mydata)
        result = mydata2.sum(axis=0)
        resultdata.append((strCountID, int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4]),
                           int(result[5]), int(result[6]), int(result[7]),
                           int(result[8]),strInfo))
        print resultdata
class Education_F:
    def ParserJson(self,url):
        result = json.load(urllib.urlopen(url))
        data =[]
        resultdata = []
        CountyId = result["Info"][0]
        for each in result['RowDataList']:
            self.CombindData(each, data, CountyId['InCountyId'])
        self.sumData(data, resultdata)
        self.writeDB(resultdata)
        # for result in data:
        #     print result
    def writeDB(self, data):
        try:
            config=Config_2()
            db = mysql.connector.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd, database=config.dbName)
            db.set_charset_collation('utf8')
            cursor = db.cursor()
            for i in data:
                args = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],
                        i[10])
                # print args
                cursor.callproc('p_edu_county_f', args)
            db.commit()
        except mysql.connector.Error as e:
            db.rollback()
            print(str(e))
        except Exception as e:
            db.rollback()
            print(str(e))
        finally:
            cursor.close()
            db.close()
    def CombindData(self,row,data,county):
        INFO_TIME=row['INFO_TIME'][0:3]
        _phd = int(row['F_A15A19_E1314_CNT']) + int(row['F_A20A24_E1314_CNT']) + \
               int(row['F_A25A29_E1314_CNT']) + int(row['F_A30A34_E1314_CNT'])+ \
               int(row['F_A35A39_E1314_CNT']) + int(row['F_A40A44_E1314_CNT'])+ \
               int(row['F_A45A49_E1314_CNT']) + int(row['F_A50A54_E1314_CNT'])+ \
               int(row['F_A55A59_E1314_CNT']) + int(row['F_A60A64_E1314_CNT'])+ \
               int(row['F_A65UP_E1314_CNT'])
        _master=int(row['F_A15A19_E1112_CNT'])+int(row['F_A20A24_E1112_CNT'])+\
                int(row['F_A25A29_E1112_CNT'])+int(row['F_A30A34_E1112_CNT'])+ \
                int(row['F_A35A39_E1112_CNT']) + int(row['F_A40A44_E1112_CNT'])+ \
                int(row['F_A45A49_E1112_CNT']) + int(row['F_A50A54_E1112_CNT'])+ \
                int(row['F_A55A59_E1112_CNT']) + int(row['F_A60A64_E1112_CNT'])+ \
                int(row['F_A65UP_E1112_CNT'])
        _university=int(row['F_A15A19_E2122_CNT'])+int(row['F_A20A24_E2122_CNT'])+\
                    int(row['F_A25A29_E2122_CNT'])+int(row['F_A30A34_E2122_CNT'])+ \
                    int(row['F_A35A39_E2122_CNT']) + int(row['F_A40A44_E2122_CNT'])+ \
                    int(row['F_A45A49_E2122_CNT']) + int(row['F_A50A54_E2122_CNT'])+ \
                    int(row['F_A55A59_E2122_CNT']) + int(row['F_A60A64_E2122_CNT'])+ \
                    int(row['F_A65UP_E2122_CNT'])
        _college=int(row['F_A15A19_E3_4_5_CNT'])+int(row['F_A20A24_E3_4_5_CNT'])+\
                 int(row['F_A25A29_E3_4_5_CNT'])+int(row['F_A30A34_E3_4_5_CNT'])+ \
                 int(row['F_A35A39_E3_4_5_CNT']) + int(row['F_A40A44_E3_4_5_CNT'])+ \
                 int(row['F_A45A49_E3_4_5_CNT']) + int(row['F_A50A54_E3_4_5_CNT'])+ \
                 int(row['F_A55A59_E3_4_5_CNT']) + int(row['F_A60A64_E3_4_5_CNT'])+ \
                 int(row['F_A65UP_E3_4_5_CNT'])
        _senior=int(row['F_A15A19_E6_7_CNT'])+int(row['F_A20A24_E6_7_CNT'])+\
                int(row['F_A25A29_E6_7_CNT'])+int(row['F_A30A34_E6_7_CNT'])+ \
                int(row['F_A35A39_E6_7_CNT']) + int(row['F_A40A44_E6_7_CNT'])+ \
                int(row['F_A45A49_E6_7_CNT']) + int(row['F_A50A54_E6_7_CNT'])+ \
                int(row['F_A55A59_E6_7_CNT']) + int(row['F_A60A64_E6_7_CNT'])+ \
                int(row['F_A65UP_E6_7_CNT'])
        _junior=int(row['F_A15A19_E8_9_CNT'])+int(row['F_A20A24_E8_9_CNT'])+\
                int(row['F_A25A29_E8_9_CNT'])+int(row['F_A30A34_E8_9_CNT'])+ \
                int(row['F_A35A39_E8_9_CNT']) + int(row['F_A40A44_E8_9_CNT'])+ \
                int(row['F_A45A49_E8_9_CNT']) + int(row['F_A50A54_E8_9_CNT'])+ \
                int(row['F_A55A59_E8_9_CNT']) + int(row['F_A60A64_E8_9_CNT'])+ \
                int(row['F_A65UP_E8_9_CNT'])
        _primary=int(row['F_A15A19_E1_2_CNT'])+int(row['F_A20A24_E1_2_CNT'])+\
                 int(row['F_A25A29_E1_2_CNT'])+int(row['F_A30A34_E1_2_CNT'])+ \
                 int(row['F_A35A39_E1_2_CNT']) + int(row['F_A40A44_E1_2_CNT'])+ \
                 int(row['F_A45A49_E1_2_CNT']) + int(row['F_A50A54_E1_2_CNT'])+ \
                 int(row['F_A55A59_E1_2_CNT']) + int(row['F_A60A64_E1_2_CNT'])+ \
                 int(row['F_A65UP_E1_2_CNT'])
        _self=int(row['F_A15A19_E03_CNT'])+int(row['F_A20A24_E03_CNT'])+\
              int(row['F_A25A29_E03_CNT'])+int(row['F_A30A34_E03_CNT'])+ \
              int(row['F_A35A39_E03_CNT']) + int(row['F_A40A44_E03_CNT'])+ \
              int(row['F_A45A49_E03_CNT']) + int(row['F_A50A54_E03_CNT'])+ \
              int(row['F_A55A59_E03_CNT']) + int(row['F_A60A64_E03_CNT'])+\
              int(row['F_A65UP_E03_CNT'])
        _no=int(row['F_A15A19_E04_CNT'])+int(row['F_A20A24_E04_CNT'])+\
            int(row['F_A25A29_E04_CNT'])+int(row['F_A30A34_E04_CNT'])+ \
            int(row['F_A35A39_E04_CNT']) + int(row['F_A40A44_E04_CNT'])+ \
            int(row['F_A45A49_E04_CNT']) + int(row['F_A50A54_E04_CNT'])+ \
            int(row['F_A55A59_E04_CNT']) + int(row['F_A60A64_E04_CNT'])+ \
            int(row['F_A65UP_E04_CNT'])

        data.append((county,_phd,_master,_university,_college,_senior,_junior,
                     _primary,_self,_no,INFO_TIME))

    def sumData(self, data, resultdata):
        strCountID = ''
        strInfo = ''
        arr = []
        mydata = []
        for row in data:
            arr = []
            # print row
            # mydata.append(data[1],data[2])
            for i in range(len(row)):
                strCountID = row[0]
                strInfo = row[10]
                if i > 0 and i < 10:
                    # print row[i]
                    arr.append(row[i])
            mydata.append(arr)

        mydata2 = numpy.array(mydata)
        result = mydata2.sum(axis=0)
        resultdata.append((strCountID, int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4]),
                           int(result[5]), int(result[6]), int(result[7]),
                           int(result[8]),strInfo))
        print resultdata
class Education_All:
    def ParserJson(self,url):
        result = json.load(urllib.urlopen(url))
        data =[]
        resultdata = []
        CountyId = result["Info"][0]
        for each in result['RowDataList']:
            self.CombindData(each, data, CountyId['InCountyId'])
        self.sumData(data, resultdata)
        self.writeDB(resultdata)
        # for result in data:
        #     print result
    def writeDB(self, data):
        try:
            config=Config_2()
            db = mysql.connector.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd, database=config.dbName)
            db.set_charset_collation('utf8')
            cursor = db.cursor()
            for i in data:
                args = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],
                        i[10])
                # print args
                cursor.callproc('p_edu_county_all', args)
            db.commit()
        except mysql.connector.Error as e:
            db.rollback()
            print(str(e))
        except Exception as e:
            db.rollback()
            print(str(e))
        finally:
            cursor.close()
            db.close()
    def CombindData(self,row,data,county):
        INFO_TIME=row['INFO_TIME'][0:3]
        _phd = int(row['F_A15A19_E1314_CNT']) + int(row['F_A20A24_E1314_CNT']) + \
               int(row['F_A25A29_E1314_CNT']) + int(row['F_A30A34_E1314_CNT'])+ \
               int(row['F_A35A39_E1314_CNT']) + int(row['F_A40A44_E1314_CNT'])+ \
               int(row['F_A45A49_E1314_CNT']) + int(row['F_A50A54_E1314_CNT'])+ \
               int(row['F_A55A59_E1314_CNT']) + int(row['F_A60A64_E1314_CNT'])+ \
               int(row['F_A65UP_E1314_CNT'])+ \
               int(row['M_A15A19_E1314_CNT']) + int(row['M_A20A24_E1314_CNT']) + \
               int(row['M_A25A29_E1314_CNT']) + int(row['M_A30A34_E1314_CNT']) + \
               int(row['M_A35A39_E1314_CNT']) + int(row['M_A40A44_E1314_CNT']) + \
               int(row['M_A45A49_E1314_CNT']) + int(row['M_A50A54_E1314_CNT']) + \
               int(row['M_A55A59_E1314_CNT']) + int(row['M_A60A64_E1314_CNT']) + \
               int(row['M_A65UP_E1314_CNT'])
        _master=int(row['F_A15A19_E1112_CNT'])+int(row['F_A20A24_E1112_CNT'])+\
                int(row['F_A25A29_E1112_CNT'])+int(row['F_A30A34_E1112_CNT'])+ \
                int(row['F_A35A39_E1112_CNT']) + int(row['F_A40A44_E1112_CNT'])+ \
                int(row['F_A45A49_E1112_CNT']) + int(row['F_A50A54_E1112_CNT'])+ \
                int(row['F_A55A59_E1112_CNT']) + int(row['F_A60A64_E1112_CNT'])+ \
                int(row['F_A65UP_E1112_CNT'])+ \
                int(row['M_A15A19_E1112_CNT']) + int(row['M_A20A24_E1112_CNT']) + \
                int(row['M_A25A29_E1112_CNT']) + int(row['M_A30A34_E1112_CNT']) + \
                int(row['M_A35A39_E1112_CNT']) + int(row['M_A40A44_E1112_CNT']) + \
                int(row['M_A45A49_E1112_CNT']) + int(row['M_A50A54_E1112_CNT']) + \
                int(row['M_A55A59_E1112_CNT']) + int(row['M_A60A64_E1112_CNT']) + \
                int(row['M_A65UP_E1112_CNT'])
        _university=int(row['F_A15A19_E2122_CNT'])+int(row['F_A20A24_E2122_CNT'])+\
                    int(row['F_A25A29_E2122_CNT'])+int(row['F_A30A34_E2122_CNT'])+ \
                    int(row['F_A35A39_E2122_CNT']) + int(row['F_A40A44_E2122_CNT'])+ \
                    int(row['F_A45A49_E2122_CNT']) + int(row['F_A50A54_E2122_CNT'])+ \
                    int(row['F_A55A59_E2122_CNT']) + int(row['F_A60A64_E2122_CNT'])+ \
                    int(row['F_A65UP_E2122_CNT'])+ \
                    int(row['M_A15A19_E2122_CNT']) + int(row['M_A20A24_E2122_CNT']) + \
                    int(row['M_A25A29_E2122_CNT']) + int(row['M_A30A34_E2122_CNT']) + \
                    int(row['M_A35A39_E2122_CNT']) + int(row['M_A40A44_E2122_CNT']) + \
                    int(row['M_A45A49_E2122_CNT']) + int(row['M_A50A54_E2122_CNT']) + \
                    int(row['M_A55A59_E2122_CNT']) + int(row['M_A60A64_E2122_CNT']) + \
                    int(row['M_A65UP_E2122_CNT'])
        _college=int(row['F_A15A19_E3_4_5_CNT'])+int(row['F_A20A24_E3_4_5_CNT'])+\
                 int(row['F_A25A29_E3_4_5_CNT'])+int(row['F_A30A34_E3_4_5_CNT'])+ \
                 int(row['F_A35A39_E3_4_5_CNT']) + int(row['F_A40A44_E3_4_5_CNT'])+ \
                 int(row['F_A45A49_E3_4_5_CNT']) + int(row['F_A50A54_E3_4_5_CNT'])+ \
                 int(row['F_A55A59_E3_4_5_CNT']) + int(row['F_A60A64_E3_4_5_CNT'])+ \
                 int(row['F_A65UP_E3_4_5_CNT'])+ \
                 int(row['M_A15A19_E3_4_5_CNT']) + int(row['M_A20A24_E3_4_5_CNT']) + \
                 int(row['M_A25A29_E3_4_5_CNT']) + int(row['M_A30A34_E3_4_5_CNT']) + \
                 int(row['M_A35A39_E3_4_5_CNT']) + int(row['M_A40A44_E3_4_5_CNT']) + \
                 int(row['M_A45A49_E3_4_5_CNT']) + int(row['M_A50A54_E3_4_5_CNT']) + \
                 int(row['M_A55A59_E3_4_5_CNT']) + int(row['M_A60A64_E3_4_5_CNT']) + \
                 int(row['M_A65UP_E3_4_5_CNT'])
        _senior=int(row['F_A15A19_E6_7_CNT'])+int(row['F_A20A24_E6_7_CNT'])+\
                int(row['F_A25A29_E6_7_CNT'])+int(row['F_A30A34_E6_7_CNT'])+ \
                int(row['F_A35A39_E6_7_CNT']) + int(row['F_A40A44_E6_7_CNT'])+ \
                int(row['F_A45A49_E6_7_CNT']) + int(row['F_A50A54_E6_7_CNT'])+ \
                int(row['F_A55A59_E6_7_CNT']) + int(row['F_A60A64_E6_7_CNT'])+ \
                int(row['F_A65UP_E6_7_CNT'])+ \
                int(row['M_A15A19_E6_7_CNT']) + int(row['M_A20A24_E6_7_CNT']) + \
                int(row['M_A25A29_E6_7_CNT']) + int(row['M_A30A34_E6_7_CNT']) + \
                int(row['M_A35A39_E6_7_CNT']) + int(row['M_A40A44_E6_7_CNT']) + \
                int(row['M_A45A49_E6_7_CNT']) + int(row['M_A50A54_E6_7_CNT']) + \
                int(row['M_A55A59_E6_7_CNT']) + int(row['M_A60A64_E6_7_CNT']) + \
                int(row['M_A65UP_E6_7_CNT'])
        _junior=int(row['F_A15A19_E8_9_CNT'])+int(row['F_A20A24_E8_9_CNT'])+\
                int(row['F_A25A29_E8_9_CNT'])+int(row['F_A30A34_E8_9_CNT'])+ \
                int(row['F_A35A39_E8_9_CNT']) + int(row['F_A40A44_E8_9_CNT'])+ \
                int(row['F_A45A49_E8_9_CNT']) + int(row['F_A50A54_E8_9_CNT'])+ \
                int(row['F_A55A59_E8_9_CNT']) + int(row['F_A60A64_E8_9_CNT'])+ \
                int(row['F_A65UP_E8_9_CNT'])+ \
                int(row['M_A15A19_E8_9_CNT']) + int(row['M_A20A24_E8_9_CNT']) + \
                int(row['M_A25A29_E8_9_CNT']) + int(row['M_A30A34_E8_9_CNT']) + \
                int(row['M_A35A39_E8_9_CNT']) + int(row['M_A40A44_E8_9_CNT']) + \
                int(row['M_A45A49_E8_9_CNT']) + int(row['M_A50A54_E8_9_CNT']) + \
                int(row['M_A55A59_E8_9_CNT']) + int(row['M_A60A64_E8_9_CNT']) + \
                int(row['M_A65UP_E8_9_CNT'])
        _primary=int(row['F_A15A19_E1_2_CNT'])+int(row['F_A20A24_E1_2_CNT'])+\
                 int(row['F_A25A29_E1_2_CNT'])+int(row['F_A30A34_E1_2_CNT'])+ \
                 int(row['F_A35A39_E1_2_CNT']) + int(row['F_A40A44_E1_2_CNT'])+ \
                 int(row['F_A45A49_E1_2_CNT']) + int(row['F_A50A54_E1_2_CNT'])+ \
                 int(row['F_A55A59_E1_2_CNT']) + int(row['F_A60A64_E1_2_CNT'])+ \
                 int(row['F_A65UP_E1_2_CNT'])+ \
                 int(row['M_A15A19_E1_2_CNT']) + int(row['M_A20A24_E1_2_CNT']) + \
                 int(row['M_A25A29_E1_2_CNT']) + int(row['M_A30A34_E1_2_CNT']) + \
                 int(row['M_A35A39_E1_2_CNT']) + int(row['M_A40A44_E1_2_CNT']) + \
                 int(row['M_A45A49_E1_2_CNT']) + int(row['M_A50A54_E1_2_CNT']) + \
                 int(row['M_A55A59_E1_2_CNT']) + int(row['M_A60A64_E1_2_CNT']) + \
                 int(row['M_A65UP_E1_2_CNT'])
        _self=int(row['F_A15A19_E03_CNT'])+int(row['F_A20A24_E03_CNT'])+\
              int(row['F_A25A29_E03_CNT'])+int(row['F_A30A34_E03_CNT'])+ \
              int(row['F_A35A39_E03_CNT']) + int(row['F_A40A44_E03_CNT'])+ \
              int(row['F_A45A49_E03_CNT']) + int(row['F_A50A54_E03_CNT'])+ \
              int(row['F_A55A59_E03_CNT']) + int(row['F_A60A64_E03_CNT'])+\
              int(row['F_A65UP_E03_CNT'])+ \
              int(row['M_A15A19_E03_CNT']) + int(row['M_A20A24_E03_CNT']) + \
              int(row['M_A25A29_E03_CNT']) + int(row['M_A30A34_E03_CNT']) + \
              int(row['M_A35A39_E03_CNT']) + int(row['M_A40A44_E03_CNT']) + \
              int(row['M_A45A49_E03_CNT']) + int(row['M_A50A54_E03_CNT']) + \
              int(row['M_A55A59_E03_CNT']) + int(row['M_A60A64_E03_CNT']) + \
              int(row['M_A65UP_E03_CNT'])
        _no=int(row['F_A15A19_E04_CNT'])+int(row['F_A20A24_E04_CNT'])+\
            int(row['F_A25A29_E04_CNT'])+int(row['F_A30A34_E04_CNT'])+ \
            int(row['F_A35A39_E04_CNT']) + int(row['F_A40A44_E04_CNT'])+ \
            int(row['F_A45A49_E04_CNT']) + int(row['F_A50A54_E04_CNT'])+ \
            int(row['F_A55A59_E04_CNT']) + int(row['F_A60A64_E04_CNT'])+ \
            int(row['F_A65UP_E04_CNT'])+ \
            int(row['M_A15A19_E04_CNT']) + int(row['M_A20A24_E04_CNT']) + \
            int(row['M_A25A29_E04_CNT']) + int(row['M_A30A34_E04_CNT']) + \
            int(row['M_A35A39_E04_CNT']) + int(row['M_A40A44_E04_CNT']) + \
            int(row['M_A45A49_E04_CNT']) + int(row['M_A50A54_E04_CNT']) + \
            int(row['M_A55A59_E04_CNT']) + int(row['M_A60A64_E04_CNT']) + \
            int(row['M_A65UP_E04_CNT'])

        data.append((county,_phd,_master,_university,_college,_senior,_junior,
                     _primary,_self,_no,INFO_TIME))

    def sumData(self, data, resultdata):
        strCountID = ''
        strInfo = ''
        arr = []
        mydata = []
        for row in data:
            arr = []
            # print row
            # mydata.append(data[1],data[2])
            for i in range(len(row)):
                strCountID = row[0]
                strInfo = row[10]
                if i > 0 and i < 10:
                    # print row[i]
                    arr.append(row[i])
            mydata.append(arr)

        mydata2 = numpy.array(mydata)
        result = mydata2.sum(axis=0)
        resultdata.append((strCountID, int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4]),
                           int(result[5]), int(result[6]), int(result[7]),
                           int(result[8]),strInfo))
        print resultdata