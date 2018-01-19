from django.db import models
import json
import time
# Create your models here.
FILE_NAME = 'messages.json'
def get_messages():
    fhandler = open(FILE_NAME,'r')
    cxt = fhandler.read()
    fhandler.close()
    return json.loads(cxt)
def save_messages(username,title,content):
    messages = get_messages()
    messages.append({"username":username,"title":title,"content":content,"publish_date":time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())})
    fhandler = open(FILE_NAME,'wt')
    fhandler.write(json.dumps(messages))
    fhandler.close()
    return True
