# importing the client from the twilio
from twilio.rest import Client
# Your Account Sid and Auth Token from twilio account
account_sid = "AC2da7f495136d1dc9706d80b3b36adc4f"
auth_token = "136fc9affccf2a81923a94911fa7f715"
# instantiating the Client
client = Client(account_sid, auth_token)
# sending message
message = client.messages.create(body='Hi there! How are you?', from_="+19705913359", to="+919455129077") 
# printing the sid after success
print(message.sid)

# buHDWzR52p-wPyy-99n7mn3P8FiNiRlxwZUekVWp