# -*-  coding: utf-8  -*-
# __author__ = '10408001'
from setting import Config_2
import mysql.connector
import json
import sys , time, logging
import traceback

logger = logging.getLogger(__name__)
logging.basicConfig(filename='/data/Population_Data/pyupload.log',
                        level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(filename)s:%(name)s:%(module)s/%(funcName)s/%(lineno)d - %(message)s',
                        datefmt='%Y/%m/%d %I:%M:%S %p')
logging.Formatter.converter = time.gmtime
class GetData():
    conn, config = None, None
    def __init__(self):
        self.config = Config_2()

    # 取得 db 連線
    def getConnection(self):
        try:
            if (self.conn == None):
                return mysql.connector.connect(user=self.config.dbUser, password=self.config.dbPwd,
                                               host=self.config.dbServer, database=self.config.dbName)
            else:
                return self.conn
        except mysql.connector.Error:
            print "Connection DB Error"
            raise
        except Exception as e:
            print e.message
            raise

    # 從 db 取得 stored procedure 結果
    def getData(self, procedureName,parameter=None):
        try:
            if self.conn == None:
                self.conn = self.getConnection()
            cursor = self.conn.cursor()
            if parameter == None :
                cursor.callproc(procedureName)
            else:
                cursor.callproc(procedureName,parameter)
            data_row = []
            for row in cursor.stored_results():
                data_row = row.fetchall()
            cursor.close()
            return data_row
        except Exception as e:
            print e.message
            raise

class getPOI_Data():
    name_corr = None
    def __init__(self):
        #宣告對照用的欄位
        self.name_corr=['type','subtype','name','address','BD','lng','lat','icon','memo','reserved']
    def getPOI(self,search_type):
        try:
            GD = GetData()
            parameter = [search_type]
            #呼叫stored procedure
            logger.debug('parameter: '+search_type)
            result = GD.getData('sp_select_poi_by_subtype', parameter)
            #用array記錄回傳結果
            logger.debug('===got '+str(len(result))+' datas===')
            returnData = []
            for row in result:
                #產生dictionary去記錄每筆結果的值
                resultVO = {}
                #從1開始 去掉ID 後面少三個 去掉icon  memo reserved欄位
                for i in range(1,len(row)-3):
                    if (row[i] != None):
                        resultVO[self.name_corr[i - 1]] = row[i]
                returnData.append(resultVO)
            return {"result":returnData}

        except Exception as err:
            logger.debug('===API-POI encounter error: '+str(err)+'===')

class getCompanyRegisterType_Data():
    name_corr = None
    def __init__(self):
        #宣告對照用的欄位
        self.name_corr=['type ','EIN ','company_name ','address ','representative ','capital_amount ','status ','lat ','lng ','creation_date','modification_date','disbanded_date','memo']
    def getCompanyRegister(self,search_type):
        try:
            GD = GetData()
            parameter = [search_type]
            #呼叫stored procedure
            logger.debug('parameter: '+search_type)
            result = GD.getData('sp_select_company_register_type', parameter)
            #用array記錄回傳結果
            logger.debug('===got '+str(len(result))+' datas===')
            returnData = []
            for row in result:
                #產生dictionary去記錄每筆結果的值
                resultVO = {}
                #從1開始 去掉ID 後面去掉 memo
                for i in range(1,len(row)-1):
                    if(row[i]!= None):
                        resultVO[self.name_corr[i-1]]=row[i]
                    else:
                        resultVO[self.name_corr[i - 1]] = ""
                returnData.append(resultVO)
            return {"result":returnData}

        except Exception as err:
            logger.debug('===API-CompanyRegisterType encounter error: '+str(err)+'===')

class getCompanyRegisterType_Data():
    name_corr = None
    def __init__(self):
        #宣告對照用的欄位
        self.name_corr=['type ','EIN ','company_name ','address ','representative ','capital_amount ','status ','lat ','lng ','creation_date','modification_date','disbanded_date','memo']
    def getCompanyRegister(self,search_type):
        try:
            GD = GetData()
            parameter = [search_type]
            #呼叫stored procedure
            logger.debug('parameter: '+search_type)
            result = GD.getData('sp_select_company_register_type', parameter)
            #用array記錄回傳結果
            logger.debug('===got '+str(len(result))+' datas===')
            returnData = []
            for row in result:
                #產生dictionary去記錄每筆結果的值
                resultVO = {}
                #從1開始 去掉ID 後面少去掉memo
                for i in range(1,len(row)-1):
                    if(row[i]!= None):
                        resultVO[self.name_corr[i-1]]=row[i]
                    else:
                        resultVO[self.name_corr[i - 1]] = ""
                returnData.append(resultVO)
            return {"result":returnData}

        except Exception as err:
            logger.debug('===API-CompanyRegisterType encounter error: '+str(err)+'===')

