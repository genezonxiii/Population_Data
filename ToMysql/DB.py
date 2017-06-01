# -*-  coding: utf-8  -*-
#__author__ = '10509002'
import logging
import json
import xlrd
from ToMysql import ToMysql
from ToMysql import DB

logger = logging.getLogger(__name__)

class DBData():
    Data = None
    mysqlconnect = None
    processName = None
    db = None


    # 預期要找出欄位的索引位置的欄位名稱
    TitleTuple = (u'城市', u'商圈', u'人流與顧客結構', u'市場地位', u'商業輻射範圍',
                  u'商圈通達性', u'常住人口增長率', u'人均可支配所得增長率', u'人均可支配收入', u'家庭人均消費支出',
                  u'臨街平均租金', u'百貨商場平均租金', u'職工平均工資', u'五險一金', u'商業營業面積',
                  u'地域範圍', u'經度', u'緯度', u'經營成本')
    TitleList = []

    def __init__(self):
        # mysql connector object
        self.mysqlconnect = ToMysql()
        self.mysqlconnect.connect()
        self.processName = "DB_Data"

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
                self.db = DB()
                # Parser Data from xls
                self.parserData(table, row_index)
                # insert or update table tb_product
                self.updateDB_Product()
                self.db = None

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
            self.db.setCity(table.cell(row_index, self.TitleList.index(self.TitleTuple[0])).value)
            self.db.setBD(table.cell(row_index, self.TitleList.index(self.TitleTuple[1])).value)
            self.db.setPopulation(table.cell(row_index, self.TitleList.index(self.TitleTuple[2])).value)
            self.db.setStatus(table.cell(row_index, self.TitleList.index(self.TitleTuple[3])).value)
            self.db.setRadiation(table.cell(row_index, self.TitleList.index(self.TitleTuple[4])).value)
            self.db.setTraffic(table.cell(row_index, self.TitleList.index(self.TitleTuple[5])).value)
            self.db.setResident(table.cell(row_index, self.TitleList.index(self.TitleTuple[6])).value)
            self.db.setIncome(table.cell(row_index, self.TitleList.index(self.TitleTuple[7])).value)
            self.db.setRevenue(table.cell(row_index, self.TitleList.index(self.TitleTuple[8])).value)
            self.db.setExpenditur(table.cell(row_index, self.TitleList.index(self.TitleTuple[9])).value)
            self.db.setNearstreet(table.cell(row_index, self.TitleList.index(self.TitleTuple[10])).value)
            self.db.setDept_store(table.cell(row_index, self.TitleList.index(self.TitleTuple[11])).value)
            self.db.setWorking_po(table.cell(row_index, self.TitleList.index(self.TitleTuple[12])).value)
            self.db.setRisk(table.cell(row_index, self.TitleList.index(self.TitleTuple[13])).value)
            self.db.setArea(table.cell(row_index, self.TitleList.index(self.TitleTuple[14])).value)
            self.db.setGeometry(table.cell(row_index, self.TitleList.index(self.TitleTuple[15])).value)
            self.db.setLng(table.cell(row_index, self.TitleList.index(self.TitleTuple[16])).value)
            self.db.setLat(table.cell(row_index, self.TitleList.index(self.TitleTuple[17])).value)
            self.db.setBusiness_cost(table.cell(row_index, self.TitleList.index(self.TitleTuple[18])).value)
            self.db.setMemo('')

        except Exception as e :
            print e.message
            logging.error(e.message)

    def updateDB_Product(self):
        try:

            paramList = (self.db.getCity(), self.db.getBD(), self.db.getPopulation(), self.db.getStatus(),
                         self.db.getRadiation(), self.db.getTraffic(), self.db.getResident(),self.db.getIncome(),self.db.getRevenue(),
                         self.db.getExpenditur(), self.db.getNearstreet(), self.db.getDept_store(), self.db.getWorking_po(),
                         self.db.getRisk(), self.db.getArea(), self.db.getGeometry(), self.db.getLng(), self.db.getLat(),
                         self.db.getBusiness_cost(), self.db.getMemo())
            result = self.mysqlconnect.cursor.callproc('sp_insert_DB', paramList)

        except Exception as e :
            print e.message
            logging.error(e.message)
            raise

if __name__=='__main__':
    mssql = DBData()
    print mssql.GetData('C:/Users/10509002/Desktop/DB.xlsx')