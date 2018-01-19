from django.db import models

# Create your models here.
import json

MESSAGE_FILE = 'messages.json'

def get_messages():
	fhandler = open(MESSAGE_FILE,'rt')
	cxt = fhandler.read()
	fhandler.close()
	return json.loads(cxt)

def save_message(publish_date,username,title,content):
	messages = get_messages()
	message = {"publish_date":publish_date,"username":username,"title":title,"content":content}
	messages.append(message)
	fhandler = open(MESSAGE_FILE,'w')
	fhandler.write(json.dumps(messages))
	fhandler.close()
	return  True
