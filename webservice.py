# -*-  coding: utf-8  -*-
__author__ = '10409003'
import web
from population_data.marriage import *
from population_data.age import *
from population_data.education import *
from population_data.age_education import *
from population_data.population_indicator import *
from CashFlow.CashFlowSim import *
from UploadData import SBI_Data
from forecast import ProductForecast,findNews,ProductLicense,CalcuFinance,Persona,RegionSelect,findMSNews
from GroupDecision import DecisionMain,DecisionChannel,DecisionCompet
import logging, time

urls = ("/OpenData/(.*)",'GetData',
        "/CashFlow/(.*)",'GetCaseData',
        "/sbiupload/(.*)", "Uploaddata",
        "/forecast/(.*)","Forecast" ,
        "/news/(.*)","GetNews",
        "/license/(.*)", "License",
        "/finance/(.*)","GetFinanceResult",\
        "/persona/(.*)","GetPersona",
        "/selectregion/(.*)","GetRegion",
        "/groupdecision/(.*)","GetDecision")
app = web.application(urls, globals())

logger = logging.getLogger(__name__)

class GetData():
    def GET(self,name):
        data=name.split('&')
        for i in range(len(data)):
            data[i]=data[i][5:len(data[i])].decode('base64')
        self.OutputData(data)
        # return data[0],data[1],data[2]
        return 'success'

    def OutputData(self, data):
        data_k=data[0].lower()
        data_t = data[1].lower()
        print data_t
        if (data_k=='sex_marriage'):
            print 'sex_marriage'
            FinalData = marriage()
            FinalData.ParserJson(data[2])
        elif (data_k=='sex_age'):
            FinalData = FiveYear_M()
            FinalData.ParserJson(data[2])
            FinalData = FiveYear_F()
            FinalData.ParserJson(data[2])
            FinalData = FiveYear_All()
            FinalData.ParserJson(data[2])
        elif (data_k == 'sex_age_edu'):
            FinalData = Education_M()
            FinalData.ParserJson(data[2])
            FinalData = Education_F()
            FinalData.ParserJson(data[2])
            FinalData = Education_All()
            FinalData.ParserJson(data[2])
            FinalData = Age_Education_M()
            FinalData.ParserJson(data[2])
            FinalData = Age_Education_F()
            FinalData.ParserJson(data[2])
            FinalData = Age_Education_All()
            FinalData.ParserJson(data[2])
        elif (data_k=='pop_index') :
            FinalData = Population_indicator_a()
            FinalData.ParserJson(data[2])
        elif (data_k == 'pop_marriage'):
            FinalData = Population_indicator_b()
            FinalData.Parsercsv(data[2])
        else:
            FinalData = Population_indicator_c()
            FinalData.Parsercsv(data[2])
        # return 'Success'

#取得新創公司財務損益平衡的模擬資料
class GetCaseData():
    def GET(self,name):
        data=name.split('&')
        for i in range(len(data)):
            data[i]=data[i][7:len(data[i])].decode('base64')
        return self.OutputData(data)


    def OutputData(self, data):
        print data[0],int(data[1]),data[2]
        worker = CashFlowSim()
        strcaseID=data[0]
        worker.loadData(strcaseID,blnDel=data[2])
        worker.simTransByDegree(degreeTrans=int(data[1]))
        return worker.output(simOnly=True)

#產業資料庫上傳
class Uploaddata():
    def GET(self, name):
        data = name.split('&')
        for i in range(len(data)):
            data[i] = data[i][5:len(data[i])].decode('base64')

        logging.basicConfig(filename='/data/Population_Data/pyupload.log',
                            level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(filename)s:%(name)s:%(module)s/%(funcName)s/%(lineno)d - %(message)s',
                            datefmt='%Y/%m/%d %I:%M:%S %p')
        logging.Formatter.converter = time.gmtime

        logger.debug('===Uploaddata===')
        logger.debug('data[0]:' + data[0])

        Upload = SBI_Data()
        return Upload.SBI_Data(data[0])

#新品風向預測
class Forecast():
    def GET(self, name):
        data=name.split('&')
        for i in range(len(data)):
            data[i]=data[i][6:len(data[i])].decode('base64')
        
        CacluData = ProductForecast()
        return CacluData.StartCalcu(data[0],data[1])
        
    def POST(self,name):
        self.GET(self.name)

