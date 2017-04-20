# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql
from ToMysql import Citypractitioners

logger = logging.getLogger(__name__)

class CityPractitionersData():
    Data = None
    mysqlconnect = None
    processName = None
    citypractitioners = None


    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'城市', u'單位', u'年份', u'從業人員數',u'城鎮從業人員數',
                  u'專業技術人員數', u'城鎮私營企業從業人員數', u'城鎮外商投資企業從業人數', u'從業人員數資料來源',
                  u'城鎮從業人員數資料來源', u'專業技術人員數資料來源', u'城鎮私營企業從業人員數資料來源',
                  u'城鎮外商投資企業從業人數資料來源')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "CityPractitioners_Data"

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
                self.citypractitioners = Citypractitioners()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.citypractitioners = None

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
            self.citypractitioners.setCity(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.citypractitioners.setYear(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)
            self.citypractitioners.setUnit(table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value)
            self.citypractitioners.setTotal(table.cell(row_index, self.TitleList.index(self.TitleList[3])).value)
            self.citypractitioners.setTown(table.cell(row_index, self.TitleList.index(self.TitleList[4])).value)
            self.citypractitioners.setSpeciality(table.cell(row_index, self.TitleList.index(self.TitleList[5])).value)
            self.citypractitioners.setTownprivate(table.cell(row_index, self.TitleList.index(self.TitleList[6])).value)
            self.citypractitioners.setTownforeign(table.cell(row_index, self.TitleList.index(self.TitleList[7])).value)
            self.citypractitioners.setTotal_Source(table.cell(row_index, self.TitleList.index(self.TitleList[8])).value)
            self.citypractitioners.setTown_Source(table.cell(row_index, self.TitleList.index(self.TitleList[9])).value)
            self.citypractitioners.setSpeciality_Source(table.cell(row_index, self.TitleList.index(self.TitleList[10])).value)
            self.citypractitioners.setTownprivate_Source(table.cell(row_index, self.TitleList.index(self.TitleList[11])).value)
            self.citypractitioners.setTownforeign_Source(table.cell(row_index, self.TitleList.index(self.TitleList[12])).value)

        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:

            paramList = (self.citypractitioners.getCity(), self.citypractitioners.getYear(), self.citypractitioners.getUnit(),
                         self.citypractitioners.getTotal(), self.citypractitioners.getTown(), self.citypractitioners.getSpeciality(),
                         self.citypractitioners.getTownprivate(), self.citypractitioners.getTownforeign(), self.citypractitioners.getTotal_Source(),
                         self.citypractitioners.getTown_Source(), self.citypractitioners.getSpeciality_Source(),self.citypractitioners.getTownprivate_Source(),
                         self.citypractitioners.getTownforeign_Source())
            result = self.mysqlconnect.cursor.callproc('sp_INsert_statistics_citypractitioners', paramList)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = CityPractitionersData()
    print mssql.GetData('C:/Users/10509002/Desktop/CDRISBI/CityPractitioners.xlsx')