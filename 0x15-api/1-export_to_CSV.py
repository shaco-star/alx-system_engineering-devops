#!/usr/bin/python3
"""Return tasks for an employee and save in to csv file"""
import sys
import requests
import csv

if __name__ == "__main__":
    id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'

    user = requests.get(url+'/users', params={'id': id}).json()
    tasks = requests.get(url+'/todos', params={'userId': id}).json()

    if isinstance(user, list):
        user = user[0]
    username = user['username']

    file_name = f'{id}.csv'
    with open(file_name, 'w', newline='') as file:
        write = csv.writer(file)
        [write.writerow(
            [id, username, task['completed'], task['title']]
            ) for task in tasks]
