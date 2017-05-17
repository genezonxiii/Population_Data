# -*-  coding: utf-8  -*-
# __author__ = '10408001'
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from setting import Config_2
import mysql.connector
import urllib
import json
from datetime import datetime

class GetNewsData():
    conn , config = None , None
    def __init__(self):
        self.config = Config_2()

    # 取得要發布電子報內容
    def GetEpaperContent(self):
        Head1, Head2, Foot = '', '', ''
        with open('Head1.txt', 'r') as f:
            Head1 += f.read()

        with open('Head2.txt', 'r') as f:
            Head2 += f.read()

        with open('Foot.txt', 'r') as f:
            Foot += f.read()
        f.close()

        body1 = self.GetNews().encode('utf-8')
        body2 = self.GetIndustryDoc()
        return Head1 + datetime.now().strftime('%Y/%m/%d') + Head2 + body1 + body2 + Foot

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
    def getData(self, procedureName):
        try:
            if self.conn == None :
                self.conn = self.getConnection()
            cursor = self.conn.cursor()
            cursor.callproc(procedureName)
            data_row = []
            for row in cursor.stored_results():
                data_row = row.fetchall()
            cursor.close()
            return data_row
        except Exception as e:
            print e.message
            raise

    # 從商發院主機取得當日新聞內容及 Html 排版
    def GetNews(self):
        result = json.load(urllib.urlopen(self.config.newsUrl))
        showType=[u'總體經濟',u'批發零售業',u'餐飲服務業',u'健康照護服務業',u'時尚服務業',u'物流服務業']
        # 新聞 & 排版
        newsBady = '<table bgcolor="#FFFFFF" width="720" border="0" cellspacing="20" cellpadding="20">' + '\n'
        newsBady += '<tr>' + '\n'
        newsBady += '<td width="50%" valign="top">' + '\n'
        for i in range(len(showType)):
            newsBady += '<table cellspacing="4" cellpadding="4" width="100%">' + '\n'
            newsBady += '<tr> <td> <h2 style = "border-bottom: 1px solid #aaaaaa;color:#372161;font-size:21px;margin:0;padding:0;" > ' \
                        + showType[i]+ ' </h2> </td> </tr>' + '\n'
            # print showType[i]
            for row in result:
                if row['Type'] == showType[i] :
                    newsBady += '<tr><td><a href="'+row['Url']+'" style="color:#2b9abe;font-size:15px;text-decoration: none;">'\
                            +row['Title'] + '</a><span style="color:#555555;font-size:12px;">('+ row['source'] +')</span></td></tr>' + '\n'

            if i == len(showType)-1:
                newsBady += '</table>' + '\n' + '</td><!-- LEFT col -->'
            else:
                newsBady += '</table><br>' + '\n'
        return newsBady

    # 取得商機觀測站內容及 Html 排版
    def GetIndustryDoc(self):
        result = self.getData('sp_select_show_upload_doc')
        # 取得商機觀測站內容及排版
        IndustryDoc = '<td width="50%" valign="top">' + '\n'
        IndustryDoc += '<table cellspacing="4" cellpadding="4" width="100%">' + '\n'
        IndustryDoc += '<tr><td><h2 style="border-bottom: 1px solid #aaaaaa;color:#372161;font-size:21px;margin:0;padding:0;">產業評析</h2></td></tr>' + '\n'
        for row in result :
            IndustryDoc += '<tr><td><a href="' + self.config.IndustryDoc + row[1].encode('utf-8') + '" style="color:#2b9abe;font-size:15px;text-decoration: none;">' + '\n'
        IndustryDoc += row[0].encode('utf-8') + '</a></td></tr>' + '\n'
        IndustryDoc += '</table>' + '\n'
        IndustryDoc += '</td><!-- RIGHT col -->' + '\n'
        IndustryDoc += '</tr>' + '\n'
        return IndustryDoc

class SendEpaper():
    conn, config ,receivers = None, None , None
    def __init__(self):
        self.config = Config_2()
        self.receivers =[]

    def SendMail(self):
        GD = GetNewsData()
        Content = GD.GetEpaperContent()
        sender = self.config.Sender
        self.GetReceivers()
        # 個人單獨發 mail
        for row in self.receivers:
            Receiver = []
            mailCancel = row['email'].encode('utf-8')
            Receiver.append(row['email'])
            self.Send(sender,row['User'].encode('utf-8'),Receiver,mailCancel,Content)
        # 群體發 mail
        # self.Send(sender,'電子報訂戶',self.receivers,Content)

    def Send(self,Sender,RecerverName,Receivers,MailCancel,Content):
        try:
            msg = MIMEMultipart()
            msg['Subject'] = u'SBI 每日產業重點新聞電子報'
            msg["From"] = Sender
            msg["To"] = ', '.join(Receivers)
            text = "<p>Hi! " + RecerverName + " 您好<br>您訂閱的電子報如下：</p>"
            Content += MailCancel.encode('base64')
            with open('Foot1.txt', 'r') as f:
                Content += f.read()
            f.close()
            part = MIMEText(text + Content, 'html')
            msg.attach(part)
            smtpObj = smtplib.SMTP(self.config.SMTP)
            smtpObj.sendmail(Sender, Receivers, msg.as_string())
            print "Successfully sent email"
        except Exception as e:
            print e.message
            print "Error: unable to send email"

    # 取得收件人名單
    def GetReceivers(self):
        result = self.getData('sp_select_EpaperOrder_User')
        for row in result:
            # 群體發 mail
            # self.receivers.append(row[1])
            # 個人單獨發 mail
            r = {'User':row[0],'email':row[1]}
            self.receivers.append(r)

    # 取得 db 連線

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
    def getData(self, procedureName):
        try:
            if self.conn == None:
                self.conn = self.getConnection()
            cursor = self.conn.cursor()
            cursor.callproc(procedureName)
            data_row = []
            for row in cursor.stored_results():
                data_row = row.fetchall()
            cursor.close()
            return data_row
        except Exception as e:
            print e.message
            raise

if __name__ == '__main__':
    SE = SendEpaper()
    SE.SendMail()