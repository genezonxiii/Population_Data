# -*-  coding: utf-8  -*-
__author__ = '10409003'
import json,urllib
import mysql.connector
class OpenData_marriage:
    def ParserJson(self,url):
        result = json.load(urllib.urlopen(url))
        data =[]
        for each in result['RowDataList']:
            self.CombindData(each, data)
        # self.writeDB(data)
        for result in data:
            print result

    def CombindData(self,row,data):
        INFO_TIME=row['INFO_TIME']
        CODE2=row['CODE2']
        A15UP_M1_CNT=row['A15UP_M1_CNT']
        A15UP_M2_CNT=row['A15UP_M2_CNT']
        A15UP_M3_CNT=row['A15UP_M3_CNT']
        A15UP_M4_CNT=row['A15UP_M4_CNT']
        data.append((INFO_TIME,CODE2,A15UP_M1_CNT+A15UP_M2_CNT,A15UP_M3_CNT,A15UP_M4_CNT))

class OpenData_FiveYear_M:
    def ParserJson(self,url):
        result = json.load(urllib.urlopen(url))
        data =[]
        for each in result['RowDataList']:
            self.CombindData(each, data)
        for result in data:
            print result
    def CombindData(self,row,data):
        PRODUCT_ID=row['PRODUCT_ID']
        INFO_TIME=row['INFO_TIME']
        CODE2=row['CODE2']
        A0A4_M_CNT=row['A0A4_M_CNT']
        A5A9_M_CNT=row['A5A9_M_CNT']
        A10A14_M_CNT=row['A10A14_M_CNT']
        A15A19_M_CNT=row['A15A19_M_CNT']
        A20A24_M_CNT=row['A20A24_M_CNT']
        A25A29_M_CNT=row['A25A29_M_CNT']
        A30A34_M_CNT=row['A30A34_M_CNT']
        A35A39_M_CNT=row['A35A39_M_CNT']
        A40A44_M_CNT=row['A40A44_M_CNT']
        A45A49_M_CNT=row['A45A49_M_CNT']
        A50A54_M_CNT=row['A50A54_M_CNT']
        A55A59_M_CNT=row['A55A59_M_CNT']
        A60A64_M_CNT=row['A60A64_M_CNT']
        A65A69_M_CNT=row['A65A69_M_CNT']
        A70A74_M_CNT=row['A70A74_M_CNT']
        A75A79_M_CNT=row['A75A79_M_CNT']
        A80A84_M_CNT=row['A80A84_M_CNT']
        A85A89_M_CNT=row['A85A89_M_CNT']
        A90A94_M_CNT=row['A90A94_M_CNT']
        A95A99_M_CNT=row['A95A99_M_CNT']
        A100UP_M_5_CNT=row['A100UP_M_5_CNT']

        data.append((PRODUCT_ID,INFO_TIME,CODE2,A0A4_M_CNT,A5A9_M_CNT,
    A10A14_M_CNT,A15A19_M_CNT,A20A24_M_CNT,A25A29_M_CNT,A30A34_M_CNT,
    A35A39_M_CNT,A40A44_M_CNT,A45A49_M_CNT,A50A54_M_CNT,A55A59_M_CNT,
    A60A64_M_CNT,A65A69_M_CNT,A70A74_M_CNT,A75A79_M_CNT,A80A84_M_CNT,A85A89_M_CNT,
    A90A94_M_CNT,A95A99_M_CNT,A100UP_M_5_CNT))
class OpenData_FiveYear_F:
    def ParserJson(self, url):
        result = json.load(urllib.urlopen(url))
        data = []
        for each in result['RowDataList']:
            self.CombindData(each, data)
        for result in data:
            print result

    def CombindData(self, row, data):
        PRODUCT_ID = row['PRODUCT_ID']
        INFO_TIME = row['INFO_TIME']
        CODE2 = row['CODE2']
        A0A4_F_CNT = row['A0A4_F_CNT']
        A5A9_F_CNT = row['A5A9_F_CNT']
        A10A14_F_CNT = row['A10A14_F_CNT']
        A15A19_F_CNT = row['A15A19_F_CNT']
        A20A24_F_CNT = row['A20A24_F_CNT']
        A25A29_F_CNT = row['A25A29_F_CNT']
        A30A34_F_CNT = row['A30A34_F_CNT']
        A35A39_F_CNT = row['A35A39_F_CNT']
        A40A44_F_CNT = row['A40A44_F_CNT']
        A45A49_F_CNT = row['A45A49_F_CNT']
        A50A54_F_CNT = row['A50A54_F_CNT']
        A55A59_F_CNT = row['A55A59_F_CNT']
        A60A64_F_CNT = row['A60A64_F_CNT']
        A65A69_F_CNT = row['A65A69_F_CNT']
        A70A74_F_CNT = row['A70A74_F_CNT']
        A75A79_F_CNT = row['A75A79_F_CNT']
        A80A84_F_CNT = row['A80A84_F_CNT']
        A85A89_F_CNT = row['A85A89_F_CNT']
        A90A94_F_CNT = row['A90A94_F_CNT']
        A95A99_F_CNT = row['A95A99_F_CNT']
        A100UP_F_5_CNT = row['A100UP_F_5_CNT']

        data.append((PRODUCT_ID, INFO_TIME, CODE2,A0A4_F_CNT,A5A9_F_CNT,
                     A10A14_F_CNT, A15A19_F_CNT,A20A24_F_CNT, A25A29_F_CNT, A30A34_F_CNT,
                     A35A39_F_CNT, A40A44_F_CNT,A45A49_F_CNT, A50A54_F_CNT,
                     A55A59_F_CNT,A60A64_F_CNT, A65A69_F_CNT,A70A74_F_CNT,
                     A75A79_F_CNT, A80A84_F_CNT,A85A89_F_CNT,
                     A90A94_F_CNT, A95A99_F_CNT,A100UP_F_5_CNT))
