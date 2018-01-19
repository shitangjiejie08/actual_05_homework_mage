from django.db import models

import time
import json

# Create your models here.

FILE_MESSAGE = 'messages.json'

def get_messages():
    fd = open(FILE_MESSAGE,'rt')
    cxt = fd.read()
    fd.close()
    print('get_messages',cxt)
    return json.loads(cxt)


def set_messages(message):
    cxt = get_messages()
    message.setdefault("publish_date",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    fd = open(FILE_MESSAGE,'wt')
    print('get_messages_pre_set',cxt)
    cxt.append(message)
    print('set_messages',cxt)
    fd.write(json.dumps(cxt))
    fd.close()
