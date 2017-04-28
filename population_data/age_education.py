# -*-  coding: utf-8  -*-
__author__ = '10409003'
import json,urllib
import mysql.connector
import numpy
from setting import Config_2
import logging, time

logger = logging.getLogger(__name__)

class Age_Education_M():
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
                        i[10],i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19],
                        i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28], i[29],
                        i[30], i[31], i[32], i[33], i[34], i[35], i[36], i[37], i[38], i[39],
                        i[40], i[41], i[42], i[43], i[44], i[45], i[46], i[47], i[48], i[49],
                        i[50], i[51], i[52], i[53], i[54], i[55], i[56], i[57], i[58], i[59],
                        i[60], i[61], i[62], i[63], i[64], i[65], i[66], i[67], i[68], i[69],
                        i[70], i[71], i[72], i[73], i[74], i[75], i[76], i[77], i[78], i[79],
                        i[80], i[81], i[82], i[83], i[84], i[85], i[86], i[87], i[88], i[89],
                        i[90], i[91], i[92], i[93], i[94], i[95], i[96], i[97], i[98], i[99],
                        i[100]
                        )
                # print args
                cursor.callproc('p_age_edu_county_m', args)
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
        M_A15A19_E1314_CNT = row['M_A15A19_E1314_CNT']
        M_A15A19_E1112_CNT = row['M_A15A19_E1112_CNT']
        M_A15A19_E2122_CNT = row['M_A15A19_E2122_CNT']
        M_A15A19_E3_4_5_CNT = row['M_A15A19_E3_4_5_CNT']
        M_A15A19_E6_7_CNT = row['M_A15A19_E6_7_CNT']
        M_A15A19_E8_9_CNT = row['M_A15A19_E8_9_CNT']
        M_A15A19_E1_2_CNT = row['M_A15A19_E1_2_CNT']
        M_A15A19_E03_CNT = row['M_A15A19_E03_CNT']
        M_A15A19_E04_CNT = row['M_A15A19_E04_CNT']
        M_A20A24_E1314_CNT = row['M_A20A24_E1314_CNT']
        M_A20A24_E1112_CNT = row['M_A20A24_E1112_CNT']
        M_A20A24_E2122_CNT = row['M_A20A24_E2122_CNT']
        M_A20A24_E3_4_5_CNT = row['M_A20A24_E3_4_5_CNT']
        M_A20A24_E6_7_CNT = row['M_A20A24_E6_7_CNT']
        M_A20A24_E8_9_CNT = row['M_A20A24_E8_9_CNT']
        M_A20A24_E1_2_CNT = row['M_A20A24_E1_2_CNT']
        M_A20A24_E03_CNT = row['M_A20A24_E03_CNT']
        M_A20A24_E04_CNT = row['M_A20A24_E04_CNT']
        M_A25A29_E1314_CNT = row['M_A25A29_E1314_CNT']
        M_A25A29_E1112_CNT = row['M_A25A29_E1112_CNT']
        M_A25A29_E2122_CNT = row['M_A25A29_E2122_CNT']
        M_A25A29_E3_4_5_CNT = row['M_A25A29_E3_4_5_CNT']
        M_A25A29_E6_7_CNT = row['M_A25A29_E6_7_CNT']
        M_A25A29_E8_9_CNT = row['M_A25A29_E8_9_CNT']
        M_A25A29_E1_2_CNT = row['M_A25A29_E1_2_CNT']
        M_A25A29_E03_CNT = row['M_A25A29_E03_CNT']
        M_A25A29_E04_CNT = row['M_A25A29_E04_CNT']
        M_A30A34_E1314_CNT = row['M_A30A34_E1314_CNT']
        M_A30A34_E1112_CNT = row['M_A30A34_E1112_CNT']
        M_A30A34_E2122_CNT = row['M_A30A34_E2122_CNT']
        M_A30A34_E3_4_5_CNT = row['M_A30A34_E3_4_5_CNT']
        M_A30A34_E6_7_CNT = row['M_A30A34_E6_7_CNT']
        M_A30A34_E8_9_CNT = row['M_A30A34_E8_9_CNT']
        M_A30A34_E1_2_CNT = row['M_A30A34_E1_2_CNT']
        M_A30A34_E03_CNT = row['M_A30A34_E03_CNT']
        M_A30A34_E04_CNT = row['M_A30A34_E04_CNT']
        M_A35A39_E1314_CNT = row['M_A35A39_E1314_CNT']
        M_A35A39_E1112_CNT = row['M_A35A39_E1112_CNT']
        M_A35A39_E2122_CNT = row['M_A35A39_E2122_CNT']
        M_A35A39_E3_4_5_CNT = row['M_A35A39_E3_4_5_CNT']
        M_A35A39_E6_7_CNT = row['M_A35A39_E6_7_CNT']
        M_A35A39_E8_9_CNT = row['M_A35A39_E8_9_CNT']
        M_A35A39_E1_2_CNT = row['M_A35A39_E1_2_CNT']
        M_A35A39_E03_CNT = row['M_A35A39_E03_CNT']
        M_A35A39_E04_CNT = row['M_A35A39_E04_CNT']
        M_A40A44_E1314_CNT = row['M_A40A44_E1314_CNT']
        M_A40A44_E1112_CNT = row['M_A40A44_E1112_CNT']
        M_A40A44_E2122_CNT = row['M_A40A44_E2122_CNT']
        M_A40A44_E3_4_5_CNT = row['M_A40A44_E3_4_5_CNT']
        M_A40A44_E6_7_CNT = row['M_A40A44_E6_7_CNT']
        M_A40A44_E8_9_CNT = row['M_A40A44_E8_9_CNT']
        M_A40A44_E1_2_CNT = row['M_A40A44_E1_2_CNT']
        M_A40A44_E03_CNT = row['M_A40A44_E03_CNT']
        M_A40A44_E04_CNT = row['M_A40A44_E04_CNT']
        M_A45A49_E1314_CNT = row['M_A45A49_E1314_CNT']
        M_A45A49_E1112_CNT = row['M_A45A49_E1112_CNT']
        M_A45A49_E2122_CNT = row['M_A45A49_E2122_CNT']
        M_A45A49_E3_4_5_CNT = row['M_A45A49_E3_4_5_CNT']
        M_A45A49_E6_7_CNT = row['M_A45A49_E6_7_CNT']
        M_A45A49_E8_9_CNT = row['M_A45A49_E8_9_CNT']
        M_A45A49_E1_2_CNT = row['M_A45A49_E1_2_CNT']
        M_A45A49_E03_CNT = row['M_A45A49_E03_CNT']
        M_A45A49_E04_CNT = row['M_A45A49_E04_CNT']
        M_A50A54_E1314_CNT = row['M_A50A54_E1314_CNT']
        M_A50A54_E1112_CNT = row['M_A50A54_E1112_CNT']
        M_A50A54_E2122_CNT = row['M_A50A54_E2122_CNT']
        M_A50A54_E3_4_5_CNT = row['M_A50A54_E3_4_5_CNT']
        M_A50A54_E6_7_CNT = row['M_A50A54_E6_7_CNT']
        M_A50A54_E8_9_CNT = row['M_A50A54_E8_9_CNT']
        M_A50A54_E1_2_CNT = row['M_A50A54_E1_2_CNT']
        M_A50A54_E03_CNT = row['M_A50A54_E03_CNT']
        M_A50A54_E04_CNT = row['M_A50A54_E04_CNT']
        M_A55A59_E1314_CNT = row['M_A55A59_E1314_CNT']
        M_A55A59_E1112_CNT = row['M_A55A59_E1112_CNT']
        M_A55A59_E2122_CNT = row['M_A55A59_E2122_CNT']
        M_A55A59_E3_4_5_CNT = row['M_A55A59_E3_4_5_CNT']
        M_A55A59_E6_7_CNT = row['M_A55A59_E6_7_CNT']
        M_A55A59_E8_9_CNT = row['M_A55A59_E8_9_CNT']
        M_A55A59_E1_2_CNT = row['M_A55A59_E1_2_CNT']
        M_A55A59_E03_CNT = row['M_A55A59_E03_CNT']
        M_A55A59_E04_CNT = row['M_A55A59_E04_CNT']
        M_A60A64_E1314_CNT = row['M_A60A64_E1314_CNT']
        M_A60A64_E1112_CNT = row['M_A60A64_E1112_CNT']
        M_A60A64_E2122_CNT = row['M_A60A64_E2122_CNT']
        M_A60A64_E3_4_5_CNT = row['M_A60A64_E3_4_5_CNT']
        M_A60A64_E6_7_CNT = row['M_A60A64_E6_7_CNT']
        M_A60A64_E8_9_CNT = row['M_A60A64_E8_9_CNT']
        M_A60A64_E1_2_CNT = row['M_A60A64_E1_2_CNT']
        M_A60A64_E03_CNT = row['M_A60A64_E03_CNT']
        M_A60A64_E04_CNT = row['M_A60A64_E04_CNT']
        M_A65UP_E1314_CNT = row['M_A65UP_E1314_CNT']
        M_A65UP_E1112_CNT = row['M_A65UP_E1112_CNT']
        M_A65UP_E2122_CNT = row['M_A65UP_E2122_CNT']
        M_A65UP_E3_4_5_CNT = row['M_A65UP_E3_4_5_CNT']
        M_A65UP_E6_7_CNT = row['M_A65UP_E6_7_CNT']
        M_A65UP_E8_9_CNT = row['M_A65UP_E8_9_CNT']
        M_A65UP_E1_2_CNT = row['M_A65UP_E1_2_CNT']
        M_A65UP_E03_CNT = row['M_A65UP_E03_CNT']
        M_A65UP_E04_CNT = row['M_A65UP_E04_CNT']

        data.append((county, M_A15A19_E1314_CNT, M_A15A19_E1112_CNT, M_A15A19_E2122_CNT, M_A15A19_E3_4_5_CNT,
                    M_A15A19_E6_7_CNT, M_A15A19_E8_9_CNT, M_A15A19_E1_2_CNT, M_A15A19_E03_CNT, M_A15A19_E04_CNT,
                    M_A20A24_E1314_CNT, M_A20A24_E1112_CNT, M_A20A24_E2122_CNT, M_A20A24_E3_4_5_CNT,
                    M_A20A24_E6_7_CNT, M_A20A24_E8_9_CNT, M_A20A24_E1_2_CNT, M_A20A24_E03_CNT, M_A20A24_E04_CNT,
                    M_A25A29_E1314_CNT, M_A25A29_E1112_CNT, M_A25A29_E2122_CNT, M_A25A29_E3_4_5_CNT,
                    M_A25A29_E6_7_CNT, M_A25A29_E8_9_CNT, M_A25A29_E1_2_CNT,M_A25A29_E03_CNT, M_A25A29_E04_CNT,
                    M_A30A34_E1314_CNT, M_A30A34_E1112_CNT, M_A30A34_E2122_CNT, M_A30A34_E3_4_5_CNT, M_A30A34_E6_7_CNT,
                    M_A30A34_E8_9_CNT, M_A30A34_E1_2_CNT, M_A30A34_E03_CNT, M_A30A34_E04_CNT, M_A35A39_E1314_CNT,
                    M_A35A39_E1112_CNT, M_A35A39_E2122_CNT, M_A35A39_E3_4_5_CNT, M_A35A39_E6_7_CNT, M_A35A39_E8_9_CNT,
                    M_A35A39_E1_2_CNT, M_A35A39_E03_CNT, M_A35A39_E04_CNT, M_A40A44_E1314_CNT, M_A40A44_E1112_CNT,
                    M_A40A44_E2122_CNT, M_A40A44_E3_4_5_CNT, M_A40A44_E6_7_CNT, M_A40A44_E8_9_CNT, M_A40A44_E1_2_CNT,
                    M_A40A44_E03_CNT, M_A40A44_E04_CNT, M_A45A49_E1314_CNT, M_A45A49_E1112_CNT, M_A45A49_E2122_CNT,
                    M_A45A49_E3_4_5_CNT, M_A45A49_E6_7_CNT, M_A45A49_E8_9_CNT, M_A45A49_E1_2_CNT, M_A45A49_E03_CNT, M_A45A49_E04_CNT,
                    M_A50A54_E1314_CNT, M_A50A54_E1112_CNT, M_A50A54_E2122_CNT, M_A50A54_E3_4_5_CNT, M_A50A54_E6_7_CNT,
                    M_A50A54_E8_9_CNT, M_A50A54_E1_2_CNT, M_A50A54_E03_CNT, M_A50A54_E04_CNT, M_A55A59_E1314_CNT,
                    M_A55A59_E1112_CNT, M_A55A59_E2122_CNT, M_A55A59_E3_4_5_CNT,M_A55A59_E6_7_CNT, M_A55A59_E8_9_CNT, M_A55A59_E1_2_CNT,
                    M_A55A59_E03_CNT, M_A55A59_E04_CNT, M_A60A64_E1314_CNT, M_A60A64_E1112_CNT, M_A60A64_E2122_CNT,
                    M_A60A64_E3_4_5_CNT, M_A60A64_E6_7_CNT, M_A60A64_E8_9_CNT,M_A60A64_E1_2_CNT, M_A60A64_E03_CNT, M_A60A64_E04_CNT,
                    M_A65UP_E1314_CNT, M_A65UP_E1112_CNT, M_A65UP_E2122_CNT, M_A65UP_E3_4_5_CNT, M_A65UP_E6_7_CNT,
                    M_A65UP_E8_9_CNT, M_A65UP_E1_2_CNT, M_A65UP_E03_CNT, M_A65UP_E04_CNT, INFO_TIME))

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
                strInfo = row[100]
                if i > 0 and i < 100:
                    # print row[i]
                    arr.append(row[i])
            mydata.append(arr)

        mydata2 = numpy.array(mydata)
        result = mydata2.sum(axis=0)
        resultdata.append((strCountID, int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4]),
                           int(result[5]), int(result[6]), int(result[7]),
                           int(result[8]),int(result[9]),int(result[10]),
                           int(result[11]), int(result[12]), int(result[13]), int(result[14]), int(result[15]),
                           int(result[16]), int(result[17]), int(result[18]),
                           int(result[19]), int(result[20]), int(result[21]),
                           int(result[22]), int(result[23]), int(result[24]), int(result[25]), int(result[26]),
                           int(result[27]), int(result[28]), int(result[29]),
                           int(result[30]), int(result[31]), int(result[32]),
                           int(result[33]), int(result[34]), int(result[35]), int(result[36]), int(result[37]),
                           int(result[38]), int(result[39]), int(result[40]),
                           int(result[41]), int(result[42]), int(result[43]),int(result[44]), int(result[45]),
                           int(result[46]), int(result[47]), int(result[48]),
                           int(result[49]), int(result[50]), int(result[51]),
                           int(result[52]),int(result[53]),int(result[54]),
                           int(result[55]), int(result[56]), int(result[57]), int(result[58]), int(result[59]),
                           int(result[60]), int(result[61]), int(result[62]),
                           int(result[63]), int(result[64]), int(result[65]),
                           int(result[66]), int(result[67]), int(result[68]), int(result[69]), int(result[70]),
                           int(result[71]), int(result[72]), int(result[73]),
                           int(result[74]), int(result[75]), int(result[76]),
                           int(result[77]), int(result[78]), int(result[79]), int(result[80]), int(result[81]),
                           int(result[82]), int(result[83]), int(result[84]),
                           int(result[85]), int(result[86]), int(result[87]),
                           int(result[88]), int(result[89]), int(result[90]),
                           int(result[91]), int(result[92]), int(result[93]),
                           int(result[94]), int(result[95]), int(result[96]),
                           int(result[97]), int(result[98]),strInfo))
        print resultdata

