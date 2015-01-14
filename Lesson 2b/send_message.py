from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC88555de32f60c450aa22dff0bad88698"
auth_token  = "19d3c75648fbf04fc75dc40bc3b4adf3" 
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hey Whats up man!!",
    to="+13019060318",    # Replace with your phone number
    from_="+12402933569") # Replace with your Twilio number
print message.sid 
