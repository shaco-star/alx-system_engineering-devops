#!/usr/bin/python3
"""Return completed tasks for an employee"""
import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'

    user = requests.get(url+'/users', params={'id': id}).json()
    tasks = requests.get(url+'/todos', params={'userId': id}).json()

    if isinstance(user, list):
        user = user[0]

    total_tasks = len(tasks)
    done_tasks = [task for task in tasks if task['completed']]

    print("Employee {} is done with tasks({}/{}):".format(
        user['name'], len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t{}".format(task['title']))
