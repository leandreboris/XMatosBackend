
from twilio.rest import Client

import socket



account_sid = "AC39f8ed0dedd29b3c82da085715de5c11"
auth_token = "8720b746571b50538b3ca500f4bfb0c9"
client = Client(account_sid, auth_token)
def send_sms(user_code, phone_number):
    message = client.messages \
                .create(
                     body=f"Hi! Your verification code is {user_code}",
                     from_='',
                     to =f'{phone_number}',
                 )

    print(message.sid)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    try:
        socket.inet_aton(ip)
        return ip
    except socket.error:
        return "IP address not found"

