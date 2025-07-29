import json
import requests
import random

class Employee:
    def __init__(self):
        self.name = ""
        self.salary = 0

    def get_placeholder(self):
        json_response_text = requests.get("https://randomuser.me/api/").text
        json_response = json.loads(json_response_text)
        self.name = json_response["results"][0]["name"]["first"] + " " + json_response["results"][0]["name"]["last"]
        self.salary = random.randint(1000, 10_000)


if __name__ == "__main__":
    employee = Employee()
    employee.get_placeholder()
    print(employee.name, employee.salary)
