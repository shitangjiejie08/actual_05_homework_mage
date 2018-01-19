from django.db import models
from datetime import datetime
import MySQLdb
# Create your models here.

MESSAGE_FILE = 'messages.json'
HOST = '127.0.0.1'
PORT = 3306
USER = 'root'
PASSWD = ''
CHARSET = 'utf8'
DB = 'huangyisan'

SQL_MESSAGE_LIST_COLUMNS = ['id','username','title', 'content', 'publish_data']
SQL_MESSAGE_LIST = 'select id,username,title,content,publish_data from message2 order by publish_data desc;'
SQL_MESSAGE_INSERT = 'insert into message2(username, title, content, publish_data) values(%s, %s, %s, %s)'
 
def get_messages():
    conn = MySQLdb.connect(host=HOST,port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_LIST)
    lines= cur.fetchall()
    cur.close()
    conn.close()
    rt_list = []
    for line in lines:
        message = dict(zip(SQL_MESSAGE_LIST_COLUMNS,line))
        if message['publish_data']:
            message['publish_data'] = message['publish_data'].strftime('%Y-%m-%d %H:%M:%S')
        rt_list.append(message)
    return rt_list
    #return [dict(zip(SQL_MESSAGE_LIST_COLUMNS,line)) for line in rt_list]
    '''
    fhandler = open(MESSAGE_FILE, 'rt')
    cxt = fhandler.read()
    fhandler.close()
    return json.loads(cxt)
    '''

def save_message(username, title, content):
    messages = get_messages()
    messages.append({'username' : username, 'title' : title, 'content' : content})
    conn = MySQLdb.connect(host=HOST,port=PORT, user=USER, passwd=PASSWD, db=DB, charset=CHARSET)
    cur = conn.cursor()
    cur.execute(SQL_MESSAGE_INSERT,(username, title, content, datetime.now()))
    conn.commit()
    cur.close()
    conn.close()
    '''
    fhandler = open(MESSAGE_FILE, 'wt')
    fhandler.write(json.dumps(messages))
    fhandler.close()
    '''
