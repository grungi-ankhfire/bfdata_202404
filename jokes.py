import requests
import json

response = requests.get("https://official-joke-api.appspot.com/random_ten")
data = json.loads(response.text)

print(type(response.text))
print(type(data))

for joke in data:
    print(joke["setup"])