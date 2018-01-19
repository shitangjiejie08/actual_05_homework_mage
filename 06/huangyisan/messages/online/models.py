from django.db import models
import json
# Create your models here.
'''
from .import models

def index(request):
    print(models.get_message())
    return render(request, 'online/index.html')
    '''
MESSAGE_FILE = 'messages.json'

def get_messages():
    fhandler = open(MESSAGE_FILE,'rt')
    cxt = fhandler.read()
    fhandler.close()
    return json.loads(cxt)

def save_messages(nowtime,username,title,content):
    messages = get_messages()
    messages.append({"time":nowtime,"username":username,"title":title,"content":content,"publish_date":""})
    fhandler = open(MESSAGE_FILE,'wt')
    fhandler.write(json.dumps(messages))
    fhandler.close()
    return True
