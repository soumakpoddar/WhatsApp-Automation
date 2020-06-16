from twilio.rest import Client 
 
account_sid = 'AC5f61e3052f385d74032821a95f887c13' 
auth_token = '533c43986b79c8a20db31c8e694931df' 
client = Client(account_sid, auth_token) 

def send_msg():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hii man....',      
                              to='whatsapp:+918972869633' 
                          ) 
    print(message.sid)