class OpenData_FiveYear_All:
    def ParserJson(self, url):
        result = json.load(urllib.urlopen(url))
        data = []
        for each in result['RowDataList']:
            self.CombindData(each, data)
        for result in data:
            print result

    def CombindData(self, row, data):
        PRODUCT_ID = row['PRODUCT_ID']
        INFO_TIME = row['INFO_TIME']
        CODE2 = row['CODE2']
        A0A4_CNT = row['A0A4_CNT']
        A5A9_CNT = row['A5A9_CNT']
        A10A14_CNT = row['A10A14_CNT']
        A15A19_CNT = row['A15A19_CNT']
        A20A24_CNT = row['A20A24_CNT']
        A25A29_CNT = row['A25A29_CNT']
        A30A34_CNT = row['A30A34_CNT']
        A35A39_CNT = row['A35A39_CNT']
        A40A44_CNT = row['A40A44_CNT']
        A45A49_CNT = row['A45A49_CNT']
        A50A54_CNT = row['A50A54_CNT']
        A55A59_CNT = row['A55A59_CNT']
        A60A64_CNT = row['A60A64_CNT']
        A65A69_CNT = row['A65A69_CNT']
        A70A74_CNT = row['A70A74_CNT']
        A75A79_CNT = row['A75A79_CNT']
        A80A84_CNT = row['A80A84_CNT']
        A85A89_CNT = row['A85A89_CNT']
        A90A94_CNT = row['A85A89_F_CNT']
        A95A99_CNT = row['A95A99_CNT']
        A100UP_5_CNT = row['A100UP_5_CNT']

        data.append((PRODUCT_ID, INFO_TIME, CODE2, A0A4_CNT, A5A9_CNT,A10A14_CNT,
                     A15A19_CNT, A20A24_CNT,A25A29_CNT,A30A34_CNT,
                     A35A39_CNT, A40A44_CNT, A45A49_CNT,A50A54_CNT, A55A59_CNT,
                     A60A64_CNT, A65A69_CNT,A70A74_CNT,A75A79_CNT, A80A84_CNT, A85A89_CNT,
                     A90A94_CNT, A95A99_CNT, A100UP_5_CNT))
class OpenData_Population:
    def ParserJson(self,url):
        result = json.load(urllib.urlopen(url))
        data =[]
        for each in result['RowDataList']:
            self.CombindData(each,data)
        for result in data:
            print result

    def CombindData(self,row,data):
        PRODUCT_ID=row['PRODUCT_ID']
        INFO_TIME=row['INFO_TIME']
        CODE2=row['CODE2']
        H_CNT=row['H_CNT']
        P_CNT=row['P_CNT']
        M_CNT=row['M_CNT']
        F_CNT=row['F_CNT']

        data.append((PRODUCT_ID,INFO_TIME,CODE2,H_CNT,P_CNT,M_CNT,F_CNT))



class OpenData_sex_marriage:
    def ParserJson(self, url):
        result = json.load(urllib.urlopen(url))
        data = []
        resultdata = []
        CountyId = result["Info"][0]
        for each in result['RowDataList']:
            self.RobinCombindData(each, data, CountyId['InCountyId'])
        self.sumData(data, resultdata)
        self.writeDB(resultdata)
        # for result in data:
        #     print result

    def writeDB(self, data):
        try:
            db = mysql.connector.connect(user='root', password='password', host='192.168.112.175',
                                         database='statistics')
            db.set_charset_collation('utf8')
            cursor = db.cursor()
            for i in data:
                args = (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
                # print args
                cursor.callproc('p_test_marriage_county', args)
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

    def RobinCombindData(self, row, data, county):
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
        row1 = 0
        row2 = 0
        row3 = 0
        row4 = 0
        row5 = 0
        row6 = 0
        row7 = 0
        row8 = 0
        row9 = ''
        for row in data:
            for i in range(len(row)):
                row1 += row[1]
                row2 += row[2]
                row3 += row[3]
                row4 += row[4]
                row5 += row[5]
                row6 += row[6]
                row7 += row[7]
                row8 += row[8]
                row9 = row[9]
                strCountID = row[0]
        resultdata.append((strCountID, row1, row2, row3, row4, row5, row6, row7, row8, row9))
