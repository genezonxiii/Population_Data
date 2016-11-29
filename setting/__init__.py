# -*-  coding: utf-8  -*-
__author__ = '10409003'

class Config:
    global dbServer,dbUser,dbPwd,dbName
    # �]�w MSSQL�s�u
    def __init__(self):
        self.dbServer = '192.168.112.155'
        self.dbUser = 'sa'
        self.dbPwd = 'Admin123!'
        self.dbName='CDRI-SIIS'


class Config_2:
    global dbServer,dbUser,dbPwd,dbName
    global mgHost,mgPort,mgDB,mgCollection
    global path
    # �]�w MYSQL�s�u
    def __init__(self):
        self.dbServer = '192.168.112.164'
        self.dbUser = 'root'
        self.dbPwd = 'admin123'
        self.dbName='cdri'
        self.path='/data/cdriqrcode/'
        
        #Mongodb �s�u
        self.mgHost='192.168.112.164'
        self.mgPort=27017
        self.mgDB='db_product4'
        self.mgCollection='co_eatapple'