# -*-  coding: utf-8  -*-
__author__ = '10409003'

class Config:
    global dbServer,dbUser,dbPwd,dbName,SIIS_User,SIIS_Pwd,SIIS_db
    #  51 MSSQL 連線資訊
    def __init__(self):
        self.dbServer = '61.218.8.51'
        self.dbUser = 'sa'
        self.dbPwd = 'Admin123!'
        self.dbName = 'CDRI-SIIS'
        self.SIIS_User = 'cdri'
        self.SIIS_Pwd = 'cdriadmin'
        self.SIIS_db = 'CDRI'

class Config_2:
    global dbServer,dbUser,dbPwd,dbName
    global mgHost,mgPort,mgDB,mgCollection
    global path , newsUrl,IndustryDoc,Sender,SMTP
    #  MYSQL 連線資訊
    def __init__(self):
        self.dbServer = '192.168.112.164'
        self.dbUser = 'root'
        self.dbPwd = 'admin123'
        self.dbName='cdri'
        self.path='/data/cdriqrcode/'
        # 電子報
        self.newsUrl = 'http://sbi1.cdri.org.tw/news/'
        self.IndustryDoc = 'http://192.168.112.164/IndustryDoc/'
        self.Sender = 'robinkuo@pershing.com.tw'
        self.SMTP = 'ms1.pershing.com.tw'
        # self.IndustryDoc = 'http://sbi1.cdri.org.tw/IndustryDoc/'
        # self.dbServer = 'localhost'
        # self.dbUser = 'root'
        # self.dbPwd = 'mysql'
        # self.dbName = 'cdri'
        # self.path = '/data/cdriqrcode/'

        # self.dbServer = 'localhost'
        # self.dbUser = 'root'
        # self.dbPwd = 'admin123'
        # self.dbName = 'sbi'
        # self.path = '/data/cdriqrcode/'
        
        #Mongodb 連線資訊
        self.mgHost='192.168.112.164'
        self.mgPort=27017
        self.mgDB='db_product4'
        self.mgCollection='co_eatapple'