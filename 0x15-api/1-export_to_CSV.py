#!/usr/bin/python3
"""request api and print details for users taskS """


import requests
import sys
import csv

if __name__ == "__main__":
    user_id = sys.argv[1]
    url_todo = "https://jsonplaceholder.typicode.com/todos/"
    url_user = "https://jsonplaceholder.typicode.com/users" + "/" + user_id
    dict_list = []
    fields = ["userId", "name", "completed", "title"]
    response = requests.get(url=url_todo)
    user_name = requests.get(url=url_user)
    users = user_name.json()
    data = response.json()

    name = users['name']
    csv_dict = {'name': name, 'userId': user_id, 'completed': True, 'title': ''}
    for dicts in data:
        if int(user_id) == dicts['userId']:
            csv_dict['completed'] = dicts['completed']
            csv_dict['title'] = dicts['title']
            dict_list.append(csv_dict)
    file = user_id + ".csv"
    with open(file, 'w') as cs:
        writer = csv.DictWriter(cs, fieldnames=fields)
        print(dict_list)
        writer.writerows(dict_list)