# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql
from ToMysql import Countrystatistic

logger = logging.getLogger(__name__)

class CountrystatisticData():
    Data = None
    mysqlconnect = None
    processName = None
    countrystatistic = None


    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'國家', u'結構', u'尺寸', u'來源', u'目標',u'第二目標',
                  u'單位', u'類型', u'資料')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "Countrystatistic_Data"

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


            # 存放excel中對應TitleTuple欄位名稱的index
            for index in range(0, len(self.TitleTuple)):
                if self.TitleTuple[index] in self.TitleList:
                    logger.debug(str(index) + self.TitleTuple[index])
                    logger.debug(u'index in file - ' + str(self.TitleList.index(self.TitleTuple[index])))


            for row_index in range(1, table.nrows):
                self.countrystatistic = Countrystatistic()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.countrystatistic = None

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
            self.countrystatistic.setCountry(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.countrystatistic.setStructure(table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value)
            self.countrystatistic.setDimensions(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)
            self.countrystatistic.setSource(table.cell(row_index, self.TitleList.index(self.TitleTuple[3])).value)
            self.countrystatistic.setTarget(table.cell(row_index, self.TitleList.index(self.TitleTuple[4])).value)
            self.countrystatistic.setSecond_target(table.cell(row_index, self.TitleList.index(self.TitleTuple[5])).value)
            self.countrystatistic.setUnit(table.cell(row_index, self.TitleList.index(self.TitleTuple[6])).value)
            self.countrystatistic.setType(table.cell(row_index, self.TitleList.index(self.TitleTuple[7])).value)
            self.countrystatistic.setData(table.cell(row_index, self.TitleList.index(self.TitleTuple[8])).value)

        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:

            paramList = (self.countrystatistic.getCountry(), self.countrystatistic.getStructure(), self.countrystatistic.getDimensions(), self.countrystatistic.getSource(),
                         self.countrystatistic.getTarget(), self.countrystatistic.getSecond_Target(), self.countrystatistic.getUnit(),self.countrystatistic.getType(), self.countrystatistic.getData())
            result = self.mysqlconnect.cursor.callproc('sp_insert_countrystatistic', paramList)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = CountrystatisticData()
    print mssql.GetData('C:/Users/10509002/Desktop/Countrystatistic.xlsx')