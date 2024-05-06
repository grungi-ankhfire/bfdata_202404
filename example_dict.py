
# id  |   username    |   email
# 42  |   bkorissen   |   kadomony@gmail.com
# 1   |   admin       |   admin@important.com
# ...

users_dict = {
    "id": [42, 1],
    "username": ["bkorissen", "admin"],
    "email": ["kadomony@gmail.com", "admin@important.com"]
}

users_list = [
    {"id": 42, "username": "bkorissen", "email": "kadomony@gmail.com"},
    {"id": 1, "username": "admin", "email": "admin@important.com"},
]

users_dict["username"][0] = "bgorissen"
users_list[0]["username"] = "bgorissen"


scores = {"a":4, "b":6, "c":3}
print(max(scores.values()))
for name, score in scores.items():
    print(f"{name} has {score} points")
