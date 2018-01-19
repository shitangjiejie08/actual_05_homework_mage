# encoding: utf-8
import MySQLdb
from MySQLdb.cursors import DictCursor


HOST='127.0.0.1'
PORT=3306
DB='zyt_db'
USER='root'
PASSWD='admin'
CHARSET='utf8'


def exec_select(s):
    conn = MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PASSWD,db=DB,charset=CHARSET)
    cur = conn.cursor(DictCursor)
    cur.execute(s)
    lines = cur.fetchall()
    cur.close()
    conn.close()
    return lines

def exec_execute(s):
    conn = MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PASSWD,db=DB,charset=CHARSET)
    cur = conn.cursor()
    cur.execute(s)
    conn.commit()
    cur.close()
    conn.close()
    return True

