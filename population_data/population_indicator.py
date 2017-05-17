# -*-  coding: utf-8  -*-
__author__ = '10409003'
import json
import urllib
import csv
import mysql.connector
from setting import Config_2
import logging, time

logger = logging.getLogger(__name__)

class Population_indicator_a():
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
                        i[10],i[11],i[12],i[13])
                cursor.callproc('p_population_a', args)
                db.commit()

        except Exception as e:
            db.rollback()
            print(str(e))
        finally:
            cursor.close()
            db.close()

    def CombindData(self, row, data):
        INFO_TIME = row['INFO_TIME'][0:3]
        COUNTY_ID= row['COUNTY_ID']
        COUNTY= row['COUNTY']
        TOWN_ID= row['TOWN_ID']
        TOWN= row['TOWN']
        V_ID= row['V_ID']
        VILLAGE=row['VILLAGE']
        M_F_RAT=row['M_F_RAT']
        P_H_CNT=row['P_H_CNT']
        P_DEN=row['P_DEN']
        DEPENDENCY_RAT=row['DEPENDENCY_RAT']
        A0A14_A15A65_RAT=row['A0A14_A15A65_RAT']
        A65UP_A15A64_RAT=row['A65UP_A15A64_RAT']
        A65_A0A14_RAT=row['A65_A0A14_RAT']
        data.append((COUNTY_ID, COUNTY, TOWN_ID, TOWN, V_ID, VILLAGE,M_F_RAT, P_H_CNT,
                     P_DEN,DEPENDENCY_RAT,A0A14_A15A65_RAT,A65UP_A15A64_RAT,A65_A0A14_RAT, INFO_TIME))

