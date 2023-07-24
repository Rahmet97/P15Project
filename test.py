from databases import *


# first_name = input('first name: ')
# last_name = input('last name:')
# email = input('email:')
# birth_day = input('birth day:')
username = input('username: ')
password = input('password: ')
# password2 = input('password confirm: ')
#
# if password1 == password2:
#     if user_is_exist('username', username):
#         raise Exception("Username already exists!")
#     if user_is_exist('email', email):
#         raise Exception("Email already exists!")
#     data = dict(
#         first_name=first_name,
#         last_name=last_name,
#         birth_day=birth_day,
#         email=email,
#         username=username,
#         password=password1
#     )
#     insert_user(data)
#     print("Success")
# else:
#     raise Exception("Password are not same!")

response = login(username, password)
if response:
    print("Logged in")
else:
    raise Exception("Username or password invalid!")

if __name__ == '__main__':
    create_table_user()