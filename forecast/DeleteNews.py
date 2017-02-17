# -*-  coding: utf-8  -*-
# __author__ = '10408001'
from setting import Config_2
from pymongo import MongoClient
from datetime import datetime,timedelta

class DelNews():
    def __init__(self):
        pass

    def dropNews(self):
        try:
            config = Config_2()
            client = MongoClient(config.mgHost, config.mgPort)
            db = client[config.mgDB]
            collect = db[config.mgCollection]
            d = datetime.today() + timedelta(days=-15)
            # d = datetime(2017,02,17)
            # print d
            # for row in collect.find({"TimeStamp":{"$lt": d}}) :
            #     print row
            collect.remove({"TimeStamp":{"$lt": d}})
        except Exception as e:
            print e.message
            raise

if __name__ == "__main__":
    dn = DelNews()
    dn.dropNews()