# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql
from ToMysql import Citytertiaryincrease

logger = logging.getLogger(__name__)

class CityTertiaryIncreaseData():
    Data = None
    mysqlconnect = None
    processName = None
    citytertiaryincrease = None


    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'城市', u'年份', u'第三產業增加值',u'第三產業增加值指數', u'第三產業增加值資料來源',
                  u'第三產業增加值指數資料來源')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "CityTertiaryIncrease_Data"

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
                self.citytertiaryincrease = Citytertiaryincrease()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.citytertiaryincrease = None

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
            self.citytertiaryincrease.setCity(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.citytertiaryincrease.setYear(table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value)
            self.citytertiaryincrease.setAmount(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)
            self.citytertiaryincrease.setExponent(table.cell(row_index, self.TitleList.index(self.TitleList[3])).value)
            self.citytertiaryincrease.setAmount_Source(table.cell(row_index, self.TitleList.index(self.TitleList[4])).value)
            self.citytertiaryincrease.setExponent_Source(table.cell(row_index, self.TitleList.index(self.TitleList[5])).value)

        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:

            paramList = (self.citytertiaryincrease.getCity(), self.citytertiaryincrease.getYear(), self.citytertiaryincrease.getAmount(),
                         self.citytertiaryincrease.getExponent(), self.citytertiaryincrease.getAmount_Source(), self.citytertiaryincrease.getExponent_Source())
            result = self.mysqlconnect.cursor.callproc('sp_INsert_statistics_citytertiaryincrease', paramList)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = CityTertiaryIncreaseData()
    print mssql.GetData('C:/Users/10509002/Desktop/CDRISBI/CityTertiaryIncrease.xlsx')