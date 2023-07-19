from databases import create_table_user, insert_user, login, activate_user
from main import send_mail
from utils import generate_code, generate_token

data = dict(
    first_name = input("Enter your first name: "),
    last_name = input("Enter your last name: "),
    email = input("Enter your email: "),
    username = input("Enter your username: "),
    password1 = input("Enter your password: "),
    password2 = input("Password confirm: ")
)

user = dict(
    username=input('username: '),
    password=input('password: ')
)

# response = insert_user(data)
# if response == 201:
#     code = generate_code()
#     send_mail(data['email'], code)
#     print('Check your email')

#     verification = input("code: ")
#     if verification == code:
#         activate_user({'username': data['username']})
#         print('Done')
#     else:
#         print('Invalid code!')


response = login(user)
if response:
    print("Welcome to our website")
else:
    print("Invalid username or password!")

if __name__ == '__main__':
    create_table_user()
