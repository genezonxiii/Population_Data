# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql,Citycivilcar
from ToMysql.City import CityData

logger = logging.getLogger(__name__)

class CityCivilCarData():
    Data = None
    mysqlconnect = None
    processName = None
    # name, unit, year = None,None,None
    # cargo, passenger, cargosource, passsource = None,None,None,None
    citycivilcar = None

    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'城市', u'單位', u'年份', u'民用載貨汽車擁有量',u'民用載客汽車擁有量',
                  u'載貨汽車資料來源', u'載客汽車資料來源')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "CityCivilCar_Data"

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
                self.citycivilcar = Citycivilcar()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.citycivilcar = None

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
            self.citycivilcar.setCity(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.citycivilcar.setUnit(table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value)
            self.citycivilcar.setYear(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)
            self.citycivilcar.setCarrygoods(table.cell(row_index, self.TitleList.index(self.TitleList[3])).value)
            self.citycivilcar.setCarrypassenger(table.cell(row_index, self.TitleList.index(self.TitleList[4])).value)
            self.citycivilcar.setCarrygoods_Source(table.cell(row_index, self.TitleList.index(self.TitleList[5])).value)
            self.citycivilcar.setCarrypassenger_Source(table.cell(row_index, self.TitleList.index(self.TitleList[6])).value)

        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:
            # SalestrSQL = """INSERT INTO tb_Statistics_citycivilcar
            # (City,Unit,Year,CarryGoods,CarryPassenger,CarryGoods_Source,CarryPassenger_Source)
            # VALUES(%s,%s,%s,%s,%s,%s,%s)"""
            paramList = (self.citycivilcar.getCity(), self.citycivilcar.getUnit(), self.citycivilcar.getYear(), self.citycivilcar.getCarrygoods(),
                      self.citycivilcar.getCarrypassenger(), self.citycivilcar.getCarrygoods_Source(), self.citycivilcar.getCarrypassenger_Source())
            result = self.mysqlconnect.cursor.callproc('sp_INsert_statistics_citycivilcar', paramList)
            # self.mysqlconnect.cursor.execute(SalestrSQL, Values)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = CityCivilCarData()
    print mssql.GetData('C:/Users/10509002/Desktop/CDRISBI/CityCivilCar.xlsx')