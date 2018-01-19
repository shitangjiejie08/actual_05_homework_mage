from django.db import models

import json, time

# Create your models here.

MESSAGE_FILE = 'conf/messages.json'

def get_messages():
    with open(MESSAGE_FILE, 'rt') as fhandle:
        cxt = fhandle.read()
    return json.loads(cxt)

def save_message(username, title, content):
    messages = get_messages()
    messages.append({"username": username, "title": title, "content": content, "publish_date": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())})
    with open(MESSAGE_FILE, 'wt') as fhandler:
        fhandler.write(json.dumps(messages))
    return True