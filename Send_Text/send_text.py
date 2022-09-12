from twilio.rest import Client 
 
account_sid = 'ACb8b6800e7f2e942632489dfaa51372b8' 
auth_token = '47689d7e9e2a3e1fc3c6ff45b2e14e35' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(messaging_service_sid='MG6ab586cd8c37151b0786f05405172749', body='teste', to='+5527988146188') 
 
print(message.sid)
