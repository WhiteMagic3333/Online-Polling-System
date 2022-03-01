from twilio.rest import Client
import random

account_sid = 'NA'
auth_token = 'NA'

OTP = str(random.randint(1000,9999))
print(OTP)
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+18624658393',
    body='Your OTP Is = '+(OTP)
    to='+917579249700'
)

print(message.sid)
