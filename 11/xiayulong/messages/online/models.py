from django.db import models

import time
import json
import MySQLdb

from django.db import models
# Create your models here.

class message2(models.Model):
    username = models.CharField(max_length=256,null=True)
    title = models.CharField(max_length=512,null=True)
    content = models.TextField(null=True)
    publish_date = models.DateTimeField(null=True)

    def __str__(self):
        tpl = '<message2: [username = {username}, tile = {title}, content = {content}, publish_date = {publish_date}]>'
        #return tpl.format(username=message2.username, title=message2.title, content=message2.content, publish_date=message2.publish_date)
        return tpl.format(username=self.username, title=self.title, content=self.content, publish_date=self.publish_date)


FILE_MESSAGE = 'messages.json'
user = 'root'
passwd = 'redhat'
host = '127.0.0.1'
db = 'message'
messages = 'select title,content,date_format(publish_date,"%Y/%m/%d %h:%i:%s"),username from tbl_message'
insert_sql = 'insert into tbl_message (title,content,publish_date,username) values (%s,%s,%s,%s)'

#def get_messages():
#    fd = open(FILE_MESSAGE,'rt')
#    cxt = fd.read()
#    fd.close()
#    print('get_messages',cxt)
#    return json.loads(cxt)
def get_messages():
    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset='utf8')
    cursor = conn.cursor()
    cursor.execute(messages)
    lines = cursor.fetchall()
    cursor.close()
    conn.close()
    arttribute = ('title','content','publish_date','username')
    result = [dict(zip(arttribute,line)) for line in lines]
    print(result)
    return result


#def set_messages(message):
#    cxt = get_messages()
#    message.setdefault("publish_date",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
#    fd = open(FILE_MESSAGE,'wt')
#    print('get_messages_pre_set',cxt)
#    cxt.append(message)
#    print('set_messages',cxt)
#    fd.write(json.dumps(cxt))
#    fd.close()

def set_messages(message):
    message.setdefault("publish_date",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,charset='utf8')
    cursor = conn.cursor()
    cursor.execute(insert_sql,(message.get("title"),message.get("content"),message.get("publish_date"),message.get("username")))
    conn.commit()
    cursor.close()
    conn.close() 





