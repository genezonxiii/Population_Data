# -*-  coding: utf-8  -*-
__author__ = '10409003'
import json
import urllib
import csv
import mysql.connector
from setting import Config_2
import logging, time

logger = logging.getLogger(__name__)


class Population_village():
    def ParserJson(self, url):
        try:
            logging.basicConfig(filename='/data/Population_Data/pyupload.log',
                                level=logging.DEBUG,
                                format='%(asctime)s - %(levelname)s - %(filename)s:%(name)s:%(module)s/%(funcName)s/%(lineno)d - %(message)s',
                                datefmt='%Y/%m/%d %I:%M:%S %p')
            logging.Formatter.converter = time.gmtime

            result = json.load(urllib.urlopen(url))
            data = []
            for each in result['RowDataList']:
                self.CombindData(each, data)
            self.writeDB(data)
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
            db = mysql.connector.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd,
                                         database=config.dbName)
            db.set_charset_collation('utf8')
            cursor = db.cursor()
            for i in data:
                args = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],
                        i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19],
                        i[20], i[21], i[22], i[23], i[24], i[25], i[26], i[27], i[28], i[29],
                        i[30], i[31], i[32], i[33], i[34], i[35], i[36], i[37], i[38], i[39],
                        i[40], i[41], i[42], i[43], i[44], i[45], i[46], i[47], i[48], i[49],
                        i[50], i[51], i[52], i[53], i[54], i[55], i[56], i[57], i[58], i[59],
                        i[60], i[61], i[62], i[63], i[64], i[65], i[66], i[67], i[68], i[69])
                logger.debug(args)
                cursor.callproc('p_population_village', args)
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

    def CombindData(self, row, data):
        try:
            INFO_TIME = row['INFO_TIME'][0:3]
            COUNTY_ID = row['COUNTY_ID']
            COUNTY = row['COUNTY']
            TOWN_ID = row['TOWN_ID']
            TOWN = row['TOWN']
            V_ID = row['V_ID']
            VILLAGE = row['VILLAGE']

            A0A4_CNT = row['A0A4_CNT']
            A0A4_M_CNT = row['A0A4_M_CNT']
            A0A4_F_CNT = row['A0A4_F_CNT']
            A5A9_CNT = row['A5A9_CNT']
            A5A9_M_CNT = row['A5A9_M_CNT']
            A5A9_F_CNT = row['A5A9_F_CNT']

            A10A14_CNT = row['A10A14_CNT']
            A10A14_M_CNT = row['A10A14_M_CNT']
            A10A14_F_CNT = row['A10A14_F_CNT']

            A15A19_CNT = row['A15A19_CNT']
            A15A19_M_CNT = row['A15A19_M_CNT']
            A15A19_F_CNT = row['A15A19_F_CNT']

            A20A24_CNT = row['A20A24_CNT']
            A20A24_M_CNT = row['A20A24_M_CNT']
            A20A24_F_CNT = row['A20A24_F_CNT']

            A25A29_CNT = row['A25A29_CNT']
            A25A29_M_CNT = row['A25A29_M_CNT']
            A25A29_F_CNT = row['A25A29_F_CNT']

            A30A34_CNT = row['A30A34_CNT']
            A30A34_M_CNT = row['A30A34_M_CNT']
            A30A34_F_CNT = row['A30A34_F_CNT']

            A35A39_CNT = row['A35A39_CNT']
            A35A39_M_CNT = row['A35A39_M_CNT']
            A35A39_F_CNT = row['A35A39_F_CNT']

            A40A44_CNT = row['A40A44_CNT']
            A40A44_M_CNT = row['A40A44_M_CNT']
            A40A44_F_CNT = row['A40A44_F_CNT']

            A45A49_CNT = row['A45A49_CNT']
            A45A49_M_CNT = row['A45A49_M_CNT']
            A45A49_F_CNT = row['A45A49_F_CNT']

            A50A54_CNT = row['A50A54_CNT']
            A50A54_M_CNT = row['A50A54_M_CNT']
            A50A54_F_CNT = row['A50A54_F_CNT']

            A55A59_CNT = row['A55A59_CNT']
            A55A59_M_CNT = row['A55A59_M_CNT']
            A55A59_F_CNT = row['A55A59_F_CNT']

            A60A64_CNT = row['A60A64_CNT']
            A60A64_M_CNT = row['A60A64_M_CNT']
            A60A64_F_CNT = row['A60A64_F_CNT']

            A65A69_CNT = row['A65A69_CNT']
            A65A69_M_CNT = row['A65A69_M_CNT']
            A65A69_F_CNT = row['A65A69_F_CNT']

            A70A74_CNT = row['A70A74_CNT']
            A70A74_M_CNT = row['A70A74_M_CNT']
            A70A74_F_CNT = row['A70A74_F_CNT']

            A75A79_CNT = row['A75A79_CNT']
            A75A79_M_CNT = row['A75A79_M_CNT']
            A75A79_F_CNT = row['A75A79_F_CNT']

            A80A84_CNT = row['A80A84_CNT']
            A80A84_M_CNT = row['A80A84_M_CNT']
            A80A84_F_CNT = row['A80A84_F_CNT']

            A85A89_CNT = row['A85A89_CNT']
            A85A89_M_CNT = row['A85A89_M_CNT']
            A85A89_F_CNT = row['A85A89_F_CNT']

            A90A94_CNT = row['A90A94_CNT']
            A90A94_M_CNT = row['A90A94_M_CNT']
            A90A94_F_CNT = row['A90A94_F_CNT']

            A95A99_CNT = row['A95A99_CNT']
            A95A99_M_CNT = row['A95A99_M_CNT']
            A95A99_F_CNT = row['A95A99_F_CNT']

            A100UP_5_CNT = row['A100UP_5_CNT']
            A100UP_5_M_CNT = row['A100UP_5_M_CNT']
            A100UP_5_F_CNT = row['A100UP_5_F_CNT']
            data.append((COUNTY_ID, COUNTY, TOWN_ID, TOWN, V_ID, VILLAGE, A0A4_CNT, A0A4_M_CNT, A0A4_F_CNT, A5A9_CNT, A5A9_M_CNT, \
                        A5A9_F_CNT, A10A14_CNT, A10A14_M_CNT, A10A14_F_CNT, A15A19_CNT, \
                        A15A19_M_CNT, A15A19_F_CNT, A20A24_CNT, A20A24_M_CNT, A20A24_F_CNT, \
                        A25A29_CNT, A25A29_M_CNT, A25A29_F_CNT, A30A34_CNT, A30A34_M_CNT, \
                        A30A34_F_CNT, A35A39_CNT, A35A39_M_CNT, A35A39_F_CNT, A40A44_CNT, \
                        A40A44_M_CNT, A40A44_F_CNT, A45A49_CNT, A45A49_M_CNT, A45A49_F_CNT, \
                        A50A54_CNT, A50A54_M_CNT, A50A54_F_CNT, A55A59_CNT, A55A59_M_CNT, \
                        A55A59_F_CNT, A60A64_CNT, A60A64_M_CNT, A60A64_F_CNT, A65A69_CNT, \
                        A65A69_M_CNT, A65A69_F_CNT, A70A74_CNT, A70A74_M_CNT, A70A74_F_CNT, \
                        A75A79_CNT, A75A79_M_CNT, A75A79_F_CNT, A80A84_CNT, A80A84_M_CNT, \
                        A80A84_F_CNT, A85A89_CNT, A85A89_M_CNT, A85A89_F_CNT, A90A94_CNT, \
                        A90A94_M_CNT, A90A94_F_CNT, A95A99_CNT, A95A99_M_CNT, A95A99_F_CNT, \
                        A100UP_5_CNT, A100UP_5_M_CNT, A100UP_5_F_CNT,INFO_TIME))
        except Exception as e:
            print e.message
            logger.debug('===combindData==='+e.message)




if __name__ == '__main__':
    mssql = Population_village()
    print mssql.ParserJson(
        url='http://segisws.moi.gov.tw/STATWSSTData/OpenService.asmx/GetAdminSTDataForOpenCode?oCode=ECC48479C0B91632E91C5874DF23C60E51A1FBEE829C41DB0FE22FA2B97D4FF92539094FCB65D41BDDE79C332EB9258D')