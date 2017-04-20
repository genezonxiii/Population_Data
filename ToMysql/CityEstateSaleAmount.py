# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql
from ToMysql import Cityestatesaleamount

logger = logging.getLogger(__name__)

class CityEstateSaleAmountData():
    Data = None
    mysqlconnect = None
    processName = None
    cityestatesaleamount = None


    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'城市', u'單位', u'年份', u'商品房銷售額',u'住宅商品房銷售額',
                  u'辦公樓銷售額', u'商業營業用房銷售額', u'商業營業用房', u'辦公樓資料來源',u'住宅商品房資料來源',
                  u'商品房資料來源')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "Cityestatesaleamount_Data"

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
                self.cityestatesaleamount = Cityestatesaleamount()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.cityestatesaleamount = None

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
            self.cityestatesaleamount.setCity(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.cityestatesaleamount.setUnit(table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value)
            self.cityestatesaleamount.setYear(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)
            self.cityestatesaleamount.setCommerce(table.cell(row_index, self.TitleList.index(self.TitleList[3])).value)
            self.cityestatesaleamount.setOffice(table.cell(row_index, self.TitleList.index(self.TitleList[4])).value)
            self.cityestatesaleamount.setResidential(table.cell(row_index, self.TitleList.index(self.TitleList[5])).value)
            self.cityestatesaleamount.setCommodity(table.cell(row_index, self.TitleList.index(self.TitleList[6])).value)
            self.cityestatesaleamount.setCommerce_Source(table.cell(row_index, self.TitleList.index(self.TitleList[7])).value)
            self.cityestatesaleamount.setOffice_Source(table.cell(row_index, self.TitleList.index(self.TitleList[8])).value)
            self.cityestatesaleamount.setResidential_Source(table.cell(row_index, self.TitleList.index(self.TitleList[9])).value)
            self.cityestatesaleamount.setCommodity_Source(table.cell(row_index, self.TitleList.index(self.TitleList[10])).value)


        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:

            paramList = (self.cityestatesaleamount.getCity(), self.cityestatesaleamount.getUnit(), self.cityestatesaleamount.getYear(),
                         self.cityestatesaleamount.getCommerce(), self.cityestatesaleamount.getOffice(), self.cityestatesaleamount.getResidential(),
                         self.cityestatesaleamount.getCommodity(), self.cityestatesaleamount.getCommerce_Source(), self.cityestatesaleamount.getOffice_Source(),
                         self.cityestatesaleamount.getResidential_Source(), self.cityestatesaleamount.getCommodity_Source())
            result = self.mysqlconnect.cursor.callproc('sp_INsert_statistics_cityestatesaleamount', paramList)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = CityEstateSaleAmountData()
    print mssql.GetData('C:/Users/10509002/Desktop/CDRISBI/CityEstateSaleAmount.xlsx')