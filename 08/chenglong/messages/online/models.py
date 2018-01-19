from datetime import datetime
from django.db import models
import json
import MySQLdb



HOST = '192.168.88.252'
PORT = 3306
DB = 'messages'
USER = 'root'
PASSWD = 'mysql'
CHARSET = 'utf8'

# Create your models here.

MESSAGE_FILE = 'messages.json'




SQL_MESSAGE_LIST_COLUMNS = ['id', 'username', 'title', 'content', 'publish_date']
SQL_MESSAGE_LIST = 'select id,username,title,content,date_format(publish_date, "%Y-%m-%d %H:%i:%S") as publish_day from message order by publish_date;'
SQL_MESSAGE_INSERT = 'insert into message(username, title, content, publish_date) values(%s,%s,%s,%s)'

def get_messages():
    conn = MySQLdb.connect(host=HOST,port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_LIST)
    rt_list = cur.fetchall()
    cur.close()
    conn.close()
    return [dict(zip(SQL_MESSAGE_LIST_COLUMNS, line)) for line in rt_list]


def save_messages(username,title,content):
    conn = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_INSERT, (username, title, content, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()
# def get_messages():
#     fhandler = open(MESSAGE_FILE, 'rt')
#     cxt = fhandler.read()
#     fhandler.close()
#     return json.loads(cxt)
#
#
# def save_messages(publish_date, username, title, content):
#     messages = get_messages()
#     messages.append({'publish_date':publish_date, 'username':username, 'title':title, 'content':content})
#     fhandler = open(MESSAGE_FILE, 'wt')
#     fhandler.write(json.dumps(messages))
#     fhandler.close()