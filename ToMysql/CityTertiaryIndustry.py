# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql
from ToMysql import Citytertiaryindustry

logger = logging.getLogger(__name__)

class CityTertiaryIndustryData():
    Data = None
    mysqlconnect = None
    processName = None
    citytertiaryindustry = None


    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'城市', u'年份', u'第三產業GDP',u'單位', u'第三產業從業人員數',
                  u'第三產業GDP資料來源', u'第三產業從業人員數資料來源')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "CityTertiaryIndustry_Data"

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
                self.citytertiaryindustry = Citytertiaryindustry()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.citytertiaryindustry = None

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
            self.citytertiaryindustry.setCity(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.citytertiaryindustry.setGdp_percent(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)
            self.citytertiaryindustry.setPractitioners_percent(table.cell(row_index, self.TitleList.index(self.TitleTuple[4])).value)
            self.citytertiaryindustry.setUnit(table.cell(row_index, self.TitleList.index(self.TitleList[3])).value)
            self.citytertiaryindustry.setYear(table.cell(row_index, self.TitleList.index(self.TitleList[1])).value)
            self.citytertiaryindustry.setGdpsource(table.cell(row_index, self.TitleList.index(self.TitleList[5])).value)
            self.citytertiaryindustry.setPractitionerssource(table.cell(row_index, self.TitleList.index(self.TitleList[6])).value)

        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:

            paramList = (self.citytertiaryindustry.getCity(), self.citytertiaryindustry.getGdp_percent(), self.citytertiaryindustry.getPractitioners_percent(),
                         self.citytertiaryindustry.getUnit(), self.citytertiaryindustry.getYear(), self.citytertiaryindustry.getGdpsource(),
                         self.citytertiaryindustry.getPractitionerssource())
            result = self.mysqlconnect.cursor.callproc('sp_INsert_statistics_citytertiaryindustry', paramList)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = CityTertiaryIndustryData()
    print mssql.GetData('C:/Users/10509002/Desktop/CDRISBI/CityTertiaryIndustry.xlsx')