class getCompanyRegisterList_Data():
    name_corr = None
    def __init__(self):
        #宣告對照用的欄位
        self.name_corr=['type ','EIN ','company_name ','address ','representative ','capital_amount ','status ','lat ','lng ','creation_date','modification_date','disbanded_date','memo']
    def getCompanyRegister(self,search_type):
        try:
            GD = GetData()
            parameter = [search_type]
            #呼叫stored procedure
            logger.debug('parameter: '+search_type)
            result = GD.getData('sp_select_company_register_list', parameter)
            #用array記錄回傳結果
            logger.debug('===got '+str(len(result))+' datas===')
            returnData = []
            for row in result:
                #產生dictionary去記錄每筆結果的值
                resultVO = {}
                #從1開始 去掉ID 後面少去掉memo
                for i in range(1,len(row)-1):
                    if(row[i]!= None):
                        resultVO[self.name_corr[i-1]]=row[i]
                    else:
                        resultVO[self.name_corr[i - 1]] = ""
                returnData.append(resultVO)
            return {"result":returnData}

        except Exception as err:
            logger.debug('===API-CompanyRegisterList encounter error: '+str(err)+'===')

class getCompanyRegisterOther_Data():
    name_corr = None
    def __init__(self):
        #宣告對照用的欄位
        self.name_corr=['type ','EIN ','company_name ','address ','representative ','capital_amount ','status ','lat ','lng ','creation_date','modification_date','disbanded_date','memo']
    def getCompanyRegister(self,search_type):
        try:
            GD = GetData()
            parameter = [search_type]
            #呼叫stored procedure
            logger.debug('parameter: '+search_type)
            result = GD.getData('sp_select_company_register_other', parameter)
            #用array記錄回傳結果
            logger.debug('===got '+str(len(result))+' datas===')
            returnData = []
            for row in result:
                #產生dictionary去記錄每筆結果的值
                resultVO = {}
                #從1開始 去掉ID 後面少去掉memo
                for i in range(1,len(row)-1):
                    if(row[i]!= None):
                        resultVO[self.name_corr[i-1]]=row[i]
                    else:
                        resultVO[self.name_corr[i - 1]] = ""
                returnData.append(resultVO)
            return {"result":returnData}

        except Exception as err:
            logger.debug('===API-CompanyRegisterOther encounter error: '+str(err)+'===')

