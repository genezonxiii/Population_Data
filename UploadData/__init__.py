# -*-  coding: utf-8  -*-
__author__ = '10409003'
import os
from ToMssql.City import City
from ToMssql.CityCivilCar import CityCivilCar
from ToMssql.CityConsumptionExpenditure import CityConsumptionExpenditure
from ToMssql.CityEstateAvgSale import CityEstateAvgSale
from ToMssql.CityEstateCompletion import CityEstateCompletion
from ToMssql.CityEstateSaleAmount import CityEstateSaleAmount
from ToMssql.CityEstateSaleArea import CityEstateSaleArea
from ToMssql.CityGender import CityGender
from ToMssql.CityGoodsTraffic import CityGoodsTraffic
from ToMssql.CityIncome import CityIncome
from ToMssql.CityPassengerTraffic import CityPassengerTraffic
from ToMssql.CityPractitioners import CityPractitioners
from ToMssql.CityRetailExponent import CityRetailExponent
from ToMssql.CitySocialConsume import CitySocialConsume
from ToMssql.CityStaff import CityStaff
from ToMssql.CityTertiaryIncrease import CityTertiaryIncrease
from ToMssql.CityTertiaryIndustry import CityTertiaryIndustry
from ToMssql.CityWholesaleRetail import CityWholesaleRetail
from ToMssql.consumer_intelligence import consumerintelligence
from ToMssql.Country import Country
from ToMssql.CountryAge import CountryAge
from ToMssql.CountryLaborForce import CountryLaborForce
from ToMssql.Gender import Gender
from ToMssql.MarketSize import MarketSize
from ToMssql.Variables import Variables




class SBI_Data():
    Data=None

    def __init__(self):
        pass
    def SBI_Data(self,DataPath):
        Supplier = str(str(str(DataPath).split('/')[4]).split('.')[0]).split('_')[0]
        print Supplier

        if Supplier == 'City':
            FinalData=City()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityCivilCar':
            FinalData=CityCivilCar()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier =='CityConsumptionExpenditure':
            FinalData = CityConsumptionExpenditure()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityEstateAvgSale':
            FinalData = CityEstateAvgSale()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityEstateCompletion':
            FinalData = CityEstateCompletion()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityEstateSaleAmount':
            FinalData = CityEstateSaleAmount()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityEstateSaleArea':
            FinalData = CityEstateSaleArea()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityGender':
            FinalData = CityGender()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityGoodsTraffic':
            FinalData = CityGoodsTraffic()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityIncome':
            FinalData = CityIncome()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityPassengerTraffic':
            FinalData = CityPassengerTraffic()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityPractitioners':
            FinalData = CityPractitioners()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityRetailExponent':
            FinalData = CityRetailExponent()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CitySocialConsume':
            FinalData = CitySocialConsume()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityStaff':
            FinalData = CityStaff()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityTertiaryIncrease':
            FinalData = CityTertiaryIncrease()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityTertiaryIndustry':
            FinalData = CityTertiaryIndustry()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CityWholesaleRetail':
            FinalData = CityWholesaleRetail()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'consumerintelligence':
            FinalData = consumerintelligence()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'Country':
            FinalData = Country()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CountryAge':
            FinalData = CountryAge()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'CountryLaborForce':
            FinalData = CountryLaborForce()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'Gender':
            FinalData = Gender()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'MarketSize':
            FinalData = MarketSize()
            return FinalData.GetData(os.path.join(DataPath))
        elif Supplier == 'Variables':
            FinalData = Variables()
            return FinalData.GetData(os.path.join(DataPath))


if __name__ == '__main__':
    Business = SBI_Data()
    Business.SBI_Data("C:/Users/10409003/Desktop/CityConsumptionExpenditure.xlsx")