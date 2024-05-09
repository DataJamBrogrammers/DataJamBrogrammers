import telepot
from telepot.loop import MessageLoop

def handle(msg):
    print(msg)
    command=msg['text']
    if command=='salude':
        bot.sendMessage(902264668, 'hola')
    if command=='foto':
        bot.sendPhoto(902264668,photo=open('im1.jpg','rb'))

        
        
bot = telepot.Bot('7187218614:AAH8gD1WZBBCivg5yBYSFXRpSzfYZ0GNPG4')
MessageLoop(bot,handle).run_forever()





