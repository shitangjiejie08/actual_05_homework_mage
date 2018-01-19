
import datetime
import json

import MySQLdb

from django.db import models
# Create your models here.

MESSAGE_FILE = 'messages.json'
class MysqlControl:
    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.passwd = "123456"
        self.port = 3306
        self.db = "mhl"
        self.charset = "utf8"
        self.select_all = "select id,publish_date,username,title,content from messages"
        self.insert_sql = "insert messages(publish_date, username, title, content) values(%s,%s,%s,%s)"


    def get_messages(self):
        conn = MySQLdb.connect(host=self.host,user=self.user,port=self.port,passwd=self.passwd,charset=self.charset,db=self.db)
        cursor = conn.cursor()
        cursor.execute(self.select_all)
        rows = cursor.fetchall()
        #info = [dict(zip(("id","publish_date","username","title","content"),row)) for row in rows]
        info = []
        dt = lambda x:datetime.datetime.strftime(x,"%Y-%m-%d %H:%M:%S")
        for row in rows:
            d1 = dict(zip(("id","publish_date","username","title","content"),(row[0],dt(row[1]),row[2],row[3],row[4])))
            info.append(d1)
        cursor.close()
        conn.close()
        return info
    def save_message(self,username,title,content):
        conn = MySQLdb.connect(host=self.host, user=self.user, port=self.port, passwd=self.passwd, charset=self.charset,db=self.db)
        cursor = conn.cursor()
        param = (datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%M:%S"),username,title,content)
        cursor.execute(self.insert_sql,param)
        conn.commit()
        cursor.close()
        conn.close()


mc = MysqlControl()
get_messages = mc.get_messages
save_message = mc.save_message
# def get_messages():
#     fhandler = open(MESSAGE_FILE, 'rt')
#     cxt = fhandler.read()
#     fhandler.close()
#     return json.loads(cxt)

# def save_message(username, title, content):
#     messages = get_messages()
#     messages.append({'username' : username, 'title' : title, 'content' : content})
#     fhandler = open(MESSAGE_FILE, 'wt')
#     fhandler.write(json.dumps(messages))
#     fhandler.close()
