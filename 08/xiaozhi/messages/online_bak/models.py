import json
import datetime
from django.db import models


MESSAGE_FILE = "messages.json"
def get_messages():
    fhandler = open(MESSAGE_FILE, 'rt')
    cxt = fhandler.read()
    fhandler.close()
    return json.loads(cxt)

def save_message(username, title, content):
    messages = get_messages()
    publish_date = (datetime.datetime.now() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    messages.append({'username':username, 'title':title, 'content':content,'publish_date':publish_date})
    print(messages)
    fhandler = open(MESSAGE_FILE, 'wt')
    fhandler.write(json.dumps(messages))
    fhandler.close()


