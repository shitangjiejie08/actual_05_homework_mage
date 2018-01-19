from django.db import models

import json

# Create your models here.

USERS_FILE = 'conf/users.txt'

def get_users():
    with open(USERS_FILE, 'rt') as f:
        users = f.read()
    return json.loads(users)

def save_users(users):
    with open(USERS_FILE, 'wt') as f:
        f.write(json.dumps(users))

def list_users(users, list_mode):
    users_list = sorted(list(users.values()), key=lambda x: x.get(list_mode))
    for user in users_list:
        user['password'] = '*' * len(user['password'])
    return users_list

def find_users(users, name):
    users_list = []
    for user in users.values():
        if user['name'].find(name) != -1:
            user['password'] = '*' * len(user['password'])
            users_list.append(user)
    return users_list