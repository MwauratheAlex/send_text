from twilio.rest import Client 
import config
 
account_sid = config.account_sid
auth_token = config.auth_token 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(
                                messaging_service_sid=config.messaging_service_sid, 
                                body="Hello again, from space. I am the enlightened one.",         
                                to='+254713958070'

                          ) 
 
print(message.sid)