#!/usr/bin/env python3
#coding=utf-8
"""
# Author: huangyisan
# Created Time : 一  5/ 8 01:22:27 2017
# File Name: test.py
# Description:

"""
import json
def get_messages():
    f = open('messages.json','rt')
    cxt = f.read()
    f.close()
    return json.loads(cxt)
a=get_messages()
print(type(a))
for i in a:
    print(i)