class Population_indicator_d():
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
            logger.debug("=======write DB=======")
            self.writeDB(data)
            logger.debug('=====finally=====')
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
                        i[10],i[11],i[12],i[13], i[14], i[15], i[16], i[17], i[18], i[19],
                        i[20], i[21], i[22], i[23])
                logger.debug(args)
                cursor.callproc('p_population_d', args)

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
            COUNTY_ID= row['COUNTY_ID']
            COUNTY= row['COUNTY']
            TOWN_ID= row['TOWN_ID']
            TOWN= row['TOWN']
            V_ID= row['V_ID']
            VILLAGE=row['VILLAGE']

            A15UP_M1_M_CNT= int(row['M_A15A24_E1_M1_CNT']) + int(row['M_A15A24_E2_M1_CNT']) + int(row['M_A15A24_E3_M1_CNT']) + \
            int(row['M_A15A24_E4_M1_CNT']) + int(row['M_A25A34_E1_M1_CNT']) + int(row['M_A25A34_E2_M1_CNT']) + int(row['M_A25A34_E3_M1_CNT']) + \
            int(row['M_A25A34_E4_M1_CNT']) + int(row['M_A35A44_E1_M1_CNT']) + int(row['M_A35A44_E2_M1_CNT']) + int(row['M_A35A44_E3_M1_CNT']) + \
            int(row['M_A35A44_E4_M1_CNT']) + int(row['M_A45A54_E1_M1_CNT']) + int(row['M_A45A54_E2_M1_CNT']) + int(row['M_A45A54_E3_M1_CNT']) + \
            int(row['M_A45A54_E4_M1_CNT']) + int(row['M_A55A64_E1_M1_CNT']) + int(row['M_A55A64_E2_M1_CNT']) + int(row['M_A55A64_E3_M1_CNT']) + \
            int(row['M_A55A64_E4_M1_CNT']) + int(row['M_A65UP_E1_M1_CNT']) + int(row['M_A65UP_E2_M1_CNT']) + int(row['M_A65UP_E3_M1_CNT']) + \
            int(row['M_A65UP_E4_M1_CNT'])

            A15UP_M1_F_CNT= int(row['F_A15A24_E1_M1_CNT']) + int(row['F_A15A24_E2_M1_CNT']) + int(row['F_A15A24_E3_M1_CNT']) + \
            int(row['F_A15A24_E4_M1_CNT']) + int(row['F_A25A34_E1_M1_CNT']) + int(row['F_A25A34_E2_M1_CNT']) + int(row['F_A25A34_E3_M1_CNT']) + \
            int(row['F_A25A34_E4_M1_CNT']) + int(row['F_A35A44_E1_M1_CNT']) + int(row['F_A35A44_E2_M1_CNT']) + int(row['F_A35A44_E3_M1_CNT']) + \
            int(row['F_A35A44_E4_M1_CNT']) + int(row['F_A45A54_E1_M1_CNT']) + int(row['F_A45A54_E2_M1_CNT']) + int(row['F_A45A54_E3_M1_CNT']) + \
            int(row['F_A45A54_E4_M1_CNT']) + int(row['F_A55A64_E1_M1_CNT']) + int(row['F_A55A64_E2_M1_CNT']) + int(row['F_A55A64_E3_M1_CNT']) + \
            int(row['F_A55A64_E4_M1_CNT']) + int(row['F_A65UP_E1_M1_CNT']) + int(row['F_A65UP_E2_M1_CNT']) + int(row['F_A65UP_E3_M1_CNT']) + \
            int(row['F_A65UP_E4_M1_CNT'])

            A15UP_M2_M_CNT= int(row['M_A15A24_E1_M2_CNT']) + int(row['M_A15A24_E2_M2_CNT']) + int(row['M_A15A24_E3_M2_CNT']) + \
            int(row['M_A15A24_E4_M2_CNT']) + int(row['M_A25A34_E1_M2_CNT']) + int(row['M_A25A34_E2_M2_CNT']) + int(row['M_A25A34_E3_M2_CNT']) + \
            int(row['M_A25A34_E4_M2_CNT']) + int(row['M_A35A44_E1_M2_CNT']) + int(row['M_A35A44_E2_M2_CNT']) + int(row['M_A35A44_E3_M2_CNT']) + \
            int(row['M_A35A44_E4_M2_CNT']) + int(row['M_A45A54_E1_M2_CNT']) + int(row['M_A45A54_E2_M2_CNT']) + int(row['M_A45A54_E3_M2_CNT']) + \
            int(row['M_A45A54_E4_M2_CNT']) + int(row['M_A55A64_E1_M2_CNT']) + int(row['M_A55A64_E2_M2_CNT']) + int(row['M_A55A64_E3_M2_CNT']) + \
            int(row['M_A55A64_E4_M2_CNT']) + int(row['M_A65UP_E1_M2_CNT']) + int(row['M_A65UP_E2_M2_CNT']) + int(row['M_A65UP_E3_M2_CNT']) + \
            int(row['M_A65UP_E4_M2_CNT'])

            A15UP_M2_F_CNT= int(row['F_A15A24_E1_M2_CNT']) + int(row['F_A15A24_E2_M2_CNT']) + int(row['F_A15A24_E3_M2_CNT']) + \
            int(row['F_A15A24_E4_M2_CNT']) + int(row['F_A25A34_E1_M2_CNT']) + int(row['F_A25A34_E2_M2_CNT']) + int(row['F_A25A34_E3_M2_CNT']) + \
            int(row['F_A25A34_E4_M2_CNT']) + int(row['F_A35A44_E1_M2_CNT']) + int(row['F_A35A44_E2_M2_CNT']) + int(row['F_A35A44_E3_M2_CNT']) + \
            int(row['F_A35A44_E4_M2_CNT']) + int(row['F_A45A54_E1_M2_CNT']) + int(row['F_A45A54_E2_M2_CNT']) + int(row['F_A45A54_E3_M2_CNT']) + \
            int(row['F_A45A54_E4_M2_CNT']) + int(row['F_A55A64_E1_M2_CNT']) + int(row['F_A55A64_E2_M2_CNT']) + int(row['F_A55A64_E3_M2_CNT']) + \
            int(row['F_A55A64_E4_M2_CNT']) + int(row['F_A65UP_E1_M2_CNT']) + int(row['F_A65UP_E2_M2_CNT']) + int(row['F_A65UP_E3_M2_CNT']) + \
            int(row['F_A65UP_E4_M2_CNT'])

            A15UP_M3_M_CNT= int(row['M_A15A24_E1_M3_CNT']) + int(row['M_A15A24_E2_M3_CNT']) + int(row['M_A15A24_E3_M3_CNT']) + \
            int(row['M_A15A24_E4_M3_CNT']) + int(row['M_A25A34_E1_M3_CNT']) + int(row['M_A25A34_E2_M3_CNT']) + int(row['M_A25A34_E3_M3_CNT']) + \
            int(row['M_A25A34_E4_M3_CNT']) + int(row['M_A35A44_E1_M3_CNT']) + int(row['M_A35A44_E2_M3_CNT']) + int(row['M_A35A44_E3_M3_CNT']) + \
            int(row['M_A35A44_E4_M3_CNT']) + int(row['M_A45A54_E1_M3_CNT']) + int(row['M_A45A54_E2_M3_CNT']) + int(row['M_A45A54_E3_M3_CNT']) + \
            int(row['M_A45A54_E4_M3_CNT']) + int(row['M_A55A64_E1_M3_CNT']) + int(row['M_A55A64_E2_M3_CNT']) + int(row['M_A55A64_E3_M3_CNT']) + \
            int(row['M_A55A64_E4_M3_CNT']) + int(row['M_A65UP_E1_M3_CNT']) + int(row['M_A65UP_E2_M3_CNT']) + int(row['M_A65UP_E3_M3_CNT']) + \
            int(row['M_A65UP_E4_M3_CNT'])

            A15UP_M3_F_CNT= int(row['F_A15A24_E1_M3_CNT']) + int(row['F_A15A24_E2_M3_CNT']) + int(row['F_A15A24_E3_M3_CNT']) + \
            int(row['F_A15A24_E4_M3_CNT']) + int(row['F_A25A34_E1_M3_CNT']) + int(row['F_A25A34_E2_M3_CNT']) + int(row['F_A25A34_E3_M3_CNT']) + \
            int(row['F_A25A34_E4_M3_CNT']) + int(row['F_A35A44_E1_M3_CNT']) + int(row['F_A35A44_E2_M3_CNT']) + int(row['F_A35A44_E3_M3_CNT']) + \
            int(row['F_A35A44_E4_M3_CNT']) + int(row['F_A45A54_E1_M3_CNT']) + int(row['F_A45A54_E2_M3_CNT']) + int(row['F_A45A54_E3_M3_CNT']) + \
            int(row['F_A45A54_E4_M3_CNT']) + int(row['F_A55A64_E1_M3_CNT']) + int(row['F_A55A64_E2_M3_CNT']) + int(row['F_A55A64_E3_M3_CNT']) + \
            int(row['F_A55A64_E4_M3_CNT']) + int(row['F_A65UP_E1_M3_CNT']) + int(row['F_A65UP_E2_M3_CNT']) + int(row['F_A65UP_E3_M3_CNT']) + \
            int(row['F_A65UP_E4_M3_CNT'])

            A15UP_M4_M_CNT= int(row['M_A15A24_E1_M4_CNT']) + int(row['M_A15A24_E2_M4_CNT']) + int(row['M_A15A24_E3_M4_CNT']) + \
            int(row['M_A15A24_E4_M4_CNT']) + int(row['M_A25A34_E1_M4_CNT']) + int(row['M_A25A34_E2_M4_CNT']) + int(row['M_A25A34_E3_M4_CNT']) + \
            int(row['M_A25A34_E4_M4_CNT']) + int(row['M_A35A44_E1_M4_CNT']) + int(row['M_A35A44_E2_M4_CNT']) + int(row['M_A35A44_E3_M4_CNT']) + \
            int(row['M_A35A44_E4_M4_CNT']) + int(row['M_A45A54_E1_M4_CNT']) + int(row['M_A45A54_E2_M4_CNT']) + int(row['M_A45A54_E3_M4_CNT']) + \
            int(row['M_A45A54_E4_M4_CNT']) + int(row['M_A55A64_E1_M4_CNT']) + int(row['M_A55A64_E2_M4_CNT']) + int(row['M_A55A64_E3_M4_CNT']) + \
            int(row['M_A55A64_E4_M4_CNT']) + int(row['M_A65UP_E1_M4_CNT']) + int(row['M_A65UP_E2_M4_CNT']) + int(row['M_A65UP_E3_M4_CNT']) + \
            int(row['M_A65UP_E4_M4_CNT'])

            A15UP_M4_F_CNT = int(row['F_A15A24_E1_M4_CNT']) + int(row['F_A15A24_E2_M4_CNT']) + int(row['F_A15A24_E3_M4_CNT']) + \
            int(row['F_A15A24_E4_M4_CNT']) + int(row['F_A25A34_E1_M4_CNT']) + int(row['F_A25A34_E2_M4_CNT']) + int(row['F_A25A34_E3_M4_CNT']) + \
            int(row['F_A25A34_E4_M4_CNT']) + int(row['F_A35A44_E1_M4_CNT']) + int(row['F_A35A44_E2_M4_CNT']) + int(row['F_A35A44_E3_M4_CNT']) + \
            int(row['F_A35A44_E4_M4_CNT']) + int(row['F_A45A54_E1_M4_CNT']) + int(row['F_A45A54_E2_M4_CNT']) + int(row['F_A45A54_E3_M4_CNT']) + \
            int(row['F_A45A54_E4_M4_CNT']) + int(row['F_A55A64_E1_M4_CNT']) + int(row['F_A55A64_E2_M4_CNT']) + int(row['F_A55A64_E3_M4_CNT']) + \
            int(row['F_A55A64_E4_M4_CNT']) + int(row['F_A65UP_E1_M4_CNT']) + int(row['F_A65UP_E2_M4_CNT']) + int(row['F_A65UP_E3_M4_CNT']) + \
            int(row['F_A65UP_E4_M4_CNT'])

            no_edu = 0
            self_edu = 0
            ele_edu = 0
            jun_edu = 0
            sen_edu = 0
            col_edu = 0
            uni_edu = 0
            mas_edu = 0
            phd_edu = 0
            data.append((COUNTY_ID, COUNTY, TOWN_ID, TOWN, V_ID, VILLAGE,A15UP_M1_M_CNT, A15UP_M1_F_CNT,
                         A15UP_M2_M_CNT, A15UP_M2_F_CNT, A15UP_M3_M_CNT, A15UP_M3_F_CNT,
                         A15UP_M4_M_CNT, A15UP_M4_F_CNT, no_edu, self_edu, ele_edu, jun_edu, sen_edu,
                         col_edu, uni_edu, mas_edu, phd_edu, INFO_TIME))

            logger.debug((COUNTY_ID, COUNTY, TOWN_ID, TOWN, V_ID, VILLAGE,A15UP_M1_M_CNT, A15UP_M1_F_CNT,
                         A15UP_M2_M_CNT, A15UP_M2_F_CNT, A15UP_M3_M_CNT, A15UP_M3_F_CNT,
                         A15UP_M4_M_CNT, A15UP_M4_F_CNT, no_edu, self_edu, ele_edu, jun_edu, sen_edu,
                         col_edu, uni_edu, mas_edu, phd_edu, INFO_TIME))
        except Exception as e:
            print e.message
            logger.debug('===combindData==='+e.message)

