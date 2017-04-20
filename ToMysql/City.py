# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql,City

logger = logging.getLogger(__name__)

class CityData():
    Data = None
    mysqlconnect = None
    # name, latitude, longitude = None,None,None
    city = None



    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'城市名稱', u'緯度', u'經度')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "City_Data"

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
                self.city = City()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.city = None

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
            # self.name = table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value
            # self.latitude = table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value
            # self.longitude = table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value
            self.city.setName(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.city.setLatitude(table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value)
            self.city.setLongitude(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)

        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:
            # paramList = (self.name, self.latitude, self.longitude)
            paramList = (self.city.getName(), self.city.getLatitude(), self.city.getLongitude())
            result = self.mysqlconnect.cursor.callproc('sp_insert_statistics_city', paramList)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = CityData()
    print mssql.GetData('C:/Users/10509002/Desktop/CDRISBI/City.xlsx')