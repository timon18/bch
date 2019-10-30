import os

user_json = 'data/user.json'

try:
    fp = open(user_json)
except IOError:
    os.makedirs('data')
