# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql
from ToMysql import Cityestateavgsale

logger = logging.getLogger(__name__)

class CityEstateAvgSaleData():
    Data = None
    mysqlconnect = None
    processName = None
    cityestateavgsale = None


    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'城市', u'單位', u'年份', u'商品房平均銷售價格',u'住宅商品房平均銷售價格',
                  u'商品房資料來源', u'住宅商品房資料來源')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "Cityestateavgsale_Data"

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
                self.cityestateavgsale = Cityestateavgsale()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.cityestateavgsale = None

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
            self.cityestateavgsale.setCity(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.cityestateavgsale.setUnit(table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value)
            self.cityestateavgsale.setYear(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)
            self.cityestateavgsale.setCommodity(table.cell(row_index, self.TitleList.index(self.TitleList[3])).value)
            self.cityestateavgsale.setResidentialcommodity(table.cell(row_index, self.TitleList.index(self.TitleList[4])).value)
            self.cityestateavgsale.setCommodity_Source(table.cell(row_index, self.TitleList.index(self.TitleList[5])).value)
            self.cityestateavgsale.setResidentialcommodity_Source(table.cell(row_index, self.TitleList.index(self.TitleList[6])).value)


        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:

            paramList = (self.cityestateavgsale.getCity(), self.cityestateavgsale.getUnit(), self.cityestateavgsale.getYear(),
                         self.cityestateavgsale.getCommodity(), self.cityestateavgsale.getResidentialcommodity(), self.cityestateavgsale.getCommodity_Source(),
                         self.cityestateavgsale.getResidentialcommodity_Source())
            result = self.mysqlconnect.cursor.callproc('sp_INsert_statistics_cityestateavgsale', paramList)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = CityEstateAvgSaleData()
    print mssql.GetData('C:/Users/10509002/Desktop/CDRISBI/CityEstateAvgSale.xlsx')