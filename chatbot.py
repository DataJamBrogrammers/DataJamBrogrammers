import telepot
from telepot.loop import MessageLoop

global paso
paso=0
global comenzar
comenzar=False


def handle(msg):
    SI = "Si"
    NO = "No"
    INSEGURO = "Inseguro"
    global respuesta1a, respuesta1b, respuesta2, respuesta3a, respuesta3b, respuesta4a, respuesta4b, respuesta4c, respuesta4d, respuesta5a, respuesta5b, respuesta6a, respuesta6b, respuesta6c, respuesta7a, respuesta7b, respuesta7c, respuesta7d, respuesta7e, respuesta7f, respuesta7g, respuesta7h, respuesta7i, respuesta7j, respuesta7k, respuesta7l, respuesta8a, respuesta8b, respuesta8c, respuesta8d, respuesta8e, respuesta8f, respuesta9, respuesta10a, respuesta10b, respuesta10c, respuesta11a, respuesta11b, respuesta11c
    global comenzar
    global paso
    print(msg)
    command=msg['text']

    if command=='Hola' and comenzar==False:
        bot.sendMessage(msg['from']['id'], 'Hola '+ msg['from']['first_name'] +' soy Esclavont, tu asistente virtual')
    
    elif command in ["comenzar","Comenzar","start","Start"] or comenzar:
        comenzar=True
        if paso==0:
            paso=1
            bot.sendMessage(msg['from']['id'],'Comenzaremos con la encuesta!')
            bot.sendMessage(msg['from']['id'],'Módulo 1: Responsabilidad')
            bot.sendMessage(msg['from']['id'],'¿Estás consciente de si la empresa ha establecido responsabilidades claras para gestionar los riesgos de esclavitud moderna y ha implementado políticas al respecto?')
            bot.sendMessage(msg['from']['id'],'¿Sabes si hay responsabilidades establecidas a nivel de la Junta Directiva?\n1. Sí\n2. No\n3. No sé')
        elif paso==1:
            respuesta1a=verificar(command)
            paso=2
            bot.sendMessage(msg['from']['id'],'¿Tienes conocimiento de algún grupo de trabajo o persona encargada a nivel operativo que maneje estos temas?\n1. Sí\n2. No\n3. No sé')

        elif paso==2:
            respuesta1b=verificar(command)
            paso=3
            bot.sendMessage(msg['from']['id'],'Módulo 2: Estrategia')
            bot.sendMessage(msg['from']['id'],'¿Has sido informado o tienes conocimiento de alguna estrategia aprobada por la Junta Directiva para manejar los riesgos de esclavitud moderna en nuestra empresa?\n1. Sí\n2. No\n3. No sé')
        elif paso==3:
            respuesta2=verificar(command)
            paso=4
            bot.sendMessage(msg['from']['id'], 'Módulo 3: Debida Diligencia')
            bot.sendMessage(msg['from']['id'],'En relación con nuestro compromiso contra la esclavitud moderna, ¿sabías que tenemos políticas que:')
            bot.sendMessage(msg['from']['id'],'¿Han sido aprobadas por nuestros líderes? \n1. Sí\n2. No\n3. No sé')
        elif paso==4:
            respuesta3a=verificar(command)
            paso=5
            bot.sendMessage(msg['from']['id'],'¿Se han compartido públicamente?\n1. Sí\n2. No\n3. No sé')

        elif paso==5:
            respuesta3b=verificar(command)
            paso=6
            bot.sendMessage(msg['from']['id'],'Módulo 4: Política de Implementación')
            bot.sendMessage(msg['from']['id'],'En cuanto a las políticas específicas contra la esclavitud moderna en nuestra empresa, ¿te han informado si:')
            bot.sendMessage(msg['from']['id'],'¿Se han comunicado a las personas clave dentro de la empresa?\n1. Sí\n2. No\n3. No sé')
        elif paso==6:
            respuesta4a=verificar(command)
            paso=7
            bot.sendMessage(msg['from']['id'],'¿Se han integrado en los procesos operativos relevantes??\n1. Sí\n2. No\n3. No sé')
        elif paso==7:
            respuesta4b=verificar(command)
            paso=8
            bot.sendMessage(msg['from']['id'],'¿Se han incluido en las cláusulas contractuales?\n1. Sí\n2. No\n3. No sé')
        elif paso==8:
            respuesta4c=verificar(command)
            paso=9
            bot.sendMessage(msg['from']['id'],'¿Se han incorporado en las capacitaciones que ofrecemos?\n1. Sí\n2. No\n3. No sé')
        elif paso==9:
            respuesta4d=verificar(command)
            paso=10
            bot.sendMessage(msg['from']['id'],'Módulo 5: Reportes')
            bot.sendMessage(msg['from']['id'],'En relación con las violaciones de nuestras políticas, incluyendo las relacionadas con la esclavitud moderna, ¿sabes si reportamos estas situaciones:')
            bot.sendMessage(msg['from']['id'],'¿Internamente a los ejecutivos y al Consejo?\n1. Sí\n2. No\n3. No sé')
        elif paso==10:
            respuesta5a=verificar(command)
            paso=11
            bot.sendMessage(msg['from']['id'],'¿Públicamente en nuestros informes de sostenibilidad u otros documentos?\n1. Sí\n2. No\n3. No sé')
        elif paso==11:
            respuesta5b=verificar(command)
            paso=12
            bot.sendMessage(msg['from']['id'],'Módulo 6: Evaluación de Riesgos')
            bot.sendMessage(msg['from']['id'],'¿Estás al tanto de cómo la empresa ha evaluado y dado prioridad a los riesgos de esclavitud moderna y explotación en:')
            bot.sendMessage(msg['from']['id'],'¿Nuestras propias operaciones y entre los empleados?\n1. Sí\n2. No\n3. No sé')
        elif paso==12:
            respuesta6a=verificar(command)
            paso=13
            bot.sendMessage(msg['from']['id'],'¿Nuestros proveedores directos (Nivel 1)?\n1. Sí\n2. No\n3. No sé')
        elif paso==13:
            respuesta6b=verificar(command)
            paso=14
            bot.sendMessage(msg['from']['id'],'¿Más allá de los proveedores de Nivel 1, incluyendo algunos de nuestras materias primas y otras relaciones comerciales, como nuestros clientes?\n1. Sí\n2. No\n3. No sé')
        elif paso==14:
            respuesta6c=verificar(command)
            paso=15
            bot.sendMessage(msg['from']['id'],'Módulo 7: Prácticas de Empleo')
            bot.sendMessage(msg['from']['id'],'Sobre las prácticas de empleo en nuestra empresa, nos gustaría saber tu opinión y conocimiento respecto a lo siguiente:')
            bot.sendMessage(msg['from']['id'],'¿Consideras que te pagan un salario justo?\n1. Sí\n2. No\n3. No sé')
        elif paso==15:
            respuesta7a=verificar(command)
            paso=16
            #TODO: seguir
            bot.sendMessage(msg['from']['id'],'...\n1. Sí\n2. No\n3. No sé')
    if command=='foto':
        bot.sendPhoto(msg['from']['id'],photo=open('im1.jpg','rb'))

