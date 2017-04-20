# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql
from ToMysql import Cityretailexponent

logger = logging.getLogger(__name__)

class CityRetailExponentData():
    Data = None
    mysqlconnect = None
    processName = None
    cityretailexponent = None


    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'城市', u'年份', u'商品零售價格指數',u'食品商品零售價格指數', u'飲料、煙酒商品零售價格指數',
                  u'服裝鞋帽商品零售價格指數', u'紡織品商品零售價格指數', u'日用商品零售價格指數', u'化妝品商品零售價格指數',
                  u'燃料商品零售價格指數', u'商品零售價格指數資料來源', u'紡織品商品零售價格指數資料來源',
                  u'服裝鞋帽商品零售價格指數資料來源',u'化妝品商品零售價格指數資料來源', u'燃料商品零售價格指數資料來源',
                  u'日用商品零售價格指數資料來源', u'食品商品零售價格指數資料來源', u'飲料、煙酒商品零售價格指數資料來源')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "CityRetailExponent_Data"

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
                self.cityretailexponent = Cityretailexponent()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.cityretailexponent = None

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
            self.cityretailexponent.setCity(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.cityretailexponent.setYear(table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value)
            self.cityretailexponent.setTotal(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)
            self.cityretailexponent.setTextile(table.cell(row_index, self.TitleList.index(self.TitleList[6])).value)
            self.cityretailexponent.setClothing(table.cell(row_index, self.TitleList.index(self.TitleList[5])).value)
            self.cityretailexponent.setCosmetic(table.cell(row_index, self.TitleList.index(self.TitleList[8])).value)
            self.cityretailexponent.setFuel(table.cell(row_index, self.TitleList.index(self.TitleList[9])).value)
            self.cityretailexponent.setNecessary(table.cell(row_index, self.TitleList.index(self.TitleList[7])).value)
            self.cityretailexponent.setFood(table.cell(row_index, self.TitleList.index(self.TitleList[3])).value)
            self.cityretailexponent.setDrinks(table.cell(row_index, self.TitleList.index(self.TitleList[4])).value)
            self.cityretailexponent.setTotal_Source(table.cell(row_index, self.TitleList.index(self.TitleList[10])).value)
            self.cityretailexponent.setTextile_Source(table.cell(row_index, self.TitleList.index(self.TitleList[11])).value)
            self.cityretailexponent.setClothing_source(table.cell(row_index, self.TitleList.index(self.TitleList[12])).value)
            self.cityretailexponent.setCosmetic_Source(table.cell(row_index, self.TitleList.index(self.TitleList[13])).value)
            self.cityretailexponent.setFuel_Source(table.cell(row_index, self.TitleList.index(self.TitleList[14])).value)
            self.cityretailexponent.setNecessary_Source(table.cell(row_index, self.TitleList.index(self.TitleList[15])).value)
            self.cityretailexponent.setFood_Source(table.cell(row_index, self.TitleList.index(self.TitleList[16])).value)
            self.cityretailexponent.setDrinks_Source(table.cell(row_index, self.TitleList.index(self.TitleList[17])).value)

        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:

            paramList = (self.cityretailexponent.getCity(), self.cityretailexponent.getYear(), self.cityretailexponent.getTotal(),
                         self.cityretailexponent.getTextile(), self.cityretailexponent.getClothing(), self.cityretailexponent.getCosmetic(),
                         self.cityretailexponent.getFuel(), self.cityretailexponent.getNecessary(), self.cityretailexponent.getFood(),
                         self.cityretailexponent.getDrinks(), self.cityretailexponent.getTotal_Source(), self.cityretailexponent.getTextile_Source(),
                         self.cityretailexponent.getClothing_source(), self.cityretailexponent.getCosmetic_Source(), self.cityretailexponent.getFuel_Source(),
                         self.cityretailexponent.getNecessary_Source(), self.cityretailexponent.getFood_Source(), self.cityretailexponent.getDrinks_Source())
            result = self.mysqlconnect.cursor.callproc('sp_INsert_statistics_cityretailexponent', paramList)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = CityRetailExponentData()
    print mssql.GetData('C:/Users/10509002/Desktop/CDRISBI/CityRetailExponent.xlsx')