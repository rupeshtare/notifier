from twilio.rest import Client
from tasks import celery


# Your Account SID from twilio.com/console
account_sid = "AC7703861baf93a9a5c7f5aaf7f6d373b9"

# Your Auth Token from twilio.com/console
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)


@celery.task
def send_sms():
    client.messages.create(to="+919021767832",
                           from_="+18312564228",
                           body="Hello from Python!")
