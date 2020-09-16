
#wnload the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC4099aa1cb7d039a0a0755047a9c51243'
auth_token = '36eeb082d0a4e025a0539489f212874a'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+16614855373',
                     to='+18625886618'
                 )

print(message.sid)
