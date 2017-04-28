# -*-  coding: utf-8  -*-
__author__ = '10409003'
import json,urllib
import mysql.connector
import numpy
from setting import Config_2
import logging, time

logger = logging.getLogger(__name__)

class FiveYear_M():
    def ParserJson(self,url):
        try:
            logging.basicConfig(filename='/data/Population_Data/pyupload.log',
                                level=logging.DEBUG,
                                format='%(asctime)s - %(levelname)s - %(filename)s:%(name)s:%(module)s/%(funcName)s/%(lineno)d - %(message)s',
                                datefmt='%Y/%m/%d %I:%M:%S %p')
            logging.Formatter.converter = time.gmtime

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
        except Exception as e:
            print e.message
            logger.debug(e.message)
        finally:
            return 'finish'

    def writeDB(self, data):
        try:
            config=Config_2()
            db = mysql.connector.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd, database=config.dbName)
            db.set_charset_collation('utf8')
            cursor = db.cursor()
            for i in data:
                args = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],
                        i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19],
                        i[20], i[21], i[22])
                # print args
                cursor.callproc('p_age_county_m', args)
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
        #PRODUCT_ID=row['PRODUCT_ID']
        INFO_TIME=row['INFO_TIME'][0:3]
        #CODE2=row['CODE2']
        A0A4_M_CNT=int(row['A0A4_M_CNT'])
        A5A9_M_CNT=int(row['A5A9_M_CNT'])
        A10A14_M_CNT=int(row['A10A14_M_CNT'])
        A15A19_M_CNT=int(row['A15A19_M_CNT'])
        A20A24_M_CNT=int(row['A20A24_M_CNT'])
        A25A29_M_CNT=int(row['A25A29_M_CNT'])
        A30A34_M_CNT=int(row['A30A34_M_CNT'])
        A35A39_M_CNT=int(row['A35A39_M_CNT'])
        A40A44_M_CNT=int(row['A40A44_M_CNT'])
        A45A49_M_CNT=int(row['A45A49_M_CNT'])
        A50A54_M_CNT=int(row['A50A54_M_CNT'])
        A55A59_M_CNT=int(row['A55A59_M_CNT'])
        A60A64_M_CNT=int(row['A60A64_M_CNT'])
        A65A69_M_CNT=int(row['A65A69_M_CNT'])
        A70A74_M_CNT=int(row['A70A74_M_CNT'])
        A75A79_M_CNT=int(row['A75A79_M_CNT'])
        A80A84_M_CNT=int(row['A80A84_M_CNT'])
        A85A89_M_CNT=int(row['A85A89_M_CNT'])
        A90A94_M_CNT=int(row['A90A94_M_CNT'])
        A95A99_M_CNT=int(row['A95A99_M_CNT'])
        A100UP_M_5_CNT=int(row['A100UP_M_5_CNT'])

        data.append((county,A0A4_M_CNT,A5A9_M_CNT,
                A10A14_M_CNT,A15A19_M_CNT,A20A24_M_CNT,A25A29_M_CNT,A30A34_M_CNT,
                A35A39_M_CNT,A40A44_M_CNT,A45A49_M_CNT,A50A54_M_CNT,A55A59_M_CNT,
                A60A64_M_CNT,A65A69_M_CNT,A70A74_M_CNT,A75A79_M_CNT,A80A84_M_CNT,A85A89_M_CNT,
                A90A94_M_CNT,A95A99_M_CNT,A100UP_M_5_CNT,INFO_TIME))

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
                strInfo = row[22]
                if i > 0 and i < 22:
                    # print row[i]
                    arr.append(row[i])
            mydata.append(arr)

        mydata2 = numpy.array(mydata)
        result = mydata2.sum(axis=0)
        resultdata.append((strCountID, int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4]),
                           int(result[5]), int(result[6]), int(result[7]),
                           int(result[8]), int(result[9]), int(result[10]),
                           int(result[11]), int(result[12]), int(result[13]),
                           int(result[14]), int(result[15]), int(result[16]),
                           int(result[17]), int(result[18]), int(result[19]),
                           int(result[20]),strInfo))
        print resultdata

