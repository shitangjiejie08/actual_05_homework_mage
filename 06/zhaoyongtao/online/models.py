from django.db import models
import json
# Create your models here.

file_path = 'appendix/online/messages.json'

def get_messages():
    fhandler = open(file_path,'r')
    cxt = json.loads(fhandler.read())
    fhandler.close()
    return cxt


def save_messages(publish,username,title,content):
    messages = get_messages()
    message = {"publish":publish,"username":username,"publish":publish,"title":title,"content":content}
    messages.append(message)
    fhandler = open(file_path,'w')
    fhandler.write(json.dumps(messages))
    print(json.dumps(messages))
    fhandler.close()
    return True
