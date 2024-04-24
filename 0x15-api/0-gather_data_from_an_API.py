#!/usr/bin/python3
"""request api and print details for users taskS """


import requests
import sys

user_id = int(sys.argv[1])
url_todo = "https://jsonplaceholder.typicode.com/todos/"
url_user = "https://jsonplaceholder.typicode.com/users" + "/" + sys.argv[1]
task_num = 0
done = 0
task_name = []
response = requests.get(url=url_todo)
user_name = requests.get(url=url_user)
users = user_name.json()
data = response.json()

name = users['name']
for dicts in data:
    if user_id == dicts['userId']:
        task_num += 1
        if dicts['completed'] is True:
            task_name.append(dicts['title'])
            done += 1

print(f"Employee {name} is done with tasks({done}/{task_num}):")
for task in task_name:
    print(f"\t {task}")
