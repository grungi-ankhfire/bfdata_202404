import requests

response = requests.get("https://api.parrycarry.com/coin/flip")

print(response.text)