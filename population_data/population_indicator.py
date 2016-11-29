# -*-  coding: utf-8  -*-
__author__ = '10409003'
import json
import urllib
import csv
import mysql.connector
from setting import Config_2

class Population_indicator_a:
    def ParserJson(self, url):
        result = json.load(urllib.urlopen(url))
        data = []
        for each in result['RowDataList']:
            self.CombindData(each, data)
        self.writeDB(data)
        for result in data:
            print result

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
        INFO_TIME = row['INFO_TIME'][0:3]
        COUNTY_ID=row['COUNTY_ID']
        COUNTY=row['COUNTY']
        TOWN_ID=row['TOWN_ID']
        TOWN=row['TOWN']
        V_ID=row['V_ID']
        VILLAGE=row['VILLAGE']
        M_F_RAT=row['M_F_RAT']
        P_H_CNT=row['P_H_CNT']
        P_DEN=row['P_DEN']
        DEPENDENCY_RAT=row['DEPENDENCY_RAT']
        A0A14_A15A65_RAT=row['A0A14_A15A65_RAT']
        A65UP_A15A64_RAT=row['A65UP_A15A64_RAT']
        A65_A0A14_RAT=row['A65_A0A14_RAT']
        data.append((COUNTY_ID, COUNTY, TOWN_ID, TOWN, V_ID, VILLAGE, M_F_RAT, P_H_CNT,
                     P_DEN,DEPENDENCY_RAT,A0A14_A15A65_RAT,A65UP_A15A64_RAT,A65_A0A14_RAT, INFO_TIME))

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
