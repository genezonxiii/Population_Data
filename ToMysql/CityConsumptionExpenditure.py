# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql
from ToMysql import CityConsumptionExpenditure

logger = logging.getLogger(__name__)

class CityConsumptionExpenditureData():
    Data = None
    mysqlconnect = None
    processName = None
    cityconsumptionexpenditure = None


    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'城市', u'單位', u'年份', u'城鎮居民人均消費支出',u'城鎮居民家庭人均食品菸酒消費支出',
                  u'城鎮居民家庭人均衣著消費支出', u'城鎮居民家庭人均居住消費支出',u'城鎮居民家庭人均交通和通訊消費支出',
                  u'城鎮居民家庭人均教育文化娛樂服務消費支出',u'城鎮居民家庭人均生活用品及服務消費支出',u'城鎮居民家庭人均醫療保健消費支出',
                  u'成鎮居民家庭平均消費支出', u'人均消費支出資料來源', u'食品菸酒消費支出資料來源', u'衣著消費支出資料來源',
                  u'居住消費支出資料來源', u'交通和通訊消費支出資料來源', u'教育文化娛樂服務消費支出資料來源', u'生活用品及服務消費支出資料來源',
                  u'醫療保健消費支出資料來源',u'家庭平均消費支出資料來源')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "ConsumptionExpenditure_Data"

    def GetData(self,path):
        try:
            logger.debug("===" + self.processName + "===")
            success = False
            resultinfo = ""
            totalRows = 0

            data = xlrd.open_workbook(path)
            table = data.sheets()[0]

            totalRows = table.nrows - 1

            # 存放excel中全部的欄位名稱
            self.TitleList = []
            for row_index in range(0, 1):
                for col_index in range(0, table.ncols):
                    self.TitleList.append(table.cell(row_index, col_index).value)

            # print self.TitleList

            # 存放excel中對應TitleTuple欄位名稱的index
            for index in range(0, len(self.TitleTuple)):
                if self.TitleTuple[index] in self.TitleList:
                    logger.debug(str(index) + self.TitleTuple[index])
                    logger.debug(u'index in file - ' + str(self.TitleList.index(self.TitleTuple[index])))


            for row_index in range(1, table.nrows):
                self.cityconsumptionexpenditure = CityConsumptionExpenditure()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.cityconsumptionexpenditure = None

            self.mysqlconnect.db.commit()
            self.mysqlconnect.dbClose()

            success = True

        except Exception as inst:
            logger.error(inst.args)
            resultinfo = inst.args
        finally:
            logger.debug("===" + self.processName + " finally===")
            return json.dumps({"success": success, "info": resultinfo, "total": totalRows}, sort_keys=False)

    def parserData(self,table,row_index):
        try:
            self.cityconsumptionexpenditure.setCity(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.cityconsumptionexpenditure.setUnit(table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value)
            self.cityconsumptionexpenditure.setYear(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)
            self.cityconsumptionexpenditure.setTotal(table.cell(row_index, self.TitleList.index(self.TitleList[3])).value)
            self.cityconsumptionexpenditure.setFood(table.cell(row_index, self.TitleList.index(self.TitleList[4])).value)
            self.cityconsumptionexpenditure.setClothes(table.cell(row_index, self.TitleList.index(self.TitleList[5])).value)
            self.cityconsumptionexpenditure.setLive(table.cell(row_index, self.TitleList.index(self.TitleList[6])).value)
            self.cityconsumptionexpenditure.setTrafficcommu(table.cell(row_index, self.TitleList.index(self.TitleList[7])).value)
            self.cityconsumptionexpenditure.setEducation(table.cell(row_index, self.TitleList.index(self.TitleList[8])).value)
            self.cityconsumptionexpenditure.setLifelihood(table.cell(row_index, self.TitleList.index(self.TitleList[9])).value)
            self.cityconsumptionexpenditure.setHealthcare(table.cell(row_index, self.TitleList.index(self.TitleList[10])).value)
            self.cityconsumptionexpenditure.setHousehold(table.cell(row_index, self.TitleList.index(self.TitleList[11])).value)
            self.cityconsumptionexpenditure.setTotal_Source(table.cell(row_index, self.TitleList.index(self.TitleList[12])).value)
            self.cityconsumptionexpenditure.setFood_Source(table.cell(row_index, self.TitleList.index(self.TitleList[13])).value)
            self.cityconsumptionexpenditure.setClothes_Source(table.cell(row_index, self.TitleList.index(self.TitleList[14])).value)
            self.cityconsumptionexpenditure.setLive_Source(table.cell(row_index, self.TitleList.index(self.TitleList[15])).value)
            self.cityconsumptionexpenditure.setTrafficcommu_Source(table.cell(row_index, self.TitleList.index(self.TitleList[16])).value)
            self.cityconsumptionexpenditure.setEducation_Source(table.cell(row_index, self.TitleList.index(self.TitleList[17])).value)
            self.cityconsumptionexpenditure.setLifelihood_Source(table.cell(row_index, self.TitleList.index(self.TitleList[18])).value)
            self.cityconsumptionexpenditure.setHealthcare_Source(table.cell(row_index, self.TitleList.index(self.TitleList[19])).value)
            self.cityconsumptionexpenditure.setHousehold_Source(table.cell(row_index, self.TitleList.index(self.TitleList[20])).value)


        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:

            paramList = (self.cityconsumptionexpenditure.getCity(), self.cityconsumptionexpenditure.getUnit(), self.cityconsumptionexpenditure.getYear(),
                         self.cityconsumptionexpenditure.getTotal(), self.cityconsumptionexpenditure.getFood(), self.cityconsumptionexpenditure.getClothes(),
                         self.cityconsumptionexpenditure.getLive(), self.cityconsumptionexpenditure.getTrafficcommu(),self.cityconsumptionexpenditure.getEducation(),
                         self.cityconsumptionexpenditure.getLifelihood(), self.cityconsumptionexpenditure.getHealthcare(), self.cityconsumptionexpenditure.getHousehold(),
                         self.cityconsumptionexpenditure.getTotal_Source(), self.cityconsumptionexpenditure.getFood_Source(), self.cityconsumptionexpenditure.getClothes_Source(),
                         self.cityconsumptionexpenditure.getLive_Source(), self.cityconsumptionexpenditure.getTrafficcommu_Source(), self.cityconsumptionexpenditure.getEducation_Source(),
                         self.cityconsumptionexpenditure.getLifelihood_Source(), self.cityconsumptionexpenditure.getHealthcare_Source(), self.cityconsumptionexpenditure.getHousehold_Source())
            result = self.mysqlconnect.cursor.callproc('sp_INsert_Statistics_CityConsumptionExpenditure', paramList)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = CityConsumptionExpenditureData()
    print mssql.GetData('C:/Users/10509002/Desktop/CDRISBI/CityConsumptionExpendditure.xlsx')