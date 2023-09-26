
from twilio.rest import Client
import random
import keys

FILE_NAME = 'quotes.txt'
f = open(FILE_NAME, "r", encoding='utf-8')
LINES = f.readlines()
random_quote = random.choice(LINES).strip()

def send_text():
    client = Client(keys.ACCOUT_SID, keys.AUTH_TOKEN)
    client.messages \
            .create(
                body=random_quote,
                from_= keys.FROM_NUM,
                to= keys.TO_NUM
            )
    print('Sent Message!')


if __name__ == '__main__':
    send_text()