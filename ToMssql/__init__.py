import pymssql
from setting import Config
import xlrd

class City:
    def __init__(self):
        pass
    def GetData(self,path):
        config=Config()
        conn = pymssql.connect(host=config.dbServer, user=config.dbUser, password=config.dbPwd, database=config.dbName)
        cur = conn.cursor()
        data = xlrd.open_workbook(path)
        table = data.sheets()[0]
        num_cols = table.ncols
        for row_index in range(1, table.nrows):
            for col_index in range(0, num_cols):
                #idCity = table.cell(row_index, 0).value
                Name = table.cell(row_index, 1).value
                latitude = table.cell(row_index, 2).value
                Longitude = table.cell(row_index, 3).value
            print Name,latitude,Longitude
            SalestrSQL = """INSERT INTO dbo.city (Name,latitude,Longitude) VALUES(%s,%s,%s)"""
            Values=(Name, latitude, Longitude)
            cur.execute(SalestrSQL, Values)
        conn.commit()




if __name__=='__main__':
    mssql = City()
    data = mssql.GetData("C:/Users/10409003/Desktop/CDRISBI/City.xlsx")