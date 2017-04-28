# -*-  coding: utf-8  -*-
__author__ = '10409003'
import json
import urllib
import mysql.connector
import numpy
from setting import Config_2
import logging, time


logger = logging.getLogger(__name__)

class marriage():
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
                args = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
                # print args
                cursor.callproc('p_marriage_county', args)
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

    def CombindData(self, row, data, county):
        INFO_TIME = row['INFO_TIME'][0:3]
        # CODE2 = row['CODE2']
        unmarried_m = int(row['M_A15A19_M1_CNT']) + int(row['M_A20A24_M1_CNT']) + int(row['M_A25A29_M1_CNT']) +\
                      int(row['M_A30A34_M1_CNT']) + int(row['M_A35A39_M1_CNT']) + int(row['M_A40A44_M1_CNT']) + \
                      int(row['M_A45A49_M1_CNT']) + int(row['M_A50A54_M1_CNT']) + \
                      int(row['M_A55A59_M1_CNT']) + int(row['M_A60A64_M1_CNT']) + int(row['M_A65A69_M1_CNT']) + \
                      int(row['M_A70A74_M1_CNT']) + int(row['M_A75A79_M1_CNT']) + int(row['M_A80A84_M1_CNT']) + \
                      int(row['M_A85A89_M1_CNT']) + int(row['M_A90A94_M1_CNT']) + \
                      int(row['M_A95A99_M1_CNT']) + int(row['M_A100UP_M1_CNT'])

        unmarried_f = int(row['F_A15A19_M1_CNT']) + int(row['F_A20A24_M1_CNT']) + int(row['F_A25A29_M1_CNT']) + \
                      int(row['F_A30A34_M1_CNT']) + int(row['F_A35A39_M1_CNT']) + int(row['F_A40A44_M1_CNT']) + \
                      int(row['F_A45A49_M1_CNT']) + int(row['F_A50A54_M1_CNT']) + \
                      int(row['F_A55A59_M1_CNT']) + int(row['F_A60A64_M1_CNT']) + int(row['F_A65A69_M1_CNT']) + \
                      int(row['F_A70A74_M1_CNT']) + int(row['F_A75A79_M1_CNT']) + int(row['F_A80A84_M1_CNT']) + \
                      int(row['F_A85A89_M1_CNT']) + int(row['F_A90A94_M1_CNT']) + \
                      int(row['F_A95A99_M1_CNT']) + int(row['F_A100UP_M1_CNT'])

        married_m = int(row['M_A15A19_M2_CNT']) + int(row['M_A20A24_M2_CNT']) + int(row['M_A25A29_M2_CNT']) + \
                    int(row['M_A30A34_M2_CNT']) + int(row['M_A35A39_M2_CNT']) + int(row['M_A40A44_M2_CNT']) + \
                    int(row['M_A45A49_M2_CNT']) + int(row['M_A50A54_M2_CNT']) + int(row['M_A55A59_M2_CNT']) + \
                    int(row['M_A60A64_M2_CNT']) + int(row['M_A65A69_M2_CNT']) + int(row['M_A70A74_M2_CNT']) + \
                    int(row['M_A75A79_M2_CNT']) + int(row['M_A80A84_M2_CNT']) + int(row['M_A85A89_M2_CNT']) + \
                    int(row['M_A90A94_M2_CNT']) + int(row['M_A95A99_M2_CNT']) + int(row['M_A100UP_M2_CNT'])

        married_f = int(row['F_A15A19_M2_CNT']) + int(row['F_A20A24_M2_CNT']) + int(row['F_A25A29_M2_CNT']) + \
                    int(row['F_A30A34_M2_CNT']) + int(row['F_A35A39_M2_CNT']) + int(row['F_A40A44_M2_CNT']) + \
                    int(row['F_A45A49_M2_CNT']) + int(row['F_A50A54_M2_CNT']) + int(row['F_A55A59_M2_CNT']) + \
                    int(row['F_A60A64_M2_CNT']) + int(row['F_A65A69_M2_CNT']) + int(row['F_A70A74_M2_CNT']) + \
                    int(row['F_A75A79_M2_CNT']) + int(row['F_A80A84_M2_CNT']) + int(row['F_A85A89_M2_CNT']) + \
                    int(row['F_A90A94_M2_CNT']) + int(row['F_A95A99_M2_CNT']) + int(row['F_A100UP_M2_CNT'])

        divorce_m = int(row['M_A15A19_M3_CNT']) + int(row['M_A20A24_M3_CNT']) + int(row['M_A25A29_M3_CNT']) + \
                    int(row['M_A30A34_M3_CNT']) + int(row['M_A35A39_M3_CNT']) + int(row['M_A40A44_M3_CNT']) + \
                    int(row['M_A45A49_M3_CNT']) + int(row['M_A50A54_M3_CNT']) + int(row['M_A55A59_M3_CNT']) + \
                    int(row['M_A60A64_M3_CNT']) + int(row['M_A65A69_M3_CNT']) + int(row['M_A70A74_M3_CNT']) + \
                    int(row['M_A75A79_M3_CNT']) + int(row['M_A80A84_M3_CNT']) + int(row['M_A85A89_M3_CNT']) + \
                    int(row['M_A90A94_M3_CNT']) + int(row['M_A95A99_M3_CNT']) + int(row['M_A100UP_M3_CNT'])

        divorce_f = int(row['F_A15A19_M3_CNT']) + int(row['F_A20A24_M3_CNT']) + int(row['F_A25A29_M3_CNT']) + \
                    int(row['F_A30A34_M3_CNT']) + int(row['F_A35A39_M3_CNT']) + int(row['F_A40A44_M3_CNT']) + \
                    int(row['F_A45A49_M3_CNT']) + int(row['F_A50A54_M3_CNT']) + int(row['F_A55A59_M3_CNT']) + \
                    int(row['F_A60A64_M3_CNT']) + int(row['F_A65A69_M3_CNT']) + int(row['F_A70A74_M3_CNT']) + \
                    int(row['F_A75A79_M3_CNT']) + int(row['F_A80A84_M3_CNT']) + int(row['F_A85A89_M3_CNT']) + \
                    int(row['F_A90A94_M3_CNT']) + int(row['F_A95A99_M3_CNT']) + int(row['F_A100UP_M3_CNT'])

        widowed_m = int(row['M_A15A19_M4_CNT']) + int(row['M_A20A24_M4_CNT']) + int(row['M_A25A29_M4_CNT']) + \
                    int(row['M_A30A34_M4_CNT']) + int(row['M_A35A39_M4_CNT']) + int(row['M_A40A44_M4_CNT']) + \
                    int(row['M_A45A49_M4_CNT']) + int(row['M_A50A54_M4_CNT']) + int(row['M_A55A59_M4_CNT']) + \
                    int(row['M_A60A64_M4_CNT']) + int(row['M_A65A69_M4_CNT']) + int(row['M_A70A74_M4_CNT']) + \
                    int(row['M_A75A79_M4_CNT']) + int(row['M_A80A84_M4_CNT']) + int(row['M_A85A89_M4_CNT']) + \
                    int(row['M_A90A94_M4_CNT']) + int(row['M_A95A99_M4_CNT']) + int(row['M_A100UP_M4_CNT'])

        widowed_f = int(row['F_A15A19_M4_CNT']) + int(row['F_A20A24_M4_CNT']) + int(row['F_A25A29_M4_CNT']) + \
                    int(row['F_A30A34_M4_CNT']) + int(row['F_A35A39_M4_CNT']) + int(row['F_A40A44_M4_CNT']) + \
                    int(row['F_A45A49_M4_CNT']) + int(row['F_A50A54_M4_CNT']) + int(row['F_A55A59_M4_CNT']) + \
                    int(row['F_A60A64_M4_CNT']) + int(row['F_A65A69_M4_CNT']) + int(row['F_A70A74_M4_CNT']) + \
                    int(row['F_A75A79_M4_CNT']) + int(row['F_A80A84_M4_CNT']) + int(row['F_A85A89_M4_CNT']) + \
                    int(row['F_A90A94_M4_CNT']) + int(row['F_A95A99_M4_CNT']) + int(row['F_A100UP_M4_CNT'])
        data.append((county, unmarried_m, unmarried_f, married_m, married_f, divorce_m, divorce_f, widowed_m,
                     widowed_f, INFO_TIME))

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
                strInfo = row[9]
                if i > 0 and i < 9:
                    # print row[i]
                    arr.append(row[i])
            mydata.append(arr)
        mydata2 = numpy.array(mydata)
        result = mydata2.sum(axis=0)
        resultdata.append((strCountID, int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4]),\
                           int(result[5]), int(result[6]), int(result[7]), strInfo))
        print resultdata

if __name__=='__main__':
    mssql = marriage()
    print mssql.ParserJson(url ='http://segisws.moi.gov.tw/STATWSSTData/OpenService.asmx/GetStatSTDataForOpenCode?oCode=6E03CA29B955A854D8F52522E38D8C7051A1FBEE829C41DBC09B9B1454506F40784066447C59ACA8118135321DF5C2FCC93C1F4155955501' )