#!/usr/bin/python3
""" returns information about his/her TODO list progress. """

import json
import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(api_url + "users/{}".format(sys.argv[1])).json()
    todolist = requests.get(
            api_url + "todos", params={"userId": sys.argv[1]}).json()

    # uses list comprehension and adds to tc if condition are met
    tasks_complete = [tc.get(
        "title") for tc in todolist if tc.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.json().get("name"), len(tasks_complete), len(todolist)))
    for i in tasks_complete:
        print("  {}".format(i))
