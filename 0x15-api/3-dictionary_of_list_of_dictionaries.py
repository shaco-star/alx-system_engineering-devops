#!/usr/bin/python3
"""Return tasks for all employees and save into JSON file"""
import json
import requests

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(url + "/users").json()

    user_tasks = {
        user.get("id"): [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        } for task in requests.get(
            url + "/todos", params={"userId": user.get("id")}).json()]
        for user in users
    }

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(user_tasks, jsonfile)
