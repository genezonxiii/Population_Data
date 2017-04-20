# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql
from ToMysql import Marketsize

logger = logging.getLogger(__name__)

class MarketsizeData():
    Data = None
    mysqlconnect = None
    processName = None
    marketsize = None


    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'國家',u'產業類別', u'主題', u'子項目', u'類別', u'單位', u'年', u'資料', u'資料來源')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "Marketsize_Data"

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
                self.marketsize = Marketsize()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.marketsize = None

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
            self.marketsize.setCountry(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.marketsize.setIndustrytype(table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value)
            self.marketsize.setSource(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)
            self.marketsize.setSubsource(table.cell(row_index, self.TitleList.index(self.TitleTuple[3])).value)
            self.marketsize.setCategories(table.cell(row_index, self.TitleList.index(self.TitleTuple[4])).value)
            self.marketsize.setCategoriesyear(table.cell(row_index, self.TitleList.index(self.TitleTuple[6])).value)
            self.marketsize.setCategoriesdata(table.cell(row_index, self.TitleList.index(self.TitleTuple[7])).value)
            self.marketsize.setUnit(table.cell(row_index, self.TitleList.index(self.TitleTuple[5])).value)
            self.marketsize.setDatasource(table.cell(row_index, self.TitleList.index(self.TitleTuple[8])).value)


        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:

            paramList = (self.marketsize.getCountry(), self.marketsize.getIndustrytype(), self.marketsize.getSource(),
                         self.marketsize.getSubsource(), self.marketsize.getCategories(), self.marketsize.getCategoriesyear(),
                         self.marketsize.getCategoriesdata(), self.marketsize.getUnit(), self.marketsize.getDatasource())
            result = self.mysqlconnect.cursor.callproc('sp_INsert_statistics_marketsize', paramList)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = MarketsizeData()
    print mssql.GetData('C:/Users/10509002/Desktop/CDRISBI/MarketSize.xlsx')