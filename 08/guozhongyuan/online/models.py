from django.db import models
from datetime import datetime
# Create your models here.

import json
import MySQLdb
#使用数据库存储数据

HOST = '127.0.0.1'
PORT = 3306
DB = 'gzy'
USER = 'root'
PASSWD = '123456'
CHARSET = 'utf8'

SQL_MESSAGE_LIST_COLUMNS = ['id','username','title','content','publish_date']
SQL_MESSAGE_LIST = 'select id,username,title,content,publish_date from message3 order by publish_date desc;'
SQL_MESSAGE_INSERT = 'insert into message3 (username,title,content,publish_date) values( %s, %s, %s, %s)'

MESSAGE_FILE = 'message.json'

def get_messages_json():

	fandler = open(MESSAGE_FILE,'rt')
	cxt = fandler.read()
	fandler.close()
	
	return json.loads(cxt)


def save_message_json(username,title,content):

	messages = get_messages()
	message = {'username':username,'title':title,'content':content}
	messages.append(message)

	fandler = open(MESSAGE_FILE, 'w')
	fandler.write(json.dumps(messages))
	fandler.close()



def get_messages():
	conn = MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PASSWD,db=DB,charset=CHARSET)
	cur = conn.cursor()
	cur.execute(SQL_MESSAGE_LIST)
	lines = cur.fetchall()
	cur.close()
	conn.close()
	rt_list = []
	for line in lines:
		message = dict(zip(SQL_MESSAGE_LIST_COLUMNS,line))
		#print (message)
		if message['publish_date']:
			message['publish_date']= message['publish_date'].strftime('%Y-%m-%d %H:%M:%S')
		rt_list.append(message)
	return rt_list

def save_message(username,title,content):
	conn = MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PASSWD,db=DB,charset=CHARSET)
	cur= conn.cursor()
	cur.execute(SQL_MESSAGE_INSERT,(username,title,content,datetime.now()))
	conn.commit()
	cur.close()
	conn.close()








