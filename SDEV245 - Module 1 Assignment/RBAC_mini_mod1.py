#Kody Fatch, Module 1 Assignment: RBAC and Authentication mini-app
#Functions
def login_user():
    login = 0
    while login == 0:
        username = input("Enter your username:\n")
        password = input("Enter your password:\n")
        if username in user_list and user_list[username]["password"] == password:
            login += 1
            print("User Found. Login Successful")
            return username
        else:
            print("User or Password was Incorrect. Please Try Again.")
def check_user(user):
    if user_list[user]["role"] == "user":
        role = "user"
        print("USER'S ASSIGNED ROLE: 'USER'")
        return role
    elif user_list[user]["role"] == "admin":
        role = "admin"
        print("USER'S ASSIGNED ROLE: 'ADMIN'")
        return role
    else:
        print("ROLE NOT ASSIGNED FOR ENTERED USER")

#List of users and the associated password and role
user_list = {"user":{"password":"userpass", "role":"user"}, "admin":{"password":"adminpass", "role":"admin"}}

#Authentication
current_user = login_user()

#Authorization
user_role = check_user(current_user)

#Output
print(f"Login Process Complete. Welcome! User Credentials Listed.\nCurrent User: {current_user}\nCurrent Role: {user_role}\nYou can now access the '{user_role}' dashboard.")

#This simple app for RBAC and Authentication shows the 'Confidentiality' part of the CIA Triad in Cybersecurity. It checks if the user is in the list of users and it checks
#the role of said user. This limits the access to only people on the user list and rescricts the privileges based on roles assigned.