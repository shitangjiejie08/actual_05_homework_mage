
from django.db import models
from pymysql.cursors import DictCursor
import json
from datetime import datetime
import  pymysql

MESSAGE_FILE = "messages.json"

HOST = '172.16.129.143'
PORT = 3306
DB = 'xiaozhi'
USER = 'root'
PASSWD = 'password'
CHARSET ='utf8'
SQL_MESSAGE_LIST = "select id,username,title,content,DATE_FORMAT(publish_date,'%Y-%m-%d %H:%i:%S') as time from message3 order by time desc;"
SQL_MESSAGE_LIST_COLUMS = ['id', 'username', 'title', 'content', 'publish_date']



def get_messages():
    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, passwd=PASSWD, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_LIST)
    rt_list = cur.fetchall()
    print(rt_list)
    cur.close()
    conn.close()
    ret = [dict(zip(SQL_MESSAGE_LIST_COLUMS, line)) for line in rt_list]
    print(type(ret))
    return [dict(zip(SQL_MESSAGE_LIST_COLUMS, line)) for line in rt_list]


def save_message(username, title, content):

    SQL_MESSAGE_INSERT = "insert into message3(username,title,content, publish_date) values('%s','%s','%s','%s')"%(username,
                                                                                                          title,
                                                                                                          content,
                                                                                                          datetime.now())
    print(SQL_MESSAGE_INSERT)
    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, passwd=PASSWD, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_INSERT)
    conn.commit()
    cur.close()
    conn.close()


