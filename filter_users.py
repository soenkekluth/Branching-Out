import json

""" filter users by age """


def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user.get("age") == age]

    for user in filtered_users:
        print(user)


""" filter users by email address """


def filter_users_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [
        user for user in users if user.get("email", "").lower() == email.lower()
    ]

    for user in filtered_users:
        print(user)
