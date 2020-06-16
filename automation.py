from twilio.rest import Client 
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 

def send_msg():
    message = client.messages.create( 
                              from_='whatsapp:',  
                              body='',      
                              to='whatsapp:' 
                          ) 
    print(message.sid)
