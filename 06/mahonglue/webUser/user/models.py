from django.db import models
import json
# Create your models here.
file_path = "messages.json"

def get_message():
    fhandler = open(file_path,"rt")
    cxt = json.loads(fhandler.read())
    fhandler.close()
    return cxt

class Users(models.Model):
    username = models.CharField(max_length=20)
    tel = models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username