class Population_indicator_e():
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
            logger.debug("=======write DB=======")
            self.writeDB(data)
            logger.debug('=====finally=====')
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
            idx = 1
            for i in data:
                # idx+=1
                # if idx < 2830:
                #     continue

                args = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],
                        i[10],i[11],i[12],i[13], i[14], i[15])
                logger.debug(args)
                cursor.callproc('p_population_e', args)

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

            no_edu = row['E04_CNT']
            self_edu = row['E03_CNT']
            ele_edu = row['E1_2_CNT']
            jun_edu = row['E8_9_CNT']
            sen_edu = row['E6_7_CNT']
            col_edu = row['E3_4_5_CNT']
            uni_edu = row['E2122_CNT']
            mas_edu = row['E1112_CNT']
            phd_edu = row['E1314_CNT']

            data.append((COUNTY_ID, COUNTY, TOWN_ID, TOWN, V_ID, VILLAGE, no_edu, self_edu, ele_edu, jun_edu, sen_edu,
                         col_edu, uni_edu, mas_edu, phd_edu, INFO_TIME))

            logger.debug((COUNTY_ID, COUNTY, TOWN_ID, TOWN, V_ID, VILLAGE, no_edu, self_edu, ele_edu, jun_edu, sen_edu,
                         col_edu, uni_edu, mas_edu, phd_edu, INFO_TIME))
        except Exception as e:
            print e.message
            logger.debug('===combindData==='+e.message)

