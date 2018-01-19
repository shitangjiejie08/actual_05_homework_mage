from django.db import models
import json
MESSAGE_FILE = 'user_db'
def get_messages():
    fhandler = open(MESSAGE_FILE,'rt')
    context = fhandler.read()
    fhandler.close()
    return json.loads(context)

def save_message(name,age,telephone):
    messages=get_messages()
    messages[name]={'Age':age,'Tel':telephone} 
    fhandler = open(MESSAGE_FILE, 'wt')
    fhandler.write(json.dumps(messages))
    fhandler.close()
    return True

def del_message(name):
    messages=get_messages()
    messages.pop(name,"")
    fhandler = open(MESSAGE_FILE, 'wt')
    fhandler.write(json.dumps(messages))
    fhandler.close()
    return True
