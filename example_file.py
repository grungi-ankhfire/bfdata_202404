import pandas as pd
import requests
import json

url = "https://api.frankfurter.app/2024-03-01..?to=USD"

response = requests.get(url)
data = response.text

with open("dump.txt", "w") as file:
    file.write(data)

with open("dump.txt", "r") as file:
    data = file.read()

class MyClass:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f"Super objet MyClass avec number = {self.number}"

    def __enter__(self):
        print("Inside Enter!")
        return self
    
    def __exit__(self, *args):
        print(f"Inside Exit! {args}")

m = MyClass(5)
print(m)

with MyClass(7) as truc:
    print(truc.number)