class Population_indicator_b:
    def Parsercsv(self,url):
        cr = csv.reader(urllib.urlopen(url))
        data = []
        i = 0
        for row in cr:
            if i >1 :
                self.CombindData(row, data)
            else:
                i+=1
        self.writeDB(data)
        # for row in data:
        #     print row

    def writeDB(self, data):
        try:
            config=Config_2()
            db = mysql.connector.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd, database=config.dbName)
            db.set_charset_collation('utf8')
            cursor = db.cursor()
            for i in data:
                args = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],i[10],i[11])
                print args
                cursor.callproc('p_population_b', args)
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

    def CombindData(self,row,data):
        rowdata=''
        M1_M=0
        M1_F=0
        M2_M = 0
        M2_F = 0
        M3_M = 0
        M3_F = 0
        M4_M = 0
        M4_F = 0
        for r in range(len(row)):
            rowdata += row[r] + ','
        for i in range(3,22):
            M1_M += int(rowdata.split(',')[i])
            M1_F += int(rowdata.split(',')[i+19])
            M2_M += int(rowdata.split(',')[i+38])
            M2_F += int(rowdata.split(',')[i+57])
            M3_M += int(rowdata.split(',')[i+76])
            M3_F += int(rowdata.split(',')[i+95])
            M4_M += int(rowdata.split(',')[i+114])
            M4_F += int(rowdata.split(',')[i+133])
        
        data.append((rowdata.split(',')[1][0:9],rowdata.split(',')[1][9:18],rowdata.split(',')[2],
                       M1_M,M1_F,M2_M,M2_F,M3_M,M3_F,M4_M,M4_F,rowdata.split(',')[0]))

