from django.db import models

import json
from datetime import datetime
import MySQLdb
# Create your models here.

MESSAGE_FILE = 'messages.json'

HOST = '192.168.6.15'
PORT = 3306
DB = 'django_web'
USER = 'root'
PASSWD = 'iscs@2016up'
CHARSET = 'utf8'

SQL_MESSAGE_LIST_COLUMNS = ['id', 'username', 'title', 'content', 'publish_date']
SQL_MESSAGE_LIST = 'select id, username, title, content, publish_date from message order by publish_date DESC;'
SQL_MESSAGE_INSERT = 'insert into message(username, title, content, publish_date) values(%s, %s, %s, %s);'

def get_messages():
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_LIST)
    lines = cur.fetchall()
    cur.close()
    conn.close()
    rt_list = []
    for line in lines:
        message = dict(zip(SQL_MESSAGE_LIST_COLUMNS, line))
        if message['publish_date']:
            message['publish_date'] = message['publish_date'].strftime('%Y-%m-%d %H:%M:%S')
        rt_list.append(message)
    return rt_list

def save_message(username, title, content):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_INSERT, (username, title, content, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()