class Age_Education_F():
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
                        i[10],i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19],
                        i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28], i[29],
                        i[30], i[31], i[32], i[33], i[34], i[35], i[36], i[37], i[38], i[39],
                        i[40], i[41], i[42], i[43], i[44], i[45], i[46], i[47], i[48], i[49],
                        i[50], i[51], i[52], i[53], i[54], i[55], i[56], i[57], i[58], i[59],
                        i[60], i[61], i[62], i[63], i[64], i[65], i[66], i[67], i[68], i[69],
                        i[70], i[71], i[72], i[73], i[74], i[75], i[76], i[77], i[78], i[79],
                        i[80], i[81], i[82], i[83], i[84], i[85], i[86], i[87], i[88], i[89],
                        i[90], i[91], i[92], i[93], i[94], i[95], i[96], i[97], i[98], i[99],
                        i[100]
                        )
                # print args
                cursor.callproc('p_age_edu_county_f', args)
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
        F_A15A19_E1314_CNT = row['F_A15A19_E1314_CNT']
        F_A15A19_E1112_CNT = row['F_A15A19_E1112_CNT']
        F_A15A19_E2122_CNT = row['F_A15A19_E2122_CNT']
        F_A15A19_E3_4_5_CNT = row['F_A15A19_E3_4_5_CNT']
        F_A15A19_E6_7_CNT = row['F_A15A19_E6_7_CNT']
        F_A15A19_E8_9_CNT = row['F_A15A19_E8_9_CNT']
        F_A15A19_E1_2_CNT = row['F_A15A19_E1_2_CNT']
        F_A15A19_E03_CNT = row['F_A15A19_E03_CNT']
        F_A15A19_E04_CNT = row['F_A15A19_E04_CNT']
        F_A20A24_E1314_CNT = row['F_A20A24_E1314_CNT']
        F_A20A24_E1112_CNT = row['F_A20A24_E1112_CNT']
        F_A20A24_E2122_CNT = row['F_A20A24_E2122_CNT']
        F_A20A24_E3_4_5_CNT = row['F_A20A24_E3_4_5_CNT']
        F_A20A24_E6_7_CNT = row['F_A20A24_E6_7_CNT']
        F_A20A24_E8_9_CNT = row['F_A20A24_E8_9_CNT']
        F_A20A24_E1_2_CNT = row['F_A20A24_E1_2_CNT']
        F_A20A24_E03_CNT = row['F_A20A24_E03_CNT']
        F_A20A24_E04_CNT = row['F_A20A24_E04_CNT']
        F_A25A29_E1314_CNT = row['F_A25A29_E1314_CNT']
        F_A25A29_E1112_CNT = row['F_A25A29_E1112_CNT']
        F_A25A29_E2122_CNT = row['F_A25A29_E2122_CNT']
        F_A25A29_E3_4_5_CNT = row['F_A25A29_E3_4_5_CNT']
        F_A25A29_E6_7_CNT = row['F_A25A29_E6_7_CNT']
        F_A25A29_E8_9_CNT = row['F_A25A29_E8_9_CNT']
        F_A25A29_E1_2_CNT = row['F_A25A29_E1_2_CNT']
        F_A25A29_E03_CNT = row['F_A25A29_E03_CNT']
        F_A25A29_E04_CNT = row['F_A25A29_E04_CNT']
        F_A30A34_E1314_CNT = row['F_A30A34_E1314_CNT']
        F_A30A34_E1112_CNT = row['F_A30A34_E1112_CNT']
        F_A30A34_E2122_CNT = row['F_A30A34_E2122_CNT']
        F_A30A34_E3_4_5_CNT = row['F_A30A34_E3_4_5_CNT']
        F_A30A34_E6_7_CNT = row['F_A30A34_E6_7_CNT']
        F_A30A34_E8_9_CNT = row['F_A30A34_E8_9_CNT']
        F_A30A34_E1_2_CNT = row['F_A30A34_E1_2_CNT']
        F_A30A34_E03_CNT = row['F_A30A34_E03_CNT']
        F_A30A34_E04_CNT = row['F_A30A34_E04_CNT']
        F_A35A39_E1314_CNT = row['F_A35A39_E1314_CNT']
        F_A35A39_E1112_CNT = row['F_A35A39_E1112_CNT']
        F_A35A39_E2122_CNT = row['F_A35A39_E2122_CNT']
        F_A35A39_E3_4_5_CNT = row['F_A35A39_E3_4_5_CNT']
        F_A35A39_E6_7_CNT = row['F_A35A39_E6_7_CNT']
        F_A35A39_E8_9_CNT = row['F_A35A39_E8_9_CNT']
        F_A35A39_E1_2_CNT = row['F_A35A39_E1_2_CNT']
        F_A35A39_E03_CNT = row['F_A35A39_E03_CNT']
        F_A35A39_E04_CNT = row['F_A35A39_E04_CNT']
        F_A40A44_E1314_CNT = row['F_A40A44_E1314_CNT']
        F_A40A44_E1112_CNT = row['F_A40A44_E1112_CNT']
        F_A40A44_E2122_CNT = row['F_A40A44_E2122_CNT']
        F_A40A44_E3_4_5_CNT = row['F_A40A44_E3_4_5_CNT']
        F_A40A44_E6_7_CNT = row['F_A40A44_E6_7_CNT']
        F_A40A44_E8_9_CNT = row['F_A40A44_E8_9_CNT']
        F_A40A44_E1_2_CNT = row['F_A40A44_E1_2_CNT']
        F_A40A44_E03_CNT = row['F_A40A44_E03_CNT']
        F_A40A44_E04_CNT = row['F_A40A44_E04_CNT']
        F_A45A49_E1314_CNT = row['F_A45A49_E1314_CNT']
        F_A45A49_E1112_CNT = row['F_A45A49_E1112_CNT']
        F_A45A49_E2122_CNT = row['F_A45A49_E2122_CNT']
        F_A45A49_E3_4_5_CNT = row['F_A45A49_E3_4_5_CNT']
        F_A45A49_E6_7_CNT = row['F_A45A49_E6_7_CNT']
        F_A45A49_E8_9_CNT = row['F_A45A49_E8_9_CNT']
        F_A45A49_E1_2_CNT = row['F_A45A49_E1_2_CNT']
        F_A45A49_E03_CNT = row['F_A45A49_E03_CNT']
        F_A45A49_E04_CNT = row['F_A45A49_E04_CNT']
        F_A50A54_E1314_CNT = row['F_A50A54_E1314_CNT']
        F_A50A54_E1112_CNT = row['F_A50A54_E1112_CNT']
        F_A50A54_E2122_CNT = row['F_A50A54_E2122_CNT']
        F_A50A54_E3_4_5_CNT = row['F_A50A54_E3_4_5_CNT']
        F_A50A54_E6_7_CNT = row['F_A50A54_E6_7_CNT']
        F_A50A54_E8_9_CNT = row['F_A50A54_E8_9_CNT']
        F_A50A54_E1_2_CNT = row['F_A50A54_E1_2_CNT']
        F_A50A54_E03_CNT = row['F_A50A54_E03_CNT']
        F_A50A54_E04_CNT = row['F_A50A54_E04_CNT']
        F_A55A59_E1314_CNT = row['F_A55A59_E1314_CNT']
        F_A55A59_E1112_CNT = row['F_A55A59_E1112_CNT']
        F_A55A59_E2122_CNT = row['F_A55A59_E2122_CNT']
        F_A55A59_E3_4_5_CNT = row['F_A55A59_E3_4_5_CNT']
        F_A55A59_E6_7_CNT = row['F_A55A59_E6_7_CNT']
        F_A55A59_E8_9_CNT = row['F_A55A59_E8_9_CNT']
        F_A55A59_E1_2_CNT = row['F_A55A59_E1_2_CNT']
        F_A55A59_E03_CNT = row['F_A55A59_E03_CNT']
        F_A55A59_E04_CNT = row['F_A55A59_E04_CNT']
        F_A60A64_E1314_CNT = row['F_A60A64_E1314_CNT']
        F_A60A64_E1112_CNT = row['F_A60A64_E1112_CNT']
        F_A60A64_E2122_CNT = row['F_A60A64_E2122_CNT']
        F_A60A64_E3_4_5_CNT = row['F_A60A64_E3_4_5_CNT']
        F_A60A64_E6_7_CNT = row['F_A60A64_E6_7_CNT']
        F_A60A64_E8_9_CNT = row['F_A60A64_E8_9_CNT']
        F_A60A64_E1_2_CNT = row['F_A60A64_E1_2_CNT']
        F_A60A64_E03_CNT = row['F_A60A64_E03_CNT']
        F_A60A64_E04_CNT = row['F_A60A64_E04_CNT']
        F_A65UP_E1314_CNT = row['F_A65UP_E1314_CNT']
        F_A65UP_E1112_CNT = row['F_A65UP_E1112_CNT']
        F_A65UP_E2122_CNT = row['F_A65UP_E2122_CNT']
        F_A65UP_E3_4_5_CNT = row['F_A65UP_E3_4_5_CNT']
        F_A65UP_E6_7_CNT = row['F_A65UP_E6_7_CNT']
        F_A65UP_E8_9_CNT = row['F_A65UP_E8_9_CNT']
        F_A65UP_E1_2_CNT = row['F_A65UP_E1_2_CNT']
        F_A65UP_E03_CNT = row['F_A65UP_E03_CNT']
        F_A65UP_E04_CNT = row['F_A65UP_E04_CNT']

        data.append((county,F_A15A19_E1314_CNT,
        F_A15A19_E1112_CNT, F_A15A19_E2122_CNT, F_A15A19_E3_4_5_CNT,F_A15A19_E6_7_CNT, F_A15A19_E8_9_CNT,
        F_A15A19_E1_2_CNT, F_A15A19_E03_CNT, F_A15A19_E04_CNT,F_A20A24_E1314_CNT, F_A20A24_E1112_CNT,
        F_A20A24_E2122_CNT, F_A20A24_E3_4_5_CNT, F_A20A24_E6_7_CNT, F_A20A24_E8_9_CNT, F_A20A24_E1_2_CNT, F_A20A24_E03_CNT, F_A20A24_E04_CNT,
        F_A25A29_E1314_CNT, F_A25A29_E1112_CNT,
        F_A25A29_E2122_CNT, F_A25A29_E3_4_5_CNT, F_A25A29_E6_7_CNT, F_A25A29_E8_9_CNT, F_A25A29_E1_2_CNT, F_A25A29_E03_CNT,
        F_A25A29_E04_CNT, F_A30A34_E1314_CNT, F_A30A34_E1112_CNT, F_A30A34_E2122_CNT, F_A30A34_E3_4_5_CNT, F_A30A34_E6_7_CNT, F_A30A34_E8_9_CNT,
        F_A30A34_E1_2_CNT, F_A30A34_E03_CNT, F_A30A34_E04_CNT, F_A35A39_E1314_CNT,
        F_A35A39_E1112_CNT, F_A35A39_E2122_CNT, F_A35A39_E3_4_5_CNT, F_A35A39_E6_7_CNT, F_A35A39_E8_9_CNT,
        F_A35A39_E1_2_CNT, F_A35A39_E03_CNT, F_A35A39_E04_CNT, F_A40A44_E1314_CNT, F_A40A44_E1112_CNT,
        F_A40A44_E2122_CNT, F_A40A44_E3_4_5_CNT, F_A40A44_E6_7_CNT, F_A40A44_E8_9_CNT, F_A40A44_E1_2_CNT, F_A40A44_E03_CNT,
        F_A40A44_E04_CNT, F_A45A49_E1314_CNT, F_A45A49_E1112_CNT, F_A45A49_E2122_CNT, F_A45A49_E3_4_5_CNT,
        F_A45A49_E6_7_CNT, F_A45A49_E8_9_CNT, F_A45A49_E1_2_CNT, F_A45A49_E03_CNT, F_A45A49_E04_CNT,
        F_A50A54_E1314_CNT, F_A50A54_E1112_CNT, F_A50A54_E2122_CNT, F_A50A54_E3_4_5_CNT, F_A50A54_E6_7_CNT, F_A50A54_E8_9_CNT, F_A50A54_E1_2_CNT,
        F_A50A54_E03_CNT, F_A50A54_E04_CNT, F_A55A59_E1314_CNT, F_A55A59_E1112_CNT, F_A55A59_E2122_CNT,
        F_A55A59_E3_4_5_CNT, F_A55A59_E6_7_CNT, F_A55A59_E8_9_CNT, F_A55A59_E1_2_CNT, F_A55A59_E03_CNT, F_A55A59_E04_CNT,
        F_A60A64_E1314_CNT,F_A60A64_E1112_CNT, F_A60A64_E2122_CNT, F_A60A64_E3_4_5_CNT, F_A60A64_E6_7_CNT,
        F_A60A64_E8_9_CNT, F_A60A64_E1_2_CNT, F_A60A64_E03_CNT, F_A60A64_E04_CNT, F_A65UP_E1314_CNT,
        F_A65UP_E1112_CNT, F_A65UP_E2122_CNT, F_A65UP_E3_4_5_CNT, F_A65UP_E6_7_CNT, F_A65UP_E8_9_CNT, F_A65UP_E1_2_CNT,
        F_A65UP_E03_CNT, F_A65UP_E04_CNT, INFO_TIME))

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
                strInfo = row[100]
                if i > 0 and i < 100:
                    # print row[i]
                    arr.append(row[i])
            mydata.append(arr)

        mydata2 = numpy.array(mydata)
        result = mydata2.sum(axis=0)
        resultdata.append((strCountID, int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4]),
                           int(result[5]), int(result[6]), int(result[7]),
                           int(result[8]),int(result[9]),int(result[10]),
                           int(result[11]), int(result[12]), int(result[13]), int(result[14]), int(result[15]),
                           int(result[16]), int(result[17]), int(result[18]),
                           int(result[19]), int(result[20]), int(result[21]),
                           int(result[22]), int(result[23]), int(result[24]), int(result[25]), int(result[26]),
                           int(result[27]), int(result[28]), int(result[29]),
                           int(result[30]), int(result[31]), int(result[32]),
                           int(result[33]), int(result[34]), int(result[35]), int(result[36]), int(result[37]),
                           int(result[38]), int(result[39]), int(result[40]),
                           int(result[41]), int(result[42]), int(result[43]),int(result[44]), int(result[45]),
                           int(result[46]), int(result[47]), int(result[48]),
                           int(result[49]), int(result[50]), int(result[51]),
                           int(result[52]),int(result[53]),int(result[54]),
                           int(result[55]), int(result[56]), int(result[57]), int(result[58]), int(result[59]),
                           int(result[60]), int(result[61]), int(result[62]),
                           int(result[63]), int(result[64]), int(result[65]),
                           int(result[66]), int(result[67]), int(result[68]), int(result[69]), int(result[70]),
                           int(result[71]), int(result[72]), int(result[73]),
                           int(result[74]), int(result[75]), int(result[76]),
                           int(result[77]), int(result[78]), int(result[79]), int(result[80]), int(result[81]),
                           int(result[82]), int(result[83]), int(result[84]),
                           int(result[85]), int(result[86]), int(result[87]),
                           int(result[88]), int(result[89]), int(result[90]),
                           int(result[91]), int(result[92]), int(result[93]),
                           int(result[94]), int(result[95]), int(result[96]),
                           int(result[97]), int(result[98]),strInfo))
        print resultdata

