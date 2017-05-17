# -*-  coding: utf-8  -*-
#__author__ = '10509002'

from mysql.connector.cursor import MySQLCursor
import mysql.connector
from mysql.connector import errorcode
import datetime
import logging
from decimal import *

logger = logging.getLogger(__name__)

class ToMysql():
    host = '192.168.112.164'
    # host = 'localhost'
    #host = 'www.a-ber.com.tw'
    database = 'cdri'
    user = 'root'
    password = 'admin123'
    #host = '192.168.112.175'
    #database = 'db_virutalbusiness'
    #user = 'root'
    # password = 'mysql'

    def __init__(self):
        pass

    def connect(self):
        try:
            self.db = mysql.connector.connect(user=self.user, password=self.password,
                              host=self.host,database=self.database)
            self.db.commit()
        except mysql.connector.error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_error:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_error:
                print("Database does not exist")
            else:
                print(err)
        self.cursor= MySQLCursor(self.db)

    def setDatabase(self,dbname):
        self.database=dbname
        pass

    def setTable(self,tbname):
        self.tablename=tbname
        pass

    def setuser(self,username,pw):
        self.user=username
        self.password=pw
        pass

    def dbClose(self):
        self.cursor.close()

class convertType():
    def __init__(self):
        pass

    def ToDateTime(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return None
            else:
                dateObj=datetime.datetime.strptime(str(value),'%Y/%m/%d %H:%M')
                return dateObj
        except Exception as e:
            logger.error(e.message)

    def ToDateTimeMDHM(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return None
            else:
                dateObj=datetime.datetime.strptime(str(value),'%m/%d %H:%M')
                return dateObj
        except Exception as e:
            logger.error(e.message)

    def ToDateTimeYYYYMMDD(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return None
            else:
                dateObj=datetime.datetime.strptime(str(value),'%Y/%m/%d')
                return dateObj
        except Exception as e:
            logger.error(e.message)

    def ToDateTimeYYYYMMDDHHMM(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return None
            else:
                dateObj=datetime.datetime.strptime(str(value),'%Y/%m/%d/%H/%M')
                return dateObj
        except Exception as e:
            logger.error(e.message)

    def ToDateTimeYMD(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return None
            else:
                dateObj=datetime.datetime.strptime(str(value),'%Y-%m-%d')
                return dateObj
        except Exception as e:
            logger.error(e.message)

    def ToDateTimeYMDHM(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return None
            else:
                dateObj=datetime.datetime.strptime(str(value),'%Y-%m-%d %H:%M')
                return dateObj
        except Exception as e:
            logger.error(e.message)

    def ToDateTimeYMDHMS(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return None
            else:
                dateObj=datetime.datetime.strptime(str(value),'%Y-%m-%d %H:%M:%S')
                return dateObj
        except Exception as e:
            logger.error(e.message)

    def ToDateTimeYMDHMSF(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return None
            else:
                dateObj=datetime.datetime.strptime(str(value),'%Y-%m-%d %H:%M:%S.%f')
                return dateObj
        except Exception as e:
            logger.error(e.message)

    def ToDateTimeYYYYMMDD_float(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return None
            else:
                ct = convertType()
                dateObj=datetime.datetime.strptime(ct.getdate(value),'%Y/%m/%d')
                return dateObj
        except Exception as e:
            logger.error(e.message)

    def ToDateTimeYMDHMS_float(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return None
            else:
                ct = convertType()
                dateObj=datetime.datetime.strptime(ct.xldate_to_datetime(value),"%Y-%m-%d %H:%M:%S")
                return dateObj
        except Exception as e:
            logger.error(e.message)

    def ToDateTime2(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return None
            else:
                dateObj=datetime.datetime.strptime(str(value),'%Y/%m/%d/%H/%M')
                return dateObj
        except Exception as e:
            logger.error(e.message)

    def getdate(self, date):
        __s_date = datetime.date(1899, 12, 31).toordinal() - 1
        if isinstance(date, float):
            date = int(date)
        d = datetime.date.fromordinal(__s_date + date)
        return d.strftime("%Y/%m/%d")

    def xldate_to_datetime(self,xldate):
        tempDate = datetime.datetime(1899, 12, 30)
        deltaDays = datetime.timedelta(days=int(xldate))
        secs = (int((xldate % 1) * 86400) - 60)
        detlaSeconds = datetime.timedelta(seconds=secs)
        TheTime = (tempDate + deltaDays + detlaSeconds)
        return TheTime.strftime("%Y-%m-%d %H:%M:%S")

    def ToInt(self,value):
        try:
            if value== None :
                return 0
            elif value=='':
                return 0
            else:
                return int(float(value))
        except Exception as e:
            logger.error(e.message)

    def ToFloat(self,value):
        try:
            if value== None :
                return 0.0
            elif value=='':
                return 0.0
            else:
                return float(value)
        except Exception as e:
            logger.error(e.message)

    def ToDecimal(self,value):
        try:
            if value == None:
                return None
            elif value == '':
                return None
            else :
                return Decimal(value)
        except Exception as e:
            logger.error(e.message)

    def ToString(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return ''
            else:
                return str(value)
        except Exception as e:
            logger.error(e.message)

    def ToStringNoEncode(self,value):
        try:
            if value== None :
                return None
            elif value=='':
                return ''
            else:
                return value
        except Exception as e:
            logger.error(e.message)

    def ToBoolean(self,value):
        try:
            if value == True:
                return True
            else:
                return False
        except Exception as e :
            logger.error(e.message)

class City():
    p_name, p_latitude, p_longitude = None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setName(self,value):
        self.p_name = self.convert.ToString(value.encode('utf-8'))

    def setLatitude(self,value):
        self.p_latitude = self.convert.ToStringNoEncode(value)

    def setLongitude(self,value):
        self.p_longitude = self.convert.ToStringNoEncode(value)

    def getName(self):
        return self.p_name

    def getLatitude(self):
        return self.p_latitude

    def getLongitude(self):
        return self.p_longitude


class Citycivilcar():
    p_city, p_unit, p_year, p_carrygoods, p_carrypassenger = None, None, None, None, None
    p_carrygoods_source, p_carrypassenger_source = None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setCarrygoods(self,value):
        self.p_carrygoods = self.convert.ToDecimal(value)

    def setCarrypassenger(self,value):
        self.p_carrypassenger = self.convert.ToDecimal(value)

    def setCarrygoods_Source(self,value):
        self.p_carrygoods_source = self.convert.ToString(value.encode('utf-8'))

    def setCarrypassenger_Source(self,value):
        self.p_carrypassenger_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getUnit(self):
        return self.p_unit

    def getYear(self):
        return self.p_year

    def getCarrygoods(self):
        return self.p_carrygoods

    def getCarrypassenger(self):
        return self.p_carrypassenger

    def getCarrygoods_Source(self):
        return self.p_carrygoods_source

    def getCarrypassenger_Source(self):
        return self.p_carrypassenger_source

class CityConsumptionExpenditure():
    p_city, p_unit, p_year, p_total, p_food = None, None, None, None, None
    p_clothes, p_live, p_trafficcommu, p_education, p_lifelihood = None, None, None, None, None
    p_healthcare, p_household, p_total_source, p_food_source, p_clothes_source = None, None, None, None, None
    p_live_source, p_trafficcommu_source, p_education_source, p_lifelihood_source, p_healthcare_source = None, None, None, None, None
    p_household_source = None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setTotal(self,value):
        self.p_total = self.convert.ToDecimal(value)

    def setFood(self,value):
        self.p_food = self.convert.ToDecimal(value)

    def setClothes(self,value):
        self.p_clothes = self.convert.ToDecimal(value)

    def setLive(self,value):
        self.p_live = self.convert.ToDecimal(value)

    def setTrafficcommu(self,value):
        self.p_trafficcommu = self.convert.ToDecimal(value)

    def setEducation(self,value):
        self.p_education = self.convert.ToDecimal(value)

    def setLifelihood(self,value):
        self.p_lifelihood = self.convert.ToDecimal(value)

    def setHealthcare(self,value):
        self.p_healthcare = self.convert.ToDecimal(value)

    def setHousehold(self,value):
        self.p_household = self.convert.ToDecimal(value)

    def setTotal_Source(self,value):
        self.p_total_source = self.convert.ToString(value.encode('utf-8'))

    def setFood_Source(self,value):
        self.p_food_source = self.convert.ToString(value.encode('utf-8'))

    def setClothes_Source(self,value):
        self.p_clothes_source = self.convert.ToString(value.encode('utf-8'))

    def setLive_Source(self,value):
        self.p_live_source = self.convert.ToString(value.encode('utf-8'))

    def setTrafficcommu_Source(self,value):
        self.p_trafficcommu_source = self.convert.ToString(value.encode('utf-8'))

    def setEducation_Source(self,value):
        self.p_education_source = self.convert.ToString(value.encode('utf-8'))

    def setLifelihood_Source(self,value):
        self.p_lifelihood_source = self.convert.ToString(value.encode('utf-8'))

    def setHealthcare_Source(self,value):
        self.p_healthcare_source = self.convert.ToString(value.encode('utf-8'))

    def setHousehold_Source(self,value):
        self.p_household_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getUnit(self):
        return self.p_unit

    def getYear(self):
        return self.p_year

    def getTotal(self):
        return self.p_total

    def getFood(self):
        return self.p_food

    def getClothes(self):
        return self.p_clothes

    def getLive(self):
        return self.p_live

    def getTrafficcommu(self):
        return self.p_trafficcommu

    def getEducation(self):
        return self.p_education

    def getLifelihood(self):
        return self.p_lifelihood

    def getHealthcare(self):
        return self.p_healthcare

    def getHousehold(self):
        return self.p_household

    def getTotal_Source(self):
        return self.p_total_source

    def getFood_Source(self):
        return self.p_food_source

    def getClothes_Source(self):
        return self.p_clothes_source

    def getLive_Source(self):
        return self.p_live_source

    def getTrafficcommu_Source(self):
        return self.p_trafficcommu_source

    def getEducation_Source(self):
        return self.p_education_source

    def getLifelihood_Source(self):
        return self.p_lifelihood_source

    def getHealthcare_Source(self):
        return self.p_healthcare_source

    def getHousehold_Source(self):
        return self.p_household_source

class Cityestateavgsale():
    p_city, p_unit, p_year, p_commodity, p_residentialcommodity = None, None, None, None, None
    p_commodity_source, p_residentialcommodity_source = None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setCommodity(self,value):
        self.p_commodity = self.convert.ToDecimal(value)

    def setResidentialcommodity(self,value):
        self.p_residentialcommodity = self.convert.ToDecimal(value)

    def setCommodity_Source(self,value):
        self.p_commodity_source = self.convert.ToString(value.encode('utf-8'))

    def setResidentialcommodity_Source(self,value):
        self.p_residentialcommodity_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getUnit(self):
        return self.p_unit

    def getYear(self):
        return self.p_year

    def getCommodity(self):
        return self.p_commodity

    def getResidentialcommodity(self):
        return self.p_residentialcommodity

    def getCommodity_Source(self):
        return self.p_commodity_source

    def getResidentialcommodity_Source(self):
        return self.p_residentialcommodity_source

class Cityestatecompletion():
    p_city, p_unit, p_year, p_commerce, p_residential = None, None, None, None, None
    p_commerce_source, p_residential_source = None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setCommerce(self,value):
        self.p_commerce = self.convert.ToDecimal(value)

    def setResidential(self,value):
        self.p_residential = self.convert.ToDecimal(value)

    def setCommerce_Source(self,value):
        self.p_commerce_source = self.convert.ToString(value.encode('utf-8'))

    def setResidential_Source(self,value):
        self.p_residential_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getUnit(self):
        return self.p_unit

    def getYear(self):
        return self.p_year

    def getCommerce(self):
        return self.p_commerce

    def getResidential(self):
        return self.p_residential

    def getCommerce_Source(self):
        return self.p_commerce_source

    def getResidential_Source(self):
        return self.p_residential_source

class Cityestatesaleamount():
    p_city, p_unit, p_year, p_commerce, p_office = None, None, None, None, None
    p_residential, p_commodity, p_commerce_source, p_office_source, p_residential_source = None, None, None, None, None
    p_commodity_source = None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setCommerce(self,value):
        self.p_commerce = self.convert.ToDecimal(value)

    def setOffice(self,value):
        self.p_office = self.convert.ToDecimal(value)

    def setResidential(self,value):
        self.p_residential = self.convert.ToDecimal(value)

    def setCommodity(self,value):
        self.p_commodity = self.convert.ToDecimal(value)

    def setCommerce_Source(self,value):
        self.p_commerce_source = self.convert.ToString(value.encode('utf-8'))

    def setOffice_Source(self,value):
        self.p_office_source = self.convert.ToString(value.encode('utf-8'))

    def setResidential_Source(self,value):
        self.p_residential_source = self.convert.ToString(value.encode('utf-8'))

    def setCommodity_Source(self,value):
        self.p_commodity_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getUnit(self):
        return self.p_unit

    def getYear(self):
        return self.p_year

    def getCommerce(self):
        return self.p_commerce

    def getOffice(self):
        return self.p_office

    def getResidential(self):
        return self.p_residential

    def getCommodity(self):
        return self.p_commodity

    def getCommerce_Source(self):
        return self.p_commerce_source

    def getOffice_Source(self):
        return self.p_office_source

    def getResidential_Source(self):
        return self.p_residential_source

    def getCommodity_Source(self):
        return self.p_commodity_source

class Cityestatesalearea():
    p_city, p_unit, p_year, p_commerce, p_office = None, None, None, None, None
    p_residential, p_commodity, p_commerce_source, p_office_source, p_residential_source = None, None, None, None, None
    p_commodity_source = None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setCommerce(self,value):
        self.p_commerce = self.convert.ToDecimal(value)

    def setOffice(self,value):
        self.p_office = self.convert.ToDecimal(value)

    def setResidential(self,value):
        self.p_residential = self.convert.ToDecimal(value)

    def setCommodity(self,value):
        self.p_commodity = self.convert.ToDecimal(value)

    def setCommerce_Source(self,value):
        self.p_commerce_source = self.convert.ToString(value.encode('utf-8'))

    def setOffice_Source(self,value):
        self.p_office_source = self.convert.ToString(value.encode('utf-8'))

    def setResidential_Source(self,value):
        self.p_residential_source = self.convert.ToString(value.encode('utf-8'))

    def setCommodity_Source(self,value):
        self.p_commodity_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getUnit(self):
        return self.p_unit

    def getYear(self):
        return self.p_year

    def getCommerce(self):
        return self.p_commerce

    def getOffice(self):
        return self.p_office

    def getResidential(self):
        return self.p_residential

    def getCommodity(self):
        return self.p_commodity

    def getCommerce_Source(self):
        return self.p_commerce_source

    def getOffice_Source(self):
        return self.p_office_source

    def getResidential_Source(self):
        return self.p_residential_source

    def getCommodity_Source(self):
        return self.p_commodity_source

class Citygender():
    p_city, p_male, p_female, p_unit, p_year = None, None, None, None, None
    p_malesource, p_femalesource = None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setMale(self,value):
        self.p_male = self.convert.ToDecimal(value)

    def setFemale(self,value):
        self.p_female = self.convert.ToDecimal(value)

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setMalesource(self,value):
        self.p_malesource = self.convert.ToString(value.encode('utf-8'))

    def setFemalesource(self,value):
        self.p_femalesource = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getMale(self):
        return self.p_male

    def getFemale(self):
        return self.p_female

    def getUnit(self):
        return self.p_unit

    def getYear(self):
        return self.p_year

    def getMalesource(self):
        return self.p_malesource

    def getFemalesource(self):
        return self.p_femalesource

class Citygoodstraffic():
    p_city, p_unit, p_year, p_highway, p_civilaviation = None, None, None, None, None
    p_watertransport, p_railroad, p_highway_source, p_civilaviation_source, p_watertransport_source = None, None, None, None, None
    p_railroad_source = None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setHighway(self,value):
        self.p_highway = self.convert.ToDecimal(value)

    def setCivilaviation(self,value):
        self.p_civilaviation = self.convert.ToDecimal(value)

    def setWatertransport(self,value):
        self.p_watertransport = self.convert.ToDecimal(value)

    def setRailroad(self,value):
        self.p_railroad = self.convert.ToDecimal(value)

    def setHighway_Source(self,value):
        self.p_highway_source = self.convert.ToString(value.encode('utf-8'))

    def setCivilaviation_Source(self,value):
        self.p_civilaviation_source = self.convert.ToString(value.encode('utf-8'))

    def setWatertransport_Source(self,value):
        self.p_watertransport_source = self.convert.ToString(value.encode('utf-8'))

    def setRailroad_Source(self,value):
        self.p_railroad_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getUnit(self):
        return self.p_unit

    def getYear(self):
        return self.p_year

    def getHighway(self):
        return self.p_highway

    def getCivilaviation(self):
        return self.p_civilaviation

    def getWatertransport(self):
        return self.p_watertransport

    def getRailroad(self):
        return self.p_railroad

    def getHighway_Source(self):
        return self.p_highway_source

    def getCivilaviation_Source(self):
        return self.p_civilaviation_source

    def getWatertransport_Source(self):
        return self.p_watertransport_source

    def getRailroad_Source(self):
        return self.p_railroad_source

class Cityincome():
    p_city, p_year, p_unit, p_staff, p_inpost = None, None, None, None, None
    p_town, p_stateunit, p_otherunit, p_staff_source, p_inpost_source = None, None, None, None, None
    p_town_source, p_stateunit_source, p_otherunit_source = None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setStaff(self,value):
        self.p_staff = self.convert.ToDecimal(value)

    def setInpost(self,value):
        self.p_inpost = self.convert.ToDecimal(value)

    def setTown(self,value):
        self.p_town = self.convert.ToDecimal(value)

    def setStatunit(self,value):
        self.p_stateunit = self.convert.ToDecimal(value)

    def setOtherunit(self,value):
        self.p_otherunit = self.convert.ToDecimal(value)

    def setStaff_Source(self,value):
        self.p_staff_source = self.convert.ToString(value.encode('utf-8'))

    def setInpost_Source(self,value):
        self.p_inpost_source = self.convert.ToString(value.encode('utf-8'))

    def setTown_Source(self,value):
        self.p_town_source = self.convert.ToString(value.encode('utf-8'))

    def setStateunit_Source(self,value):
        self.p_stateunit_source = self.convert.ToString(value.encode('utf-8'))

    def setOtherunit_Source(self,value):
        self.p_otherunit_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getYear(self):
        return self.p_year

    def getUnit(self):
        return self.p_unit

    def getStaff(self):
        return self.p_staff

    def getInpost(self):
        return self.p_inpost

    def getTown(self):
        return self.p_town

    def getStatunit(self):
        return self.p_stateunit

    def getOtherunit(self):
        return self.p_otherunit

    def getStaff_Source(self):
        return self.p_staff_source

    def getInpost_Source(self):
        return self.p_inpost_source

    def getTown_Source(self):
        return self.p_town_source

    def getStateunit_Source(self):
        return self.p_stateunit_source

    def getOtherunit_Source(self):
        return self.p_otherunit_source

class Citypassengertraffic():
    p_city, p_unit, p_year, p_highway, p_civilaviation = None, None, None, None, None
    p_watertransport, p_railroad, p_highway_source, p_civilaviation_source, p_watertransport_source = None, None, None, None, None
    p_railroad_source = None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setHighway(self,value):
        self.p_highway = self.convert.ToDecimal(value)

    def setCivilaviation(self,value):
        self.p_civilaviation = self.convert.ToDecimal(value)

    def setWatertransport(self,value):
        self.p_watertransport = self.convert.ToDecimal(value)

    def setRailroad(self,value):
        self.p_railroad = self.convert.ToDecimal(value)

    def setHighway_Source(self,value):
        self.p_highway_source = self.convert.ToString(value.encode('utf-8'))

    def setCivilaviation_Source(self,value):
        self.p_civilaviation_source = self.convert.ToString(value.encode('utf-8'))

    def setWatertransport_Source(self,value):
        self.p_watertransport_source = self.convert.ToString(value.encode('utf-8'))

    def setRailroad_Source(self,value):
        self.p_railroad_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getUnit(self):
        return self.p_unit

    def getYear(self):
        return self.p_year

    def getHighway(self):
        return self.p_highway

    def getCivilaviation(self):
        return self.p_civilaviation

    def getWatertransport(self):
        return self.p_watertransport

    def getRailroad(self):
        return self.p_railroad

    def getHighway_Source(self):
        return self.p_highway_source

    def getCivilaviation_Source(self):
        return self.p_civilaviation_source

    def getWatertransport_Source(self):
        return self.p_watertransport_source

    def getRailroad_Source(self):
        return self.p_railroad_source

class Citypractitioners():
    p_city, p_year, p_unit, p_total, p_town = None, None, None, None, None
    p_speciality, p_townprivate, p_townforeign, p_total_source, p_town_source = None, None, None, None, None
    p_speciality_source, p_townprivate_source, p_townforeign_source = None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setTotal(self,value):
        self.p_total = self.convert.ToDecimal(value)

    def setTown(self,value):
        self.p_town = self.convert.ToDecimal(value)

    def setSpeciality(self,value):
        self.p_speciality = self.convert.ToDecimal(value)

    def setTownprivate(self,value):
        self.p_townprivate = self.convert.ToDecimal(value)

    def setTownforeign(self,value):
        self.p_townforeign = self.convert.ToDecimal(value)

    def setTotal_Source(self,value):
        self.p_total_source = self.convert.ToString(value.encode('utf-8'))

    def setTown_Source(self,value):
        self.p_town_source = self.convert.ToString(value.encode('utf-8'))

    def setSpeciality_Source(self,value):
        self.p_speciality_source = self.convert.ToString(value.encode('utf-8'))

    def setTownprivate_Source(self,value):
        self.p_townprivate_source = self.convert.ToString(value.encode('utf-8'))

    def setTownforeign_Source(self,value):
        self.p_townforeign_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getYear(self):
        return self.p_year

    def getUnit(self):
        return self.p_unit

    def getTotal(self):
        return self.p_total

    def getTown(self):
        return self.p_town

    def getSpeciality(self):
        return self.p_speciality

    def getTownprivate(self):
        return self.p_townprivate

    def getTownforeign(self):
        return self.p_townforeign

    def getTotal_Source(self):
        return self.p_total_source

    def getTown_Source(self):
        return self.p_town_source

    def getSpeciality_Source(self):
        return self.p_speciality_source

    def getTownprivate_Source(self):
        return self.p_townprivate_source

    def getTownforeign_Source(self):
        return self.p_townforeign_source

class Cityretailexponent():
    p_city, p_year, p_total, p_textile, p_clothing = None, None, None, None, None
    p_cosmetic, p_fuel, p_necessary, p_food, p_drinks = None, None, None, None, None
    p_total_source, p_textile_source, p_clothing_source, p_cosmetic_source, p_fuel_source = None, None, None, None, None
    p_necessary_source, p_food_source, p_drinks_source = None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setTotal(self,value):
        self.p_total = self.convert.ToDecimal(value)

    def setTextile(self,value):
        self.p_textile = self.convert.ToDecimal(value)

    def setClothing(self,value):
        self.p_clothing = self.convert.ToDecimal(value)

    def setCosmetic(self,value):
        self.p_cosmetic = self.convert.ToDecimal(value)

    def setFuel(self,value):
        self.p_fuel = self.convert.ToDecimal(value)

    def setNecessary(self,value):
        self.p_necessary = self.convert.ToDecimal(value)

    def setFood(self,value):
        self.p_food = self.convert.ToDecimal(value)

    def setDrinks(self,value):
        self.p_drinks = self.convert.ToDecimal(value)

    def setTotal_Source(self,value):
        self.p_total_source = self.convert.ToString(value.encode('utf-8'))

    def setTextile_Source(self,value):
        self.p_textile_source = self.convert.ToString(value.encode('utf-8'))

    def setClothing_source(self,value):
        self.p_clothing_source = self.convert.ToString(value.encode('utf-8'))

    def setCosmetic_Source(self,value):
        self.p_cosmetic_source = self.convert.ToString(value.encode('utf-8'))

    def setFuel_Source(self,value):
        self.p_fuel_source = self.convert.ToString(value.encode('utf-8'))

    def setNecessary_Source(self,value):
        self.p_necessary_source = self.convert.ToString(value.encode('utf-8'))

    def setFood_Source(self,value):
        self.p_food_source = self.convert.ToString(value.encode('utf-8'))

    def setDrinks_Source(self,value):
        self.p_drinks_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getYear(self):
        return self.p_year

    def getTotal(self):
        return self.p_total

    def getTextile(self):
        return self.p_textile

    def getClothing(self):
        return self.p_clothing

    def getCosmetic(self):
        return self.p_cosmetic

    def getFuel(self):
        return self.p_fuel

    def getNecessary(self):
        return self.p_necessary

    def getFood(self):
        return self.p_food

    def getDrinks(self):
        return self.p_drinks

    def getTotal_Source(self):
        return self.p_total_source

    def getTextile_Source(self):
        return self.p_textile_source

    def getClothing_source(self):
        return self.p_clothing_source

    def getCosmetic_Source(self):
        return self.p_cosmetic_source

    def getFuel_Source(self):
        return self.p_fuel_source

    def getNecessary_Source(self):
        return self.p_necessary_source

    def getFood_Source(self):
        return self.p_food_source

    def getDrinks_Source(self):
        return self.p_drinks_source

class Citysocialconsume():
    p_city, p_unit, p_year, p_retailsum, p_wholesaleretailsale = None, None, None, None, None
    p_wholesaleretail_retailsum, p_retailsum_source, p_wholesaleretailsale_source, p_wholesaleretail_retailsum_source = None, None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setRetailsum(self,value):
        self.p_retailsum = self.convert.ToDecimal(value)

    def setWholesaleretailsale(self,value):
        self.p_wholesaleretailsale = self.convert.ToDecimal(value)

    def setWholesaleretail_Retailsum(self,value):
        self.p_wholesaleretail_retailsum = self.convert.ToDecimal(value)

    def setRetailsum_Source(self,value):
        self.p_retailsum_source = self.convert.ToString(value.encode('utf-8'))

    def setWholesaleretailsale_Source(self,value):
        self.p_wholesaleretailsale_source = self.convert.ToString(value.encode('utf-8'))

    def setWholesaleretail_Retailsum_Source(self,value):
        self.p_wholesaleretail_retailsum_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getUnit(self):
        return self.p_unit

    def getYear(self):
        return self.p_year

    def getRetailsum(self):
        return self.p_retailsum

    def getWholesaleretailsale(self):
        return self.p_wholesaleretailsale

    def getWholesaleretail_Retailsum(self):
        return self.p_wholesaleretail_retailsum

    def getRetailsum_Source(self):
        return self.p_retailsum_source

    def getWholesaleretailsale_Source(self):
        return self.p_wholesaleretailsale_source

    def getWholesaleretail_Retailsum_Source(self):
        return self.p_wholesaleretail_retailsum_source

class Citystaff():
    p_city, p_year, p_unit, p_inpost, p_stateunit = None, None, None, None, None
    p_inpost_source, p_stateunit_source = None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setInpost(self,value):
        self.p_inpost = self.convert.ToDecimal(value)

    def setStateunit(self,value):
        self.p_stateunit = self.convert.ToDecimal(value)

    def setInpost_Source(self,value):
        self.p_inpost_source = self.convert.ToString(value.encode('utf-8'))

    def setStateunit_Source(self,value):
        self.p_stateunit_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getYear(self):
        return self.p_year

    def getUnit(self):
        return self.p_unit

    def getInpost(self):
        return self.p_inpost

    def getStateunit(self):
        return self.p_stateunit

    def getInpost_Source(self):
        return self.p_inpost_source

    def getStateunit_Source(self):
        return self.p_stateunit_source

class Citytertiaryincrease():
    p_city, p_year, p_amount, p_exponent, p_amount_source = None, None, None, None, None
    p_exponent_source = None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setAmount(self,value):
        self.p_amount = self.convert.ToDecimal(value)

    def setExponent(self,value):
        self.p_exponent = self.convert.ToDecimal(value)

    def setAmount_Source(self,value):
        self.p_amount_source = self.convert.ToString(value.encode('utf-8'))

    def setExponent_Source(self,value):
        self.p_exponent_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getYear(self):
        return self.p_year

    def getAmount(self):
        return self.p_amount

    def getExponent(self):
        return self.p_exponent

    def getAmount_Source(self):
        return self.p_amount_source

    def getExponent_Source(self):
        return self.p_exponent_source

class Citytertiaryindustry():
    p_city, p_gdp_percent, p_practitioners_percent, p_unit, p_year = None, None ,None, None, None
    p_gdpsource, p_practitionerssource = None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setGdp_percent(self,value):
        self.p_gdp_percent = self.convert.ToDecimal(value)

    def setPractitioners_percent(self,value):
        self.p_practitioners_percent = self.convert.ToDecimal(value)

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setGdpsource(self,value):
        self.p_gdpsource = self.convert.ToString(value.encode('utf-8'))

    def setPractitionerssource(self,value):
        self.p_practitionerssource = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getGdp_percent(self):
        return self.p_gdp_percent

    def getPractitioners_percent(self):
        return self.p_practitioners_percent

    def getUnit(self):
        return self.p_unit

    def getYear(self):
        return self.p_year

    def getGdpsource(self):
        return self.p_gdpsource

    def getPractitionerssource(self):
        return self.p_practitionerssource

class Citywholesaleretail():
    p_city, p_unit, p_year, p_retailsum, p_saleforcity = None, None, None, None, None
    p_saleforcounty, p_saleforbelowcounty, p_retailsum_source, p_saleforcity_source, p_saleforcounty_source = None, None, None, None, None
    p_saleforbelowcounty_source = None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToInt(value)

    def setRetailsum(self,value):
        self.p_retailsum = self.convert.ToDecimal(value)

    def setSaleforcity(self,value):
        self.p_saleforcity = self.convert.ToDecimal(value)

    def setSaleforcounty(self,value):
        self.p_saleforcounty = self.convert.ToDecimal(value)

    def setSaleforbelowcounty(self,value):
        self.p_saleforbelowcounty = self.convert.ToDecimal(value)

    def setRetailsum_Source(self,value):
        self.p_retailsum_source = self.convert.ToString(value.encode('utf-8'))

    def setSaleforcity_Source(self,value):
        self.p_saleforcity_source = self.convert.ToString(value.encode('utf-8'))

    def setSaleforcounty_Source(self,value):
        self.p_saleforcounty_source = self.convert.ToString(value.encode('utf-8'))

    def setSaleforbelowcounty_Source(self,value):
        self.p_saleforbelowcounty_source = self.convert.ToString(value.encode('utf-8'))

    def getCity(self):
        return self.p_city

    def getUnit(self):
        return self.p_unit

    def getYear(self):
        return self.p_year

    def getRetailsum(self):
        return self.p_retailsum

    def getSaleforcity(self):
        return self.p_saleforcity

    def getSaleforcounty(self):
        return self.p_saleforcounty

    def getSaleforbelowcounty(self):
        return self.p_saleforbelowcounty

    def getRetailsum_Source(self):
        return self.p_retailsum_source

    def getSaleforcity_Source(self):
        return self.p_saleforcity_source

    def getSaleforcounty_Source(self):
        return self.p_saleforcounty_source

    def getSaleforbelowcounty_Source(self):
        return self.p_saleforbelowcounty_source

class Consumer_Intelligence():
    p_layer, p_type, p_item, p_subitem, p_variablename = None, None, None, None, None
    p_city, p_year, p_data = None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setLayer(self,value):
        self.p_layer = self.convert.ToString(value.encode('utf-8'))

    def setType(self,value):
        self.p_type = self.convert.ToString(value.encode('utf-8'))

    def setItem(self,value):
        self.p_item = self.convert.ToString(value.encode('utf-8'))

    def setSubitem(self,value):
        self.p_subitem = self.convert.ToString(value.encode('utf-8'))

    def setVariablename(self,value):
        self.p_variablename = self.convert.ToString(value.encode('utf-8'))

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setYear(self,value):
        self.p_year = self.convert.ToString(value.encode('utf-8'))

    def setData(self,value):
        self.p_data = self.convert.ToDecimal(value)

    def getLayer(self):
        return self.p_layer

    def getType(self):
        return self.p_type

    def getItem(self):
        return self.p_item

    def getSubitem(self):
        return self.p_subitem

    def getVariablename(self):
        return self.p_variablename

    def getCity(self):
        return self.p_city

    def getYear(self):
        return self.p_year

    def getData(self):
        return self.p_data

class Country():
    p_name, p_longitude, p_latitude = None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setName(self,value):
        self.p_name = self.convert.ToString(value.encode('utf-8'))

    def setLongitude(self,value):
        self.p_longitude = self.convert.ToStringNoEncode(value)

    def setLatitude(self,value):
        self.p_latitude = self.convert.ToStringNoEncode(value)

    def getName(self):
        return self.p_name

    def getLongitude(self):
        return self.p_longitude

    def getLatitude(self):
        return self.p_latitude

class Countryage():
    p_country, p_underfourteen, p_fifteensixtyfour, p_oversixtyfive = None, None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCountry(self,value):
        self.p_country = self.convert.ToString(value.encode('utf-8'))

    def setUnderfourteen(self,value):
        self.p_underfourteen = self.convert.ToDecimal(value)

    def setFifteensixtyfour(self,value):
        self.p_fifteensixtyfour = self.convert.ToDecimal(value)

    def setOversixtyfive(self,value):
        self.p_oversixtyfive = self.convert.ToDecimal(value)

    def getCountry(self):
        return self.p_country

    def getUnderfourteen(self):
        return self.p_underfourteen

    def getFifteensixtyfour(self):
        return self.p_fifteensixtyfour

    def getOversixtyfive(self):
        return self.p_oversixtyfive

class Countrylaborforce():
    p_country, p_male, p_female = None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCountry(self,value):
        self.p_country = self.convert.ToString(value.encode('utf-8'))

    def setMale(self,value):
        self.p_male = self.convert.ToDecimal(value)

    def setFemale(self,value):
        self.p_female = self.convert.ToDecimal(value)

    def getCountry(self):
        return self.p_country

    def getMale(self):
        return self.p_male

    def getFemale(self):
        return self.p_female

class Gender():
    p_country, p_male, p_female = None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCountry(self,value):
        self.p_country = self.convert.ToString(value.encode('utf-8'))

    def setMale(self,value):
        self.p_male = self.convert.ToDecimal(value)

    def setFemale(self,value):
        self.p_female = self.convert.ToDecimal(value)

    def getCountry(self):
        return self.p_country

    def getMale(self):
        return self.p_male

    def getFemale(self):
        return self.p_female

class Marketsize():
    p_country, p_industrytype, p_source, p_subsource, p_categories = None, None, None, None, None
    p_categoriesyear, p_categoriesdata, p_unit, p_datasource = None, None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCountry(self,value):
        self.p_country = self.convert.ToString(value.encode('utf-8'))

    def setIndustrytype(self,value):
        self.p_industrytype = self.convert.ToString(value.encode('utf-8'))

    def setSource(self,value):
        self.p_source = self.convert.ToString(value.encode('utf-8'))

    def setSubsource(self,value):
        self.p_subsource = self.convert.ToString(value.encode('utf-8'))

    def setCategories(self,value):
        self.p_categories = self.convert.ToString(value.encode('utf-8'))

    def setCategoriesyear(self,value):
        self.p_categoriesyear = self.convert.ToInt(value)

    def setCategoriesdata(self,value):
        self.p_categoriesdata = self.convert.ToDecimal(value)

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setDatasource(self,value):
        self.p_datasource = self.convert.ToString(value.encode('utf-8'))

    def getCountry(self):
        return self.p_country

    def getIndustrytype(self):
        return self.p_industrytype

    def getSource(self):
        return self.p_source

    def getSubsource(self):
        return self.p_subsource

    def getCategories(self):
        return self.p_categories

    def getCategoriesyear(self):
        return self.p_categoriesyear

    def getCategoriesdata(self):
        return self.p_categoriesdata

    def getUnit(self):
        return self.p_unit

    def getDatasource(self):
        return self.p_datasource

class Variables():
    p_layer, p_type, p_item, p_subitem, p_variablename = None, None, None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setLayer(self,value):
        self.p_layer = self.convert.ToString(value.encode('utf-8'))

    def setType(self,value):
        self.p_type = self.convert.ToString(value.encode('utf-8'))

    def setItem(self,value):
        self.p_item = self.convert.ToString(value.encode('utf-8'))

    def setSubitem(self,value):
        self.p_subitem = self.convert.ToString(value.encode('utf-8'))

    def setVariablename(self,value):
        self.p_variablename = self.convert.ToString(value.encode('utf-8'))

    def getLayer(self):
        return self.p_layer

    def getType(self):
        return self.p_type

    def getItem(self):
        return self.p_item

    def getSubitem(self):
        return self.p_subitem

    def getVariablename(self):
        return self.p_variablename

class POI():
    p_type, p_subtype, p_name, p_address, p_BD = None, None, None, None, None
    p_lng, p_lat, p_icon, p_memo, p_reserved = None, None, None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setType(self,value):
        self.p_type = self.convert.ToString(value.encode('utf-8'))

    def setSubType(self,value):
        self.p_subtype = self.convert.ToString(value.encode('utf-8'))

    def setName(self,value):
        self.p_name = self.convert.ToString(value.encode('utf-8'))

    def setAddress(self,value):
        self.p_address = self.convert.ToString(value.encode('utf-8'))

    def setBD(self,value):
        self.p_BD = self.convert.ToString(value.encode('utf-8'))

    def setLongitude(self,value):
        self.p_lng = self.convert.ToStringNoEncode(value)

    def setLatitude(self,value):
        self.p_lat = self.convert.ToStringNoEncode(value)

    def setIcon(self,value):
        self.p_icon = self.convert.ToString(value.encode('utf-8'))

    def setMemo(self,value):
        self.p_memo = self.convert.ToString(value.encode('utf-8'))

    def setReserved(self,value):
        self.p_reserved = self.convert.ToString(value.encode('utf-8'))

    def getType(self):
        return self.p_type

    def getSubtype(self):
        return self.p_subtype

    def getName(self):
        return self.p_name

    def getAddress(self):
        return self.p_address

    def getBD(self):
        return self.p_BD

    def getLongitude(self):
        return  self.p_lng

    def getLatitude(self):
        return  self.p_lat

    def getIcon(self):
        return  self.p_icon

    def getMemo(self):
        return self.p_memo

    def getReserved(self):
        return self.p_reserved

class Countrystatistic():
    p_country, p_structure, p_dimensions, p_source, p_target = None, None, None, None, None
    p_second_target, p_unit, p_type, p_data = None, None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCountry(self,value):
        self.p_country = self.convert.ToString(value.encode('utf-8'))

    def setStructure(self,value):
        self.p_structure = self.convert.ToString(value.encode('utf-8'))

    def setDimensions(self,value):
        self.p_dimensions = self.convert.ToString(value.encode('utf-8'))

    def setSource(self,value):
        self.p_source = self.convert.ToString(value.encode('utf-8'))

    def setTarget(self,value):
        self.p_target = self.convert.ToString(value.encode('utf-8'))

    def setSecond_target(self,value):
        self.p_second_target = self.convert.ToString(value.encode('utf-8'))

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setType(self,value):
        self.p_type = self.convert.ToInt(value)

    def setData(self,value):
        self.p_data = self.convert.ToDecimal(value)

    def getCountry(self):
        return self.p_country

    def getStructure(self):
        return self.p_structure

    def getDimensions(self):
        return self.p_dimensions

    def getSource(self):
        return self.p_source

    def getTarget(self):
        return self.p_target

    def getSecond_Target(self):
        return self.p_second_target

    def getUnit(self):
        return self.p_unit

    def getType(self):
        return self.p_type

    def getData(self):
        return self.p_data

class Countrycitystatistic():
    p_city, p_structure, p_dimensions, p_source, p_target = None, None, None, None, None
    p_second_target, p_unit, p_type, p_data = None, None, None, None

    def __init__(self):
        self.convert = convertType()
    def __del__(self):
        self.convert = None

    def setCity(self,value):
        self.p_city = self.convert.ToString(value.encode('utf-8'))

    def setStructure(self,value):
        self.p_structure = self.convert.ToString(value.encode('utf-8'))

    def setDimensions(self,value):
        self.p_dimensions = self.convert.ToString(value.encode('utf-8'))

    def setSource(self,value):
        self.p_source = self.convert.ToString(value.encode('utf-8'))

    def setTarget(self,value):
        self.p_target = self.convert.ToString(value.encode('utf-8'))

    def setSecond_target(self,value):
        self.p_second_target = self.convert.ToString(value.encode('utf-8'))

    def setUnit(self,value):
        self.p_unit = self.convert.ToString(value.encode('utf-8'))

    def setType(self,value):
        self.p_type = self.convert.ToInt(value)

    def setData(self,value):
        self.p_data = self.convert.ToDecimal(value)

    def getCity(self):
        return self.p_city

    def getStructure(self):
        return self.p_structure

    def getDimensions(self):
        return self.p_dimensions

    def getSource(self):
        return self.p_source

    def getTarget(self):
        return self.p_target

    def getSecond_Target(self):
        return self.p_second_target

    def getUnit(self):
        return self.p_unit

    def getType(self):
        return self.p_type

    def getData(self):
        return self.p_data