#! /usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib


def md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()