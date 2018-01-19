#encoding: utf-8
from django.db import models

class User(models.Model):
    username=models.CharField(max_length=64)
    age=models.IntegerField()
    tel=models.CharField(max_length=64)
    password=models.CharField(max_length=512)

    def __str__(self):
        tpl = '<User:[username={username}, age={age}, tel={tel},password={password},id={id}]>'
        return tpl.format(id=self.id,username=self.username, age=self.age, tel=self.tel,password=self.password)