class Age_Education_All():
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
                        i[10],i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19],
                        i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28], i[29],
                        i[30], i[31], i[32], i[33], i[34], i[35], i[36], i[37], i[38], i[39],
                        i[40], i[41], i[42], i[43], i[44], i[45], i[46], i[47], i[48], i[49],
                        i[50], i[51], i[52], i[53], i[54], i[55], i[56], i[57], i[58], i[59],
                        i[60], i[61], i[62], i[63], i[64], i[65], i[66], i[67], i[68], i[69],
                        i[70], i[71], i[72], i[73], i[74], i[75], i[76], i[77], i[78], i[79],
                        i[80], i[81], i[82], i[83], i[84], i[85], i[86], i[87], i[88], i[89],
                        i[90], i[91], i[92], i[93], i[94], i[95], i[96], i[97], i[98], i[99],
                        i[100]
                        )
                # print args
                cursor.callproc('p_age_edu_county_all', args)
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
        _A15A19_E1314_CNT = int(row['M_A15A19_E1314_CNT'])+int(row['F_A15A19_E1314_CNT'])
        _A15A19_E1112_CNT = int(row['M_A15A19_E1112_CNT'])+int(row['F_A15A19_E1112_CNT'])
        _A15A19_E2122_CNT = int(row['M_A15A19_E2122_CNT'])+int(row['F_A15A19_E2122_CNT'])
        _A15A19_E3_4_5_CNT = int(row['M_A15A19_E3_4_5_CNT'])+int(row['F_A15A19_E3_4_5_CNT'])
        _A15A19_E6_7_CNT = int(row['M_A15A19_E6_7_CNT'])+int(row['F_A15A19_E6_7_CNT'])
        _A15A19_E8_9_CNT = int(row['M_A15A19_E8_9_CNT'])+int(row['F_A15A19_E8_9_CNT'])
        _A15A19_E1_2_CNT = int(row['M_A15A19_E1_2_CNT'])+int(row['F_A15A19_E1_2_CNT'])
        _A15A19_E03_CNT = int(row['M_A15A19_E03_CNT'])+int(row['F_A15A19_E03_CNT'])
        _A15A19_E04_CNT = int(row['M_A15A19_E04_CNT'])+int(row['F_A15A19_E04_CNT'])
        _A20A24_E1314_CNT = int(row['M_A20A24_E1314_CNT'])+int(row['F_A20A24_E1314_CNT'])
        _A20A24_E1112_CNT = int(row['M_A20A24_E1112_CNT'])+int(row['F_A20A24_E1112_CNT'])
        _A20A24_E2122_CNT = int(row['M_A20A24_E2122_CNT'])+int(row['F_A20A24_E2122_CNT'])
        _A20A24_E3_4_5_CNT = int(row['M_A20A24_E3_4_5_CNT'])+int(row['F_A20A24_E3_4_5_CNT'])
        _A20A24_E6_7_CNT = int(row['M_A20A24_E6_7_CNT'])+int(row['F_A20A24_E6_7_CNT'])
        _A20A24_E8_9_CNT = int(row['M_A20A24_E8_9_CNT'])+int(row['F_A20A24_E8_9_CNT'])
        _A20A24_E1_2_CNT = int(row['M_A20A24_E1_2_CNT'])+ int(row['F_A20A24_E1_2_CNT'])
        _A20A24_E03_CNT = int(row['M_A20A24_E03_CNT'])+int(row['F_A20A24_E03_CNT'])
        _A20A24_E04_CNT = int(row['M_A20A24_E04_CNT'])+int(row['F_A20A24_E04_CNT'])
        _A25A29_E1314_CNT = int(row['M_A25A29_E1314_CNT'])+int(row['F_A25A29_E1314_CNT'])
        _A25A29_E1112_CNT = int(row['M_A25A29_E1112_CNT'])+int(row['F_A25A29_E1112_CNT'])
        _A25A29_E2122_CNT = int(row['M_A25A29_E2122_CNT'])+int(row['F_A25A29_E2122_CNT'])
        _A25A29_E3_4_5_CNT = int(row['M_A25A29_E3_4_5_CNT'])+int(row['F_A25A29_E3_4_5_CNT'])
        _A25A29_E6_7_CNT = int(row['M_A25A29_E6_7_CNT'])+int(row['F_A25A29_E6_7_CNT'])
        _A25A29_E8_9_CNT = int(row['M_A25A29_E8_9_CNT'])+int(row['F_A25A29_E8_9_CNT'])
        _A25A29_E1_2_CNT = int(row['M_A25A29_E1_2_CNT'])+int(row['F_A25A29_E1_2_CNT'])
        _A25A29_E03_CNT = int(row['M_A25A29_E03_CNT'])+int(row['F_A25A29_E03_CNT'])
        _A25A29_E04_CNT = int(row['M_A25A29_E04_CNT'])+int(row['F_A25A29_E04_CNT'])
        _A30A34_E1314_CNT = int(row['M_A30A34_E1314_CNT'])+int(row['F_A30A34_E1314_CNT'])
        _A30A34_E1112_CNT = int(row['M_A30A34_E1112_CNT'])+int(row['F_A30A34_E1112_CNT'])
        _A30A34_E2122_CNT = int(row['M_A30A34_E2122_CNT'])+int(row['F_A30A34_E2122_CNT'])
        _A30A34_E3_4_5_CNT = int(row['M_A30A34_E3_4_5_CNT'])+int(row['F_A30A34_E3_4_5_CNT'])
        _A30A34_E6_7_CNT = int(row['M_A30A34_E6_7_CNT'])+int(row['F_A30A34_E6_7_CNT'])
        _A30A34_E8_9_CNT = int(row['M_A30A34_E8_9_CNT'])+int(row['F_A30A34_E8_9_CNT'])
        _A30A34_E1_2_CNT = int(row['M_A30A34_E1_2_CNT'])+int(row['F_A30A34_E1_2_CNT'])
        _A30A34_E03_CNT = int(row['M_A30A34_E03_CNT'])+int(row['F_A30A34_E03_CNT'])
        _A30A34_E04_CNT = int(row['M_A30A34_E04_CNT'])+int(row['F_A30A34_E04_CNT'])
        _A35A39_E1314_CNT = int(row['M_A35A39_E1314_CNT'])+int(row['F_A35A39_E1314_CNT'])
        _A35A39_E1112_CNT = int(row['M_A35A39_E1112_CNT'])+int(row['F_A35A39_E1112_CNT'])
        _A35A39_E2122_CNT = int(row['M_A35A39_E2122_CNT'])+int(row['F_A35A39_E2122_CNT'])
        _A35A39_E3_4_5_CNT = int(row['M_A35A39_E3_4_5_CNT'])+int(row['F_A35A39_E3_4_5_CNT'])
        _A35A39_E6_7_CNT = int(row['M_A35A39_E6_7_CNT'])+int(row['F_A35A39_E6_7_CNT'])
        _A35A39_E8_9_CNT = int(row['M_A35A39_E8_9_CNT'])+int(row['F_A35A39_E8_9_CNT'])
        _A35A39_E1_2_CNT = int(row['M_A35A39_E1_2_CNT'])+int(row['F_A35A39_E1_2_CNT'])
        _A35A39_E03_CNT = int(row['M_A35A39_E03_CNT'])+int(row['F_A35A39_E03_CNT'])
        _A35A39_E04_CNT = int(row['M_A35A39_E04_CNT'])+int(row['F_A35A39_E04_CNT'])
        _A40A44_E1314_CNT = int(row['M_A40A44_E1314_CNT'])+int(row['F_A40A44_E1314_CNT'])
        _A40A44_E1112_CNT = int(row['M_A40A44_E1112_CNT'])+int(row['F_A40A44_E1112_CNT'])
        _A40A44_E2122_CNT = int(row['M_A40A44_E2122_CNT'])+int(row['F_A40A44_E2122_CNT'])
        _A40A44_E3_4_5_CNT = int(row['M_A40A44_E3_4_5_CNT'])+int(row['F_A40A44_E3_4_5_CNT'])
        _A40A44_E6_7_CNT = int(row['M_A40A44_E6_7_CNT'])+int(row['F_A40A44_E6_7_CNT'])
        _A40A44_E8_9_CNT = int(row['M_A40A44_E8_9_CNT'])+int(row['F_A40A44_E8_9_CNT'])
        _A40A44_E1_2_CNT = int(row['M_A40A44_E1_2_CNT'])+int(row['F_A40A44_E1_2_CNT'])
        _A40A44_E03_CNT = int(row['M_A40A44_E03_CNT'])+int(row['F_A40A44_E03_CNT'])
        _A40A44_E04_CNT = int(row['M_A40A44_E04_CNT'])+int(row['F_A40A44_E04_CNT'])
        _A45A49_E1314_CNT = int(row['M_A45A49_E1314_CNT'])+int(row['F_A45A49_E1314_CNT'])
        _A45A49_E1112_CNT = int(row['M_A45A49_E1112_CNT'])+int(row['F_A45A49_E1112_CNT'])
        _A45A49_E2122_CNT = int(row['M_A45A49_E2122_CNT'])+int(row['F_A45A49_E2122_CNT'])
        _A45A49_E3_4_5_CNT = int(row['M_A45A49_E3_4_5_CNT'])+int(row['F_A45A49_E3_4_5_CNT'])
        _A45A49_E6_7_CNT = int(row['M_A45A49_E6_7_CNT'])+ int(row['F_A45A49_E6_7_CNT'])
        _A45A49_E8_9_CNT = int(row['M_A45A49_E8_9_CNT'])+int(row['F_A45A49_E8_9_CNT'])
        _A45A49_E1_2_CNT = int(row['M_A45A49_E1_2_CNT'])+int(row['F_A45A49_E1_2_CNT'])
        _A45A49_E03_CNT = int(row['M_A45A49_E03_CNT'])+int(row['F_A45A49_E03_CNT'])
        _A45A49_E04_CNT = int(row['M_A45A49_E04_CNT'])+int(row['F_A45A49_E04_CNT'])
        _A50A54_E1314_CNT = int(row['M_A50A54_E1314_CNT'])+int(row['F_A50A54_E1314_CNT'])
        _A50A54_E1112_CNT = int(row['M_A50A54_E1112_CNT'])+int(row['F_A50A54_E1112_CNT'])
        _A50A54_E2122_CNT = int(row['M_A50A54_E2122_CNT'])+int(row['F_A50A54_E2122_CNT'])
        _A50A54_E3_4_5_CNT = int(row['M_A50A54_E3_4_5_CNT'])+int(row['F_A50A54_E3_4_5_CNT'])
        _A50A54_E6_7_CNT = int(row['M_A50A54_E6_7_CNT'])+int(row['F_A50A54_E6_7_CNT'])
        _A50A54_E8_9_CNT = int(row['M_A50A54_E8_9_CNT'])+int(row['F_A50A54_E8_9_CNT'])
        _A50A54_E1_2_CNT = int(row['M_A50A54_E1_2_CNT'])+int(row['F_A50A54_E1_2_CNT'])
        _A50A54_E03_CNT = int(row['M_A50A54_E03_CNT'])+int(row['F_A50A54_E03_CNT'])
        _A50A54_E04_CNT = int(row['M_A50A54_E04_CNT'])+int(row['F_A50A54_E04_CNT'])
        _A55A59_E1314_CNT = int(row['M_A55A59_E1314_CNT'])+int(row['F_A55A59_E1314_CNT'])
        _A55A59_E1112_CNT = int(row['M_A55A59_E1112_CNT'])+int(row['F_A55A59_E1112_CNT'])
        _A55A59_E2122_CNT = int(row['M_A55A59_E2122_CNT'])+int(row['F_A55A59_E2122_CNT'])
        _A55A59_E3_4_5_CNT = int(row['M_A55A59_E3_4_5_CNT'])+int(row['F_A55A59_E3_4_5_CNT'])
        _A55A59_E6_7_CNT = int(row['M_A55A59_E6_7_CNT'])+int(row['F_A55A59_E6_7_CNT'])
        _A55A59_E8_9_CNT = int(row['M_A55A59_E8_9_CNT'])+int(row['F_A55A59_E8_9_CNT'])
        _A55A59_E1_2_CNT = int(row['M_A55A59_E1_2_CNT'])+int(row['F_A55A59_E1_2_CNT'])
        _A55A59_E03_CNT = int(row['M_A55A59_E03_CNT'])+int(row['F_A55A59_E03_CNT'])
        _A55A59_E04_CNT = int(row['M_A55A59_E04_CNT'])+int(row['F_A55A59_E04_CNT'])
        _A60A64_E1314_CNT = int(row['M_A60A64_E1314_CNT'])+int(row['F_A60A64_E1314_CNT'])
        _A60A64_E1112_CNT = int(row['M_A60A64_E1112_CNT'])+int(row['F_A60A64_E1112_CNT'])
        _A60A64_E2122_CNT = int(row['M_A60A64_E2122_CNT'])+int(row['F_A60A64_E2122_CNT'])
        _A60A64_E3_4_5_CNT = int(row['M_A60A64_E3_4_5_CNT'])+int(row['F_A60A64_E3_4_5_CNT'])
        _A60A64_E6_7_CNT = int(row['M_A60A64_E6_7_CNT'])+int(row['F_A60A64_E6_7_CNT'])
        _A60A64_E8_9_CNT = int(row['M_A60A64_E8_9_CNT'])+ int(row['F_A60A64_E8_9_CNT'])
        _A60A64_E1_2_CNT = int(row['M_A60A64_E1_2_CNT'])+int(row['F_A60A64_E1_2_CNT'])
        _A60A64_E03_CNT = int(row['M_A60A64_E03_CNT'])+int(row['F_A60A64_E03_CNT'])
        _A60A64_E04_CNT = int(row['M_A60A64_E04_CNT'])+int(row['F_A60A64_E04_CNT'])
        _A65UP_E1314_CNT = int(row['M_A65UP_E1314_CNT'])+int(row['F_A65UP_E1314_CNT'])
        _A65UP_E1112_CNT = int(row['M_A65UP_E1112_CNT'])+int(row['F_A65UP_E1112_CNT'])
        _A65UP_E2122_CNT = int(row['M_A65UP_E2122_CNT'])+int(row['F_A65UP_E2122_CNT'])
        _A65UP_E3_4_5_CNT = int(row['M_A65UP_E3_4_5_CNT'])+int(row['F_A65UP_E3_4_5_CNT'])
        _A65UP_E6_7_CNT = int(row['M_A65UP_E6_7_CNT'])+int(row['F_A65UP_E6_7_CNT'])
        _A65UP_E8_9_CNT = int(row['M_A65UP_E8_9_CNT'])+int(row['F_A65UP_E8_9_CNT'])
        _A65UP_E1_2_CNT = int(row['M_A65UP_E1_2_CNT'])+int(row['F_A65UP_E1_2_CNT'])
        _A65UP_E03_CNT = int(row['M_A65UP_E03_CNT'])+int(row['F_A65UP_E03_CNT'])
        _A65UP_E04_CNT = int(row['M_A65UP_E04_CNT'])+int(row['F_A65UP_E04_CNT'])

        data.append((county,_A15A19_E1314_CNT,_A15A19_E1112_CNT,_A15A19_E2122_CNT,_A15A19_E3_4_5_CNT,
                _A15A19_E6_7_CNT,_A15A19_E8_9_CNT,_A15A19_E1_2_CNT,_A15A19_E03_CNT,_A15A19_E04_CNT,
                _A20A24_E1314_CNT,_A20A24_E1112_CNT,_A20A24_E2122_CNT,_A20A24_E3_4_5_CNT,
                _A20A24_E6_7_CNT,_A20A24_E8_9_CNT,_A20A24_E1_2_CNT,_A20A24_E03_CNT,_A20A24_E04_CNT,
                _A25A29_E1314_CNT,_A25A29_E1112_CNT,_A25A29_E2122_CNT,_A25A29_E3_4_5_CNT,
                _A25A29_E6_7_CNT,_A25A29_E8_9_CNT,_A25A29_E1_2_CNT,_A25A29_E03_CNT,_A25A29_E04_CNT,
                _A30A34_E1314_CNT,_A30A34_E1112_CNT,_A30A34_E2122_CNT,_A30A34_E3_4_5_CNT,_A30A34_E6_7_CNT,
                _A30A34_E8_9_CNT,_A30A34_E1_2_CNT,_A30A34_E03_CNT,_A30A34_E04_CNT,_A35A39_E1314_CNT,
                _A35A39_E1112_CNT,_A35A39_E2122_CNT,_A35A39_E3_4_5_CNT,_A35A39_E6_7_CNT,_A35A39_E8_9_CNT,
                _A35A39_E1_2_CNT,_A35A39_E03_CNT,_A35A39_E04_CNT,_A40A44_E1314_CNT,_A40A44_E1112_CNT,
                _A40A44_E2122_CNT,_A40A44_E3_4_5_CNT,_A40A44_E6_7_CNT,_A40A44_E8_9_CNT,_A40A44_E1_2_CNT,
                _A40A44_E03_CNT,_A40A44_E04_CNT,_A45A49_E1314_CNT,_A45A49_E1112_CNT,_A45A49_E2122_CNT,
                _A45A49_E3_4_5_CNT,_A45A49_E6_7_CNT,_A45A49_E8_9_CNT,_A45A49_E1_2_CNT,_A45A49_E03_CNT,_A45A49_E04_CNT,
                _A50A54_E1314_CNT,_A50A54_E1112_CNT,_A50A54_E2122_CNT,_A50A54_E3_4_5_CNT,_A50A54_E6_7_CNT,
                _A50A54_E8_9_CNT,_A50A54_E1_2_CNT,_A50A54_E03_CNT,_A50A54_E04_CNT,_A55A59_E1314_CNT,
                _A55A59_E1112_CNT,_A55A59_E2122_CNT,_A55A59_E3_4_5_CNT,_A55A59_E6_7_CNT,_A55A59_E8_9_CNT,_A55A59_E1_2_CNT,
                _A55A59_E03_CNT,_A55A59_E04_CNT,_A60A64_E1314_CNT,_A60A64_E1112_CNT,_A60A64_E2122_CNT,
                _A60A64_E3_4_5_CNT,_A60A64_E6_7_CNT,_A60A64_E8_9_CNT,_A60A64_E1_2_CNT,_A60A64_E03_CNT,_A60A64_E04_CNT,
                _A65UP_E1314_CNT,_A65UP_E1112_CNT,_A65UP_E2122_CNT,_A65UP_E3_4_5_CNT,_A65UP_E6_7_CNT,
                _A65UP_E8_9_CNT,_A65UP_E1_2_CNT,_A65UP_E03_CNT,_A65UP_E04_CNT,INFO_TIME))

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
                strInfo = row[100]
                if i > 0 and i < 100:
                    # print row[i]
                    arr.append(row[i])
            mydata.append(arr)

        mydata2 = numpy.array(mydata)
        result = mydata2.sum(axis=0)
        resultdata.append((strCountID, int(result[0]), int(result[1]), int(result[2]), int(result[3]), int(result[4]),
                           int(result[5]), int(result[6]), int(result[7]),
                           int(result[8]),int(result[9]),int(result[10]),
                           int(result[11]), int(result[12]), int(result[13]), int(result[14]), int(result[15]),
                           int(result[16]), int(result[17]), int(result[18]),
                           int(result[19]), int(result[20]), int(result[21]),
                           int(result[22]), int(result[23]), int(result[24]), int(result[25]), int(result[26]),
                           int(result[27]), int(result[28]), int(result[29]),
                           int(result[30]), int(result[31]), int(result[32]),
                           int(result[33]), int(result[34]), int(result[35]), int(result[36]), int(result[37]),
                           int(result[38]), int(result[39]), int(result[40]),
                           int(result[41]), int(result[42]), int(result[43]),int(result[44]), int(result[45]),
                           int(result[46]), int(result[47]), int(result[48]),
                           int(result[49]), int(result[50]), int(result[51]),
                           int(result[52]),int(result[53]),int(result[54]),
                           int(result[55]), int(result[56]), int(result[57]), int(result[58]), int(result[59]),
                           int(result[60]), int(result[61]), int(result[62]),
                           int(result[63]), int(result[64]), int(result[65]),
                           int(result[66]), int(result[67]), int(result[68]), int(result[69]), int(result[70]),
                           int(result[71]), int(result[72]), int(result[73]),
                           int(result[74]), int(result[75]), int(result[76]),
                           int(result[77]), int(result[78]), int(result[79]), int(result[80]), int(result[81]),
                           int(result[82]), int(result[83]), int(result[84]),
                           int(result[85]), int(result[86]), int(result[87]),
                           int(result[88]), int(result[89]), int(result[90]),
                           int(result[91]), int(result[92]), int(result[93]),
                           int(result[94]), int(result[95]), int(result[96]),
                           int(result[97]), int(result[98]),strInfo))
        print resultdata


if __name__ == '__main__':
    mssql = Age_Education_All()
    print mssql.ParserJson(url='http://segisws.moi.gov.tw/STATWSSTData/OpenService.asmx/GetStatSTDataForOpenCode?oCode=6E03CA29B955A854D8F52522E38D8C7051A1FBEE829C41DB24A8D456DDA4E3BA5AF51EE58102DB3A0956DEC9A8D69E14C93C1F4155955501')
