import telepot
from telepot.loop import MessageLoop

def handle(msg):
    print(msg)
    command=msg['text']
    if command=='hola':
        bot.sendMessage(msg['from']['id'], 'Hola '+ msg['from']['first_name'] +' soy Esclavont, tu asistente virtual')
    if command=='foto':
        bot.sendPhoto(msg['from']['id'],photo=open('im1.jpg','rb'))

        
        
bot = telepot.Bot('7187218614:AAH8gD1WZBBCivg5yBYSFXRpSzfYZ0GNPG4')
MessageLoop(bot,handle).run_forever()





