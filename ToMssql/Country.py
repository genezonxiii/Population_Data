# -*-  coding: utf-8  -*-
__author__ = '10409003'
import pymssql
from setting import Config
import xlrd

class Country:
    def __init__(self):
        pass
    def GetData(self,path):
        config=Config()
        conn = pymssql.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd, database=config.dbName)
        cur = conn.cursor()
        workbook = xlrd.open_workbook(path)
        sheet = workbook.sheet_by_index(0)
        for rows in range(1, sheet.nrows):
            arr = []
            for cols in range(3):
                arr.append(self.finaldata(sheet.cell_value(rows, cols)))
            cur.execute(
                "INSERT INTO dbo.country VALUES (%s, %s, %s)",
                tuple(arr)
            )
        conn.commit()
        return 'success'

    def finaldata(self, data):
        if (data == '' or data == 'NULL'):
            return None
        else:
            return data