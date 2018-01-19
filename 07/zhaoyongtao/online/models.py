from django.db import models

import json
# Create your models here.
f_path = 'appendix/online/messages.json'

def load_messages():
    f = open(f_path,'r')
    cxt = json.loads(f.read())
    f.close()
    return cxt

def create_messages(name,title,content,publish_time):
    messages = load_messages()
    message = {"name":name,"title":title,"content":content,"publish_time":publish_time}
    messages.append(message)
    
    f = open(f_path,'w')
    f.write(json.dumps(messages))
    f.close()
    return True
    