def verificar(command):
    if command=='1':
        return "Si"
    elif command=='2':
        return "No"
    else:
        return "Inseguro"

bot = telepot.Bot('7187218614:AAH8gD1WZBBCivg5yBYSFXRpSzfYZ0GNPG4')
MessageLoop(bot,handle).run_forever()


global respuesta1a, respuesta1b, respuesta2, respuesta3a, respuesta3b, respuesta4a, respuesta4b, respuesta4c, respuesta4d, respuesta5a, respuesta5b, respuesta6a, respuesta6b, respuesta6c, respuesta7a, respuesta7b, respuesta7c, respuesta7d, respuesta7e, respuesta7f, respuesta7g, respuesta7h, respuesta7i, respuesta7j, respuesta7k, respuesta7l, respuesta8a, respuesta8b, respuesta8c, respuesta8d, respuesta8e, respuesta8f, respuesta9, respuesta10a, respuesta10b, respuesta10c, respuesta11a, respuesta11b, respuesta11c
respuesta1a = None
respuesta1b = None

respuesta2 = None

respuesta3a = None
respuesta3b = None

respuesta4a = None
respuesta4b = None
respuesta4c = None
respuesta4d = None

respuesta5a = None
respuesta5b = None

respuesta6a = None
respuesta6b = None
respuesta6c = None

respuesta7a = None
respuesta7b = None
respuesta7c = None
respuesta7d = None
respuesta7e = None
respuesta7f = None
respuesta7g = None
respuesta7h = None
respuesta7i = None
respuesta7j = None
respuesta7k = None
respuesta7l = None

respuesta8a = None
respuesta8b = None
respuesta8c = None
respuesta8d = None
respuesta8e = None
respuesta8f = None

respuesta9 = None

respuesta10a = None
respuesta10b = None
respuesta10c = None

respuesta11a = None
respuesta11b = None
respuesta11c = None




