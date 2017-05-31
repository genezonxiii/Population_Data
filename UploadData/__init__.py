# -*-  coding: utf-8  -*-
__author__ = '10409003'
import os
from ToMysql.City import CityData
from ToMysql.CityCivilCar import CityCivilCarData
from ToMysql.CityConsumptionExpenditure import CityConsumptionExpenditureData
from ToMysql.CityEstateAvgSale import CityEstateAvgSaleData
from ToMysql.CityEstateCompletion import CityEstateCompletionData
from ToMysql.CityEstateSaleAmount import CityEstateSaleAmountData
from ToMysql.CityEstateSaleArea import CityEstateSaleAreaData
from ToMysql.CityGender import CityGenderData
from ToMysql.CityGoodsTraffic import CityGoodsTrafficData
from ToMysql.CityIncome import CityIncomeData
from ToMysql.CityPassengerTraffic import CityPassengerTrafficData
from ToMysql.CityPractitioners import CityPractitionersData
from ToMysql.CityRetailExponent import CityRetailExponentData
from ToMysql.CitySocialConsume import CitySocialConsumeData
from ToMysql.CityStaff import CityStaffData
from ToMysql.CityTertiaryIncrease import CityTertiaryIncreaseData
from ToMysql.CityTertiaryIndustry import CityTertiaryIndustryData
from ToMysql.CityWholesaleRetail import CityWholesaleRetailData
from ToMysql.consumer_intelligence import Consumer_IntelligenceData
from ToMysql.Country import CountryData
from ToMysql.CountryAge import CountryAgeData
from ToMysql.CountryLaborForce import CountryLaborForceData
from ToMysql.Gender import GenderData
from ToMysql.MarketSize import MarketsizeData
from ToMysql.Variables import VariablesData
from ToMysql.POI import POIData
from ToMysql.Countrystatistic import CountrystatisticData
from ToMysql.Countrycitystatistic import CountrycitystatisticData
import  logging

logger = logging.getLogger(__name__)

class SBI_Data():
    Data=None

    def __init__(self):
        pass
    def SBI_Data(self,DataPath):
        filename_with_ext = str(DataPath).split('/')[4]
        filename = str(filename_with_ext).split('.')[0]
        Industry = str(filename).split('_')[0]
        #Supplier = str(str(str(DataPath).split('/')[4]).split('.')[0]).split('_')[0]
        print Industry

        if Industry == 'City':
            FinalData=CityData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityCivilCar':
            FinalData=CityCivilCarData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry =='CityConsumptionExpenditure':
            FinalData = CityConsumptionExpenditureData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityEstateAvgSale':
            FinalData = CityEstateAvgSaleData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityEstateCompletion':
            FinalData = CityEstateCompletionData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityEstateSaleAmount':
            FinalData = CityEstateSaleAmountData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityEstateSaleArea':
            FinalData = CityEstateSaleAreaData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityGender':
            FinalData = CityGenderData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityGoodsTraffic':
            FinalData = CityGoodsTrafficData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityIncome':
            FinalData = CityIncomeData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityPassengerTraffic':
            FinalData = CityPassengerTrafficData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityPractitioners':
            FinalData = CityPractitionersData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityRetailExponent':
            FinalData = CityRetailExponentData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CitySocialConsume':
            FinalData = CitySocialConsumeData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityStaff':
            FinalData = CityStaffData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityTertiaryIncrease':
            FinalData = CityTertiaryIncreaseData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityTertiaryIndustry':
            FinalData = CityTertiaryIndustryData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CityWholesaleRetail':
            FinalData = CityWholesaleRetailData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'consumerintelligence':
            FinalData = Consumer_IntelligenceData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'Country':
            FinalData = CountryData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CountryAge':
            FinalData = CountryAgeData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'CountryLaborForce':
            FinalData = CountryLaborForceData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'Gender':
            FinalData = GenderData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'MarketSize':
            FinalData = MarketsizeData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'Variables':
            FinalData = VariablesData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'POI' :
            FinalData = POIData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'Countrystatistic':
            FinalData = CountrystatisticData()
            return FinalData.GetData(os.path.join(DataPath))
        elif Industry == 'Countrycitystatistic':
            FinalData = CountrycitystatisticData()
            return FinalData.GetData(os.path.join(DataPath))

if __name__ == '__main__':
    Business = SBI_Data()
    Business.SBI_Data("C:/Users/10409003/Desktop/CityConsumptionExpenditure.xlsx")