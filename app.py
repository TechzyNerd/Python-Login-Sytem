import json

# load user from json file
try:
    with open("users.json", "r") as file:
        users = json.load(file)
except FileNotFoundError:
    users = {}   # if file doesn't exist, create an empty user list


print("Welcome to Login System Python v1.")

print("\nAre you already a user (Y/N):")
already_user = input().strip()


# Register new user
if already_user.lower() == "n":
    print("Create a username:")
    new_username = input().strip()

    print("Create a password:")
    new_password = input().strip()

    # save new user into the  dictionary.
    users[new_username] = new_password

    # save to file json
    with open("users.json", "w") as file:
        json.dump(users, file)

    print("\nAccount created and saved! You can now login.\n")


# Login User
print("Login - Please enter your username:")
login_username = input().strip()

print("Enter your password:")
login_password = input().strip()

# check login 
if login_username in users and users[login_username] == login_password:
    print("\nLogin successful! Welcome,", login_username)
else:
    print("\nLogin failed! Wrong username or password.")
