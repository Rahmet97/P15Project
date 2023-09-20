from celery_app import send

result = send.delay(
    'ruslanovrahmet@gmail.com',
    'rahmetruslanov6797@gmail.com',
    'mythmyth363@gmail.com',
    'abrayovjasurbek@gmail.com'
)

print('Testing...')