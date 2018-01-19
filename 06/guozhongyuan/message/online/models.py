from django.db import models

# Create your models here.

import json

MESSAGE_FILE = 'message.json'

def get_messages():

	fandler = open(MESSAGE_FILE,'rt')
	cxt = fandler.read()
	fandler.close()
	
	return json.loads(cxt)


def save_message(username,title,content):

	messages = get_messages()
	message = {'username':username,'title':title,'content':content}
	messages.append(message)

	fandler = open(MESSAGE_FILE, 'w')
	fandler.write(json.dumps(messages))
	fandler.close()