class Population_indicator_c:

    def Parsercsv(self,url):
        cr = csv.reader(urllib.urlopen(url))
        data = []
        i = 0
        for row in cr:
            if i >1 :
                self.CombindData(row, data)
            else:
                i+=1
        self.writeDB(data)
        for row in data:
            print row

    def writeDB(self, data):
        try:
            config=Config_2()
            db = mysql.connector.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd, database=config.dbName)
            db.set_charset_collation('utf8')
            cursor = db.cursor()
            for i in data:
                args = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],i[10],i[11],i[12])
                # print args
                cursor.callproc('p_population_c', args)
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

    def CombindData(self,row,data):
        rowdata = ''
        phd = 0
        mas = 0
        uni = 0
        for r in range(len(row)):
            rowdata += row[r] + ','
        for i in range(4, 8):
            phd += int(rowdata.split(',')[i])
            mas += int(rowdata.split(',')[i + 4])
            uni += int(rowdata.split(',')[i + 8])
        col = int(rowdata.split(',')[16]) + int(rowdata.split(',')[17]) + \
              int(rowdata.split(',')[18]) + int(rowdata.split(',')[19]) + \
              int(rowdata.split(',')[20]) + int(rowdata.split(',')[21]) + \
              int(rowdata.split(',')[22]) + int(rowdata.split(',')[23]) + \
              int(rowdata.split(',')[24]) + int(rowdata.split(',')[25])
        sen = int(rowdata.split(',')[26]) + int(rowdata.split(',')[27]) + \
              int(rowdata.split(',')[28]) + int(rowdata.split(',')[29]) + \
              int(rowdata.split(',')[30]) + int(rowdata.split(',')[31]) + \
              int(rowdata.split(',')[32]) + int(rowdata.split(',')[33])
        jun = int(rowdata.split(',')[34]) + int(rowdata.split(',')[35]) + \
              int(rowdata.split(',')[36]) + int(rowdata.split(',')[37]) + \
              int(rowdata.split(',')[38]) + int(rowdata.split(',')[39]) + \
              int(rowdata.split(',')[40]) + int(rowdata.split(',')[41])
        pri = int(rowdata.split(',')[42]) + int(rowdata.split(',')[43]) + \
              int(rowdata.split(',')[44]) + int(rowdata.split(',')[45])
        sel = int(rowdata.split(',')[46]) + int(rowdata.split(',')[47])
        no = int(rowdata.split(',')[48]) + int(rowdata.split(',')[49])
        data.append((rowdata.split(',')[1][0:9],rowdata.split(',')[1][9:18],rowdata.split(',')[2],
             no, sel, pri, jun, sen, col, uni, mas, phd,rowdata.split(',')[0]))


if __name__ == '__main__':
    # mssql = Population_indicator_d()
    # print mssql.ParserJson(url='http://segisws.moi.gov.tw/STATWSSTData/OpenService.asmx/GetAdminSTDataForOpenCode?oCode=ECC48479C0B91632E91C5874DF23C60E51A1FBEE829C41DBC09B9B1454506F40B9422055B5A47ABBD5421BC7960893AF')
    tmp = Population_indicator_a()
    print tmp.ParserJson(url = 'http://segisws.moi.gov.tw/STATWSSTData/OpenService.asmx/GetAdminSTDataForOpenCode?oCode=ECC48479C0B91632E91C5874DF23C60E51A1FBEE829C41DB309864665027587E2539094FCB65D41BDDE79C332EB9258D')
    # mssql = Population_indicator_e()
    # print mssql.ParserJson(url='http://segisws.moi.gov.tw/STATWSSTData/OpenService.asmx/GetAdminSTDataForOpenCode?oCode=ECC48479C0B91632E91C5874DF23C60E51A1FBEE829C41DBFCC17E8034AB503F212AB7B0B0B2E8CAD5421BC7960893AF')