#讀取新聞
class GetNews():
    def GET(self,name):
        news=findMSNews()
        data=news.getNews()
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        resule = json.dumps(data)
        return resule
        
    def POST(self,name):
        self.GET(self.name)

#產品授權機制
class License():
    def GET(self, name):
        data=name.split('&')
        for i in range(len(data)):
            data[i]=data[i][5:len(data[i])].decode('base64')
            #print data[i]
        result=[]
        sp = ProductLicense()
        if data[0] == 'License':
            result=sp.getProductLicense(data[1])
        elif data[0]=='ChannelAuth':
            result = sp.getChannelAuth(data[1],data[2])
        else:
            result = sp.getServiceLicense(int(data[1]))

        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)

        resule = json.dumps(result)
        return resule

        # http://192.168.112.164:8070/license/type=TGljZW5zZQ == & prod = NjJiNGNhNTEtODNiNi0xMWU2LTkxNTEtMDA1MDU2YWY3NjBj
        # type: TGljZW5zZQ==   (License)
        # http://192.168.112.164:8070/license/type=Q2hhbm5lbEF1dGg=&prod=NjJiNGNhNTEtODNiNi0xMWU2LTkxNTEtMDA1MDU2YWY3NjBj&agnt=NzgzYzU4OTAtOGFhMC0xMWU2LTkxNTEtMDA1MDU2YWY3NjBj
        # type:  Q2hhbm5lbEF1dGg=   (ChannelAuth)
        # http://192.168.112.164:8070/license/type=U2VydmljZQ==&quty=MTAw
        # type: U2VydmljZQ== (Service)

#新創公司財務損益平衡
class GetFinanceResult():
    def GET(self, name):
        data = name.split('&')
        for i in range(len(data)):
            data[i] = data[i][5:len(data[i])].decode('base64')

        result = []
        cf=CalcuFinance()
        if data[0]=='balance':
            result = cf.startCalcu(data[1])
        else:
            result = cf.getBathtubCurve(data[1])

        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)

        resule = json.dumps(result)
        return resule

    #損益平衡圖
    #http://localhost:8080/finance/type=YmFsYW5jZQ==&case=MGRiNWVhMTctMmM5Mi0xMWU2LWIxMDEtMDAwYzI5YzFkMDY3
    #浴盆曲線圖
    #http://localhost:8080/finance/type=YmF0aHR1Yg==&case=MGRiNWVhMTctMmM5Mi0xMWU2LWIxMDEtMDAwYzI5YzFkMDY3

#目標客群
class GetPersona():
    def GET(self, name):
        data = name.split('&')
        for i in range(len(data)):
            data[i] = data[i][4:len(data[i])].decode('base64')
            #print data[i]
        result = []
        pn = Persona()
        result = pn.getPersona(data[0],data[1],int(data[2]),int(data[3]),int(data[4]),int(data[5]),int(data[6]),int(data[7]),int(data[8]))
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)

        resule = json.dumps(result)
        return resule

#決策空間
class GetDecision():
    def GET(self, name):
        data = name.split('&')
        for i in range(len(data)):
            data[i] = data[i][5:len(data[i])].decode('base64')

        result = []
        GD = None
        if data[0]== '1':
            GD = DecisionMain()
        elif data[0]== '2':
            GD = DecisionChannel()
        elif data[0]== '3':
            GD = DecisionCompet()
        result = GD.startCalcuate(data[1])

        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        GD = None
        return json.dumps(result)

        #商圈決策
        #http://localhost:8080/groupdecision/type=MQ==&case=MDk5MTBlNWMtNGJjNi00MjUzLWIxNjYtMjQwMWRjNzZlZDY1

#區位選擇
class GetRegion():
    def GET(self, name):
        data = name.split('&')
        for i in range(len(data)):
            data[i] = data[i][5:len(data[i])].decode('base64')

        result = []
        RS = RegionSelect()
        result = RS.startCalcuate(data[0], data[1], data[2], int(data[3]), int(data[4]), \
                                  int(data[5]), int(data[6]), int(data[7]), int(data[8]),\
                                  float(data[9]), float(data[10]), float(data[11]))
        RS = None
        web.header('Content-Type', 'text/json; charset=utf-8;', unique=True)
        return json.dumps(result)

        # http://localhost:8080/selectregion/type=&area=&city=&ch1a=&ch1b=&ch2a=&ch2b=&ch3a=&ch3b=&per1=&per2=&per3=

if __name__ == "__main__":
    app.run()