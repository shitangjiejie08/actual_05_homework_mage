#encoding: utf-8
from django.db import models

class Message2(models.Model):
    username=models.CharField(max_length=256)
    title=models.CharField(max_length=512)
    content=models.TextField(max_length=256)
    publish=models.DateTimeField()


    def __str__(self):
        tpl = '<Message2:[username={username}, title={title}, content={content}, publish={publish}]>'
        return tpl.format(username=self.username, title=self.title, content=self.content, publish=self.publish)
