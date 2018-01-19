from django.db import models
import json
import time
# Create your models here.

MESSAGE_FILE = 'message.json'

def get_messages():
	fhandler = open(MESSAGE_FILE,'rt')
	cxt = fhandler.read()
	fhandler.close()
	return json.loads(cxt)


def save_message(username,title,content):
	messages = get_messages()
	message = {"username":username,"title":title,"content":content,
	           "publish_date":time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
	           }
	messages.append(message)

	fhandler = open(MESSAGE_FILE,'w')
	fhandler.write(json.dumps(messages))
	fhandler.close()
	return True


