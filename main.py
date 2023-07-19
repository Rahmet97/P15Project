import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(reciever_email, code):
    # Email configuration
    sender_email = 'ruslanovrahmet@gmail.com'
    subject = 'Account activation'
    message = f'Your activation code is: {code}'

    # SMTP server configuration for gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'ruslanovrahmet@gmail.com'
    smtp_password = 'cvkhnrmxfgaeqlwu'

    # Create a multipart message and set headers
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = reciever_email
    email_message['Subject'] = subject

    email_message.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        server.send_message(email_message)
