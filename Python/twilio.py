from twilio.rest import Client
import time
import twilioKey


# Configuración de Twilio
account_sid = twilioKey.account_sid
auth_token = twilioKey.auth_token
client = Client(account_sid, auth_token)

# Letra de la canción
lyrics = "I used to rule the world, seas would rise when I gave the word..."

# Envío del mensaje
for i in range(2):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="I used to rule the world, seas would rise when I gave the word...",
        to='whatsapp:+4143936561'
    )
    time.sleep(30)