class FiveYear_F():
    def ParserJson(self, url):
        try:
            logging.basicConfig(filename='/data/Population_Data/pyupload.log',
                                level=logging.DEBUG,
                                format='%(asctime)s - %(levelname)s - %(filename)s:%(name)s:%(module)s/%(funcName)s/%(lineno)d - %(message)s',
                                datefmt='%Y/%m/%d %I:%M:%S %p')
            logging.Formatter.converter = time.gmtime

            result = json.load(urllib.urlopen(url))
            data = []
            resultdata = []
            CountyId = result["Info"][0]
            for each in result['RowDataList']:
                self.CombindData(each, data, CountyId['InCountyId'])
            self.sumData(data, resultdata)
            self.writeDB(resultdata)
            # for result in data:
            #     print result

        except Exception as e:
            print e.message
            logger.debug(e.message)

        finally:
            return 'finish'

    def writeDB(self, data):
        try:
            config = Config_2()
            db = mysql.connector.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd, database=config.dbName)
            db.set_charset_collation('utf8')
            cursor = db.cursor()
            for i in data:
                args = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],
                        i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19],
                        i[20], i[21], i[22])
                # print args
                cursor.callproc('p_age_county_f', args)
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

    def CombindData(self, row, data,county):
        INFO_TIME = row['INFO_TIME'][0:3]
        A0A4_F_CNT = int(row['A0A4_F_CNT'])
        A5A9_F_CNT = int(row['A5A9_F_CNT'])
        A10A14_F_CNT = int(row['A10A14_F_CNT'])
        A15A19_F_CNT = int(row['A15A19_F_CNT'])
        A20A24_F_CNT = int(row['A20A24_F_CNT'])
        A25A29_F_CNT = int(row['A25A29_F_CNT'])
        A30A34_F_CNT = int(row['A30A34_F_CNT'])
        A35A39_F_CNT = int(row['A35A39_F_CNT'])
        A40A44_F_CNT = int(row['A40A44_F_CNT'])
        A45A49_F_CNT = int(row['A45A49_F_CNT'])
        A50A54_F_CNT = int(row['A50A54_F_CNT'])
        A55A59_F_CNT = int(row['A55A59_F_CNT'])
        A60A64_F_CNT = int(row['A60A64_F_CNT'])
        A65A69_F_CNT = int(row['A65A69_F_CNT'])
        A70A74_F_CNT = int(row['A70A74_F_CNT'])
        A75A79_F_CNT = int(row['A75A79_F_CNT'])
        A80A84_F_CNT = int(row['A80A84_F_CNT'])
        A85A89_F_CNT = int(row['A85A89_F_CNT'])
        A90A94_F_CNT = int(row['A90A94_F_CNT'])
        A95A99_F_CNT = int(row['A95A99_F_CNT'])
        A100UP_F_5_CNT = int(row['A100UP_F_5_CNT'])

        data.append((county,A0A4_F_CNT,A5A9_F_CNT,
                     A10A14_F_CNT, A15A19_F_CNT, A20A24_F_CNT, A25A29_F_CNT, A30A34_F_CNT,
                     A35A39_F_CNT, A40A44_F_CNT, A45A49_F_CNT, A50A54_F_CNT,
                     A55A59_F_CNT, A60A64_F_CNT, A65A69_F_CNT, A70A74_F_CNT,
                     A75A79_F_CNT, A80A84_F_CNT,A85A89_F_CNT,
                     A90A94_F_CNT, A95A99_F_CNT, A100UP_F_5_CNT, INFO_TIME))


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
                strInfo = row[22]
                if i > 0 and i < 22:
                    # print row[i]
                    arr.append(row[i])
            mydata.append(arr)

        mydata2 = numpy.array(mydata)
        result = mydata2.sum(axis=0)
        resultdata.append(
            (strCountID, int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4]),
             int(result[5]), int(result[6]), int(result[7]),
             int(result[8]), int(result[9]), int(result[10]),
             int(result[11]), int(result[12]), int(result[13]),
             int(result[14]), int(result[15]), int(result[16]),
             int(result[17]), int(result[18]), int(result[19]),
             int(result[20]), strInfo))
        print resultdata