class getCompanyRegisterStat_Data():
    name_corr = None
    def __init__(self):
        #宣告對照用的欄位
        self.name_corr={}
        self.name_corr['chattels_mortgage_transaction'] = ['time_month','action','entity','type','mortgage_amount','currency','contract_time','terminate_time','memo']
        self.name_corr['chattels_mortgage_transaction_stat'] = ['time_month','type','mortgage_amount','currency','quantity','memo']
        self.name_corr['register_stat_change'] = ['county_id','county_name','last_month_quantity','last_month_capital','established_quantity','established_capital','disbanded_quantity','disbanded_capital','increase_quantity','increase_capital','decrease_quantity','decrease_capital','industry_alter_quantity','industry_alter_capital','modification_quantity','modification_capital','current_month_quantity','current_month_capital','info_time','memo']
        self.name_corr['register_stat_change_industrytype'] = ['industry_type','last_month_quantity','last_month_capital','established_quantity','established_capital','disbanded_quantity','disbanded_capital','increase_quantity','increase_capital','decrease_quantity','decrease_capital','industry_alter_quantity','industry_alter_capital','modification_quantity','modification_capital','current_month_quantity','current_month_capital','info_time','memo']
        self.name_corr['register_stat_change_organ'] = ['organ','last_month_quantity','last_month_capital','established_quantity','established_capital','disbanded_quantity','disbanded_capital','increase_quantity','increase_capital','decrease_quantity','decrease_capital','industry_alter_quantity','industry_alter_capital','modification_quantity','modification_capital','current_month_quantity','current_month_capital','info_time','memo']
        self.name_corr['register_stat_foreign_industry'] = ['foreign_company_type','total','AgricultureForestryFishingAnimalHusbandry','MiningAndEarthwork','Manufacturing','ElectricityAndGasSupplyIndustry','WaterSupplyAndPollutionRemediation','ConstructionIndustry','WholesaleAndRetailTrade','TransportAndWarehousing','AccommodationAndCatering','InformationAndCommunication','FinanceAndInsurance','ImmovableIndustry','ProfessionalScientificAndTechnicalServices','SupportServices','PublicAdministrationAndDefenseCompulsorySocialSecurity','EducationServices','HealthCareAndSocialWorkServices','ArtsEntertainmentAndLeisureServices','OtherServices','uncategorized','info_time','memo']
        self.name_corr['register_stat_foreign_workingcapital'] = ['foreign_company_type','total','_0_1mil','_1_5mil','_5_10mil','_10_20mil','_20_30mil','_30_40mil','_40_50mil','_50_60mil','_60_100mil','_100_150mil','_150_200mil','_200mil_up','info_time','memo']
        self.name_corr['register_stat_industry_disbanded'] = ['county_id','county_name','total_quantity','total_capital','AgricultureForestryFishingAnimalHusbandry_quantity','AgricultureForestryFishingAnimalHusbandry_capital','MiningAndEarthwork_quantity','MiningAndEarthwork_capital','Manufacturing_quantity','Manufacturing_capital','ElectricityAndGasSupplyIndustry_quantity','ElectricityAndGasSupplyIndustry_capital','WaterSupplyAndPollutionRemediation_quantity','WaterSupplyAndPollutionRemediation_capital','ConstructionIndustry_quantity','ConstructionIndustry_capital','WholesaleAndRetailTrade_quantity','WholesaleAndRetailTrade_capital','TransportAndWarehousing_quantity','TransportAndWarehousing_capital','AccommodationAndCatering_quantity','AccommodationAndCatering_capital','InformationAndCommunication_quantity','InformationAndCommunication_capital','FinanceAndInsurance_quantity','FinanceAndInsurance_capital','ImmovableIndustry_quantity','ImmovableIndustry_capital','ProfessionalScientificAndTechnicalServices_quantity','ProfessionalScientificAndTechnicalServices_capital','SupportServices_quantity','SupportServices_capital','PublicAdministrationAndDefenseCompulsorySocialSecurity_quantity','PublicAdministrationAndDefenseCompulsorySocialSecurity_capital','EducationServices_quantity','EducationServices_capital','HealthCareAndSocialWorkServices_quantity','HealthCareAndSocialWorkServices_capital','ArtsEntertainmentAndLeisureServices_quantity','ArtsEntertainmentAndLeisureServices_capital','OtherServices_quantity','OtherServices_capital','uncategorized_quantity','uncategorized_capital','info_time','memo']
        self.name_corr['register_stat_industry_established'] = ['county_id','county_name','total_quantity','total_capital','AgricultureForestryFishingAnimalHusbandry_quantity','AgricultureForestryFishingAnimalHusbandry_capital','MiningAndEarthwork_quantity','MiningAndEarthwork_capital','Manufacturing_quantity','Manufacturing_capital','ElectricityAndGasSupplyIndustry_quantity','ElectricityAndGasSupplyIndustry_capital','WaterSupplyAndPollutionRemediation_quantity','WaterSupplyAndPollutionRemediation_capital','ConstructionIndustry_quantity','ConstructionIndustry_capital','WholesaleAndRetailTrade_quantity','WholesaleAndRetailTrade_capital','TransportAndWarehousing_quantity','TransportAndWarehousing_capital','AccommodationAndCatering_quantity','AccommodationAndCatering_capital','InformationAndCommunication_quantity','InformationAndCommunication_capital','FinanceAndInsurance_quantity','FinanceAndInsurance_capital','ImmovableIndustry_quantity','ImmovableIndustry_capital','ProfessionalScientificAndTechnicalServices_quantity','ProfessionalScientificAndTechnicalServices_capital','SupportServices_quantity','SupportServices_capital','PublicAdministrationAndDefenseCompulsorySocialSecurity_quantity','PublicAdministrationAndDefenseCompulsorySocialSecurity_capital','EducationServices_quantity','EducationServices_capital','HealthCareAndSocialWorkServices_quantity','HealthCareAndSocialWorkServices_capital','ArtsEntertainmentAndLeisureServices_quantity','ArtsEntertainmentAndLeisureServices_capital','OtherServices_quantity','OtherServices_capital','uncategorized_quantity','uncategorized_capital','info_time','memo']
        self.name_corr['register_stat_industry_existing'] = ['county_id','county_name','total_quantity','total_capital','AgricultureForestryFishingAnimalHusbandry_quantity','AgricultureForestryFishingAnimalHusbandry_capital','MiningAndEarthwork_quantity','MiningAndEarthwork_capital','Manufacturing_quantity','Manufacturing_capital','ElectricityAndGasSupplyIndustry_quantity','ElectricityAndGasSupplyIndustry_capital','WaterSupplyAndPollutionRemediation_quantity','WaterSupplyAndPollutionRemediation_capital','ConstructionIndustry_quantity','ConstructionIndustry_capital','WholesaleAndRetailTrade_quantity','WholesaleAndRetailTrade_capital','TransportAndWarehousing_quantity','TransportAndWarehousing_capital','AccommodationAndCatering_quantity','AccommodationAndCatering_capital','InformationAndCommunication_quantity','InformationAndCommunication_capital','FinanceAndInsurance_quantity','FinanceAndInsurance_capital','ImmovableIndustry_quantity','ImmovableIndustry_capital','ProfessionalScientificAndTechnicalServices_quantity','ProfessionalScientificAndTechnicalServices_capital','SupportServices_quantity','SupportServices_capital','PublicAdministrationAndDefenseCompulsorySocialSecurity_quantity','PublicAdministrationAndDefenseCompulsorySocialSecurity_capital','EducationServices_quantity','EducationServices_capital','HealthCareAndSocialWorkServices_quantity','HealthCareAndSocialWorkServices_capital','ArtsEntertainmentAndLeisureServices_quantity','ArtsEntertainmentAndLeisureServices_capital','OtherServices_quantity','OtherServices_capital','uncategorized_quantity','uncategorized_capital','info_time','memo']
        self.name_corr['register_stat_industry_organ'] = ['organ_name','total_quantity','total_capital','AgricultureForestryFishingAnimalHusbandry_quantity','AgricultureForestryFishingAnimalHusbandry_capital','MiningAndEarthwork_quantity','MiningAndEarthwork_capital','Manufacturing_quantity','Manufacturing_capital','ElectricityAndGasSupplyIndustry_quantity','ElectricityAndGasSupplyIndustry_capital','WaterSupplyAndPollutionRemediation_quantity','WaterSupplyAndPollutionRemediation_capital','ConstructionIndustry_quantity','ConstructionIndustry_capital','WholesaleAndRetailTrade_quantity','WholesaleAndRetailTrade_capital','TransportAndWarehousing_quantity','TransportAndWarehousing_capital','AccommodationAndCatering_quantity','AccommodationAndCatering_capital','InformationAndCommunication_quantity','InformationAndCommunication_capital','FinanceAndInsurance_quantity','FinanceAndInsurance_capital','ImmovableIndustry_quantity','ImmovableIndustry_capital','ProfessionalScientificAndTechnicalServices_quantity','ProfessionalScientificAndTechnicalServices_capital','SupportServices_quantity','SupportServices_capital','PublicAdministrationAndDefenseCompulsorySocialSecurity_quantity','PublicAdministrationAndDefenseCompulsorySocialSecurity_capital','EducationServices_quantity','EducationServices_capital','HealthCareAndSocialWorkServices_quantity','HealthCareAndSocialWorkServices_capital','ArtsEntertainmentAndLeisureServices_quantity','ArtsEntertainmentAndLeisureServices_capital','OtherServices_quantity','OtherServices_capital','uncategorized_quantity','uncategorized_capital','info_time','memo']
        self.name_corr['register_stat_organization'] = ['county_id','county_name','total_quantity','total_capital','UnlimitedCompany_quantity','UnlimitedCompany_capital','LimitedPartnership_quantity','LimitedPartnership_capital','LimitedCompany_quantity','LimitedCompany_capital','CompanyLimitedByShares_quantity','CompanyLimitedByShares_capital','ForeignCompanyWithRecognition_quantity','ForeignCompanyWithRecognition_capital','MainlandRegionWithRecognition_quantity','MainlandRegionWithRecognition_capital','ForeignCompanyRepresentativeOffices_quantity','MainlandRegionRepresentativeOffices_quantity','info_time','memo']
        self.name_corr['register_stat_organization_industrytype'] = ['industry_type','total_quantity','total_capital','UnlimitedCompany_quantity','UnlimitedCompany_capital','LimitedPartnership_quantity','LimitedPartnership_capital','LimitedCompany_quantity','LimitedCompany_capital','CompanyLimitedByShares_quantity','CompanyLimitedByShares_capital','ForeignCompanyWithRecognition_quantity','ForeignCompanyWithRecognition_capital','MainlandRegionWithRecognition_quantity','MainlandRegionWithRecognition_capital','ForeignCompanyRepresentativeOffices_quantity','MainlandRegionRepresentativeOffices_quantity','info_time','memo']
        self.name_corr['register_stat_paidup_industry'] = ['industry_type','total_quantity','total_capital','_0_1mil_quantity','_0_1mil_capital','_1_5mil_quantity','_1_5mil_capital','_5_10mil_quantity','_5_10mil_capital','_10_20mil_quantity','_10_20mil_capital','_20_30mil_quantity','_20_30mil_capital','_30_40mil_quantity','_30_40mil_capital','_40_50mil_quantity','_40_50mil_capital','_50_100mil_quantity','_50_100mil_capital','_100_500mil_quantity','_100_500mil_capital','_500mil_up_quantity','_500mil_up_capital','info_time','memo']
        self.name_corr['register_stat_sex'] = ['county_id','county_name','total_quantity','M_quantity','M_quantity_percent','F_quantity','F_quantity_percent','total_capital','M_capital','M_capital_percent','F_capital','F_capital_percent','info_time','memo']
        self.name_corr['register_stat_status'] = ['county_id','county_name','established_capital','established_quantity','existing_capital','existing_quantity','disbanded_capital','disbanded_quantity','info_time','memo']
    def getCompanyRegister(self,search_type):
        try:
            GD = GetData()
            parameter = [search_type]
            #呼叫stored procedure
            logger.debug('parameter: '+search_type)
            result = GD.getData('sp_select_company_register_stat', parameter)
            #用array記錄回傳結果
            logger.debug('===got '+str(len(result))+' datas===')
            returnData = []
            for row in result:
                #產生dictionary去記錄每筆結果的值
                resultVO = {}
                #從1開始 去掉ID 後面少去掉memo
                for i in range(1,len(row)-1):
                    if(row[i]!= None and i<10):
                        resultVO[self.name_corr[parameter[0]][i-1]]=row[i]
                    else:
                        resultVO[self.name_corr[parameter[0]][i - 1]] = ""
                returnData.append(resultVO)
            return {"result":returnData}

        except Exception as err:
            logger.debug('===API-CompanyRegisterStat encounter error: '+str(err)+'===')

class getPOIhiyesData():
    name_corr = None
    def __init__(self):
        #宣告對照用的欄位
        self.name_corr=['poi_id','type','subtype','name','addr','BD','lng','lat','icon','memo','reserved']
    def getPOI(self,lat,lng,radius):
        try:
            GD = GetData()
            parameter = [lat,lng,radius]
            #呼叫stored procedure
            logger.debug('parameter: ' + lat+", " + lng+", " + radius)
            result = GD.getData('sp_select_POI_hiyes', parameter)
            #用array記錄回傳結果
            logger.debug('===got '+str(len(result))+' datas===')
            returnData = []
            for row in result:
                #產生dictionary去記錄每筆結果的值
                resultVO = {}
                #從1開始 去掉ID 後面少去掉memo
                for i in range(0,len(row)):
                    if(row[i]!= None):
                        resultVO[self.name_corr[i]]=row[i]
                    else:
                        resultVO[self.name_corr[i]] = ""
                returnData.append(resultVO)
            return {"result":returnData}

        except Exception as err:
            logger.debug('===getPOIhiyesData encounter error: '+str(err)+'===')
