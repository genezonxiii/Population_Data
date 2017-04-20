# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql
from ToMysql import Citysocialconsume

logger = logging.getLogger(__name__)

class CitySocialConsumeData():
    Data = None
    mysqlconnect = None
    processName = None
    citysocialconsume = None


    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'城市', u'單位', u'年份', u'社會消費品零售總額',u'限額以上批發、零售貿易業商品銷售總額',
                  u'限額以上批發零售貿易業商品零售銷售總額', u'社會消費品零售總額資料來源', u'限額以上批發、零售貿易業商品銷售總額資料來源',
                  u'限額以上批發零售貿易業商品零售銷售總額資料來源')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "CitySocialConsume_Data"

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
                self.citysocialconsume = Citysocialconsume()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.citysocialconsume = None

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
            self.citysocialconsume.setCity(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.citysocialconsume.setUnit(table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value)
            self.citysocialconsume.setYear(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)
            self.citysocialconsume.setRetailsum(table.cell(row_index, self.TitleList.index(self.TitleList[3])).value)
            self.citysocialconsume.setWholesaleretailsale(table.cell(row_index, self.TitleList.index(self.TitleList[4])).value)
            self.citysocialconsume.setWholesaleretail_Retailsum(table.cell(row_index, self.TitleList.index(self.TitleList[5])).value)
            self.citysocialconsume.setRetailsum_Source(table.cell(row_index, self.TitleList.index(self.TitleList[6])).value)
            self.citysocialconsume.setWholesaleretailsale_Source(table.cell(row_index, self.TitleList.index(self.TitleList[7])).value)
            self.citysocialconsume.setWholesaleretail_Retailsum_Source(table.cell(row_index, self.TitleList.index(self.TitleList[8])).value)

        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:

            paramList = (self.citysocialconsume.getCity(), self.citysocialconsume.getUnit(), self.citysocialconsume.getYear(),
                         self.citysocialconsume.getRetailsum(), self.citysocialconsume.getWholesaleretailsale(), self.citysocialconsume.getWholesaleretail_Retailsum(),
                         self.citysocialconsume.getRetailsum_Source(), self.citysocialconsume.getWholesaleretailsale_Source(), self.citysocialconsume.getWholesaleretail_Retailsum_Source())
            result = self.mysqlconnect.cursor.callproc('sp_INsert_statistics_citysocialconsume', paramList)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = CitySocialConsumeData()
    print mssql.GetData('C:/Users/10509002/Desktop/CDRISBI/CitySocialConsume.xlsx')