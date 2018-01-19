from datetime import datetime

from django.db import models
import MySQLdb

# Create your models here.

HOST = '127.0.0.1'
PORT = 3306
DB = 'zyt_db'
USER = 'root'
PASSWD = 'admin'
CHARSET = 'utf8'

SQL_MESSAGE_LIST_COLUMNS = ['mid', 'username', 'title', 'content', 'publish_date']
SQL_MESSAGE_LIST = 'select mid,username,title,content,publish_date from message order by publish_date desc;'
SQL_MESSAGE_INSERT = 'insert into message(username,title,content,publish_date) values(%s,%s,%s,%s)'


def load_messages():
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
            message['publish_date'] = message['publish_date'].strftime("%Y-%m-%d %H:%M:%S")
            rt_list.append(message)
    return rt_list


def create_messages(username, title, content, publish_date):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_INSERT, (username, title, content, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()
    return True
