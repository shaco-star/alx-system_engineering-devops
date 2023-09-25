#!/usr/bin/python3
"""Return tasks for an employee and save in to JSON file"""

import json
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'

    user = requests.get(url+'/users', params={'id': id}).json()
    tasks = requests.get(url+'/todos', params={'userId': id}).json()

    if isinstance(user, list):
        user = user[0]
    username = user['username']

    file_name = f'{id}.JSON'
    with open(file_name, "w") as jsonfile:
        json.dump(
                {id: [{"task": t.get("title"), "completed": t.get(
                    "completed"), "username": username}
                    for t in tasks]}, jsonfile)
