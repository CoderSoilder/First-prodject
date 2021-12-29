from twilio.rest import Client

account_sid = "Your twilio account sid"
auth_token = "Your twilio auth token"
twilio_number = "Your twilio number"

# Numbers to report to

target1 = "Your number"

client = Client(account_sid, auth_token)

while True:
  message = client.messages.create(
    body="Message",
    from_=twilio_number,
    to=target1
  )
  
  print(message.body)
  
# WARNING when you make an twilio account you will start with $15 but it will coast around 5 cents per message!