class FiveYear_All():
    def ParserJson(self, url):
        try:
            logging.basicConfig(filename='/data/Population_Data/pyupload.log',
                                level=logging.DEBUG,
                                format='%(asctime)s - %(levelname)s - %(filename)s:%(name)s:%(module)s/%(funcName)s/%(lineno)d - %(message)s',
                                datefmt='%Y/%m/%d %I:%M:%S %p')
            logging.Formatter.converter = time.gmtime
            result = json.load(urllib.urlopen(url))
            data = []
            resultdata = []
            CountyId = result["Info"][0]
            for each in result['RowDataList']:
                self.CombindData(each, data, CountyId['InCountyId'])
            self.sumData(data, resultdata)
            self.writeDB(resultdata)
            # for result in data:
            #     print result
        except Exception as e:
            print e.message
            logging.error(e.message)

        finally:
            return 'finish'


    def writeDB(self, data):
        try:
            config=Config_2()
            db = mysql.connector.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd, database=config.dbName)
            db.set_charset_collation('utf8')
            cursor = db.cursor()
            for i in data:
                args = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],
                        i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19],
                        i[20], i[21], i[22])
                # print args
                cursor.callproc('p_age_county_all', args)
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

    def CombindData(self, row, data,county):
        PRODUCT_ID = row['PRODUCT_ID']
        INFO_TIME = row['INFO_TIME'][0:3]
        CODE2 = row['CODE2']
        A0A4_CNT = int(row['A0A4_CNT'])
        A5A9_CNT = int(row['A5A9_CNT'])
        A10A14_CNT = int(row['A10A14_CNT'])
        A15A19_CNT = int(row['A15A19_CNT'])
        A20A24_CNT = int(row['A20A24_CNT'])
        A25A29_CNT = int(row['A25A29_CNT'])
        A30A34_CNT = int(row['A30A34_CNT'])
        A35A39_CNT = int(row['A35A39_CNT'])
        A40A44_CNT = int(row['A40A44_CNT'])
        A45A49_CNT = int(row['A45A49_CNT'])
        A50A54_CNT = int(row['A50A54_CNT'])
        A55A59_CNT = int(row['A55A59_CNT'])
        A60A64_CNT = int(row['A60A64_CNT'])
        A65A69_CNT = int(row['A65A69_CNT'])
        A70A74_CNT = int(row['A70A74_CNT'])
        A75A79_CNT = int(row['A75A79_CNT'])
        A80A84_CNT = int(row['A80A84_CNT'])
        A85A89_CNT = int(row['A85A89_CNT'])
        A90A94_CNT = int(row['A90A94_CNT'])
        A95A99_CNT = int(row['A95A99_CNT'])
        A100UP_5_CNT = int(row['A100UP_5_CNT'])

        data.append((county, A0A4_CNT, A5A9_CNT,A10A14_CNT,
                     A15A19_CNT, A20A24_CNT,A25A29_CNT,A30A34_CNT,
                     A35A39_CNT, A40A44_CNT, A45A49_CNT,A50A54_CNT, A55A59_CNT,
                     A60A64_CNT, A65A69_CNT,A70A74_CNT,A75A79_CNT, A80A84_CNT, A85A89_CNT,
                     A90A94_CNT, A95A99_CNT, A100UP_5_CNT,INFO_TIME))


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
                strInfo = row[22]
                if i > 0 and i < 22:
                    # print row[i]
                    arr.append(row[i])
            mydata.append(arr)

        mydata2 = numpy.array(mydata)
        result = mydata2.sum(axis=0)
        resultdata.append(
            (strCountID, int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4]),
             int(result[5]), int(result[6]), int(result[7]),
             int(result[8]), int(result[9]), int(result[10]),
             int(result[11]), int(result[12]), int(result[13]),
             int(result[14]), int(result[15]), int(result[16]),
             int(result[17]), int(result[18]), int(result[19]),
             int(result[20]),strInfo))
        print resultdata

if __name__=='__main__':
    mssql = FiveYear_F()
    print mssql.ParserJson(url ='http://segisws.moi.gov.tw/STATWSSTData/OpenService.asmx/GetStatSTDataForOpenCode?oCode=6E03CA29B955A854D8F52522E38D8C7051A1FBEE829C41DBAA621E921CCAA2C59B8468D8E9726F6F71F479EBD1A8F092D8BBECC4B34231B0' )
