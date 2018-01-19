from django.db import models

from pymysql.cursors import DictCursor
import pymysql

HOST = '172.16.129.143'
PORT = 3306
DB = 'xiaozhi'
USER = 'root'
PASSWD = 'password'
CHARSET ='utf8'


SQL_LOG_INSERT = "insert into access_log(ip, access_time, method, url, agreement, status, flux) " \
                     "values(%s, %s, %s, %s, %s, %s, %s);"
SQL_LOG_STATUS = "select * from access_log where status = %s limit 100"

def add_log(ip, access_time, method, url, agreement, status, flux):
    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, passwd=PASSWD, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_LOG_INSERT, (ip, access_time, method, url, agreement, status, flux))
    conn.commit()

def read_log(log):
    with open(log) as f:
        for line in f:
            yield  line


def loganalysis():
    for line in read_log('access.log.10'):
        line = line.split()
        ip, access_time, method, url, agreement, status, flux = line[0], line[3], line[5], line[6], \
                                                                      line[7], line[8], line[9],
        yield ip, access_time, method, url, agreement, status, flux


def import_sql():
    for  line in loganalysis():
        ip, access_time, method, url, agreement, status, flux = line
        add_log(ip, access_time[1::], method, url, agreement, status, flux)


def list(status):
    rt = {}
    conn = pymysql.connect(host=HOST, port=PORT, db=DB, user=USER, passwd=PASSWD, charset=CHARSET, cursorclass=DictCursor)
    cur = conn.cursor()
    cur.execute(SQL_LOG_STATUS, (status,))
    rt_list = cur.fetchall()
    for num, row in enumerate(rt_list):
        ip = row['ip']
        access_time = row['access_time']
        method = row['method']
        url = row['url']
        agreement = row['agreement']
        status = row['status']
        flux = row['flux']
        rt[num] = {'ip':ip,
                   'access_time':access_time,
                   'method':method,
                   'url':url,
                   'agreement':agreement,
                   'status':status,
                   'flux':flux}
    print(rt)
    return rt



if __name__ == '__main__':
    import_sql()
