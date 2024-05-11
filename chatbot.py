import telepot
from telepot.loop import MessageLoop

global paso
paso=0
global comenzar
comenzar=False
global info
info ={}
global empresa
empresa=""


def handle(msg):
    global comenzar
    global paso
    global info
    global empresa
    
    print(msg)
    command=msg['text']

    if command=='Hola' and comenzar==False:
        bot.sendMessage(msg['from']['id'], 'Hola '+ msg['from']['first_name'] +' soy Esclavont, tu asistente virtual')
        bot.sendMessage(msg['from']['id'],'Para empezar en que empresa trabajas?:')
        
        
    elif command in ["comenzar","Comenzar","start","Start"] or comenzar:
        comenzar=True
        if paso==0:
            paso=1
            bot.sendMessage(msg['from']['id'],'Comenzaremos con la encuesta!')
            bot.sendMessage(msg['from']['id'],'Módulo 1: Responsabilidad')
            bot.sendMessage(msg['from']['id'],'¿Estás consciente de si la empresa ha establecido responsabilidades claras para gestionar los riesgos de esclavitud moderna y ha implementado políticas al respecto?')
            bot.sendMessage(msg['from']['id'],'¿Sabes si hay responsabilidades establecidas a nivel de la Junta Directiva?\n1. Sí\n2. No\n3. No sé')
        elif paso==1:
            verificar("respuesta1a",command)
            paso=2
            bot.sendMessage(msg['from']['id'],'¿Tienes conocimiento de algún grupo de trabajo o persona encargada a nivel operativo que maneje estos temas?\n1. Sí\n2. No\n3. No sé')

        elif paso==2:
            verificar("respuesta1b",command)
            paso=3
            bot.sendMessage(msg['from']['id'],'Módulo 2: Estrategia')
            bot.sendMessage(msg['from']['id'],'¿Has sido informado o tienes conocimiento de alguna estrategia aprobada por la Junta Directiva para manejar los riesgos de esclavitud moderna en nuestra empresa?\n1. Sí\n2. No\n3. No sé')
        elif paso==3:
            verificar("respuesta2",command)
            paso=4
            bot.sendMessage(msg['from']['id'], 'Módulo 3: Debida Diligencia')
            bot.sendMessage(msg['from']['id'],'En relación con nuestro compromiso contra la esclavitud moderna, ¿sabías que tenemos políticas que:')
            bot.sendMessage(msg['from']['id'],'¿Han sido aprobadas por nuestros líderes? \n1. Sí\n2. No\n3. No sé')
        elif paso==4:
            verificar("respuesta3a",command)
            paso=5
            bot.sendMessage(msg['from']['id'],'¿Se han compartido públicamente?\n1. Sí\n2. No\n3. No sé')

        elif paso==5:
            verificar("respuesta3b",command)
            paso=6
            bot.sendMessage(msg['from']['id'],'Módulo 4: Política de Implementación')
            bot.sendMessage(msg['from']['id'],'En cuanto a las políticas específicas contra la esclavitud moderna en nuestra empresa, ¿te han informado si:')
            bot.sendMessage(msg['from']['id'],'¿Se han comunicado a las personas clave dentro de la empresa?\n1. Sí\n2. No\n3. No sé')
        elif paso==6:
            verificar("respuesta4a",command)
            paso=7
            bot.sendMessage(msg['from']['id'],'¿Se han integrado en los procesos operativos relevantes??\n1. Sí\n2. No\n3. No sé')
        elif paso==7:
            verificar("respuesta4b",command)
            paso=8
            bot.sendMessage(msg['from']['id'],'¿Se han incluido en las cláusulas contractuales?\n1. Sí\n2. No\n3. No sé')
        elif paso==8:
            verificar("respuesta4c",command)
            paso=9
            bot.sendMessage(msg['from']['id'],'¿Se han incorporado en las capacitaciones que ofrecemos?\n1. Sí\n2. No\n3. No sé')
        elif paso==9:
            verificar("respuesta4d",command)
            paso=10
            bot.sendMessage(msg['from']['id'],'Módulo 5: Reportes')
            bot.sendMessage(msg['from']['id'],'En relación con las violaciones de nuestras políticas, incluyendo las relacionadas con la esclavitud moderna, ¿sabes si reportamos estas situaciones:')
            bot.sendMessage(msg['from']['id'],'¿Internamente a los ejecutivos y al Consejo?\n1. Sí\n2. No\n3. No sé')
        elif paso==10:
            verificar("respuesta5a",command)
            paso=11
            bot.sendMessage(msg['from']['id'],'¿Públicamente en nuestros informes de sostenibilidad u otros documentos?\n1. Sí\n2. No\n3. No sé')
        elif paso==11:
            verificar("respuesta5b",command)
            paso=12
            bot.sendMessage(msg['from']['id'],'Módulo 6: Evaluación de Riesgos')
            bot.sendMessage(msg['from']['id'],'¿Estás al tanto de cómo la empresa ha evaluado y dado prioridad a los riesgos de esclavitud moderna y explotación en:')
            bot.sendMessage(msg['from']['id'],'¿Nuestras propias operaciones y entre los empleados?\n1. Sí\n2. No\n3. No sé')
        elif paso==12:
            verificar("respuesta6a",command)
            paso=13
            bot.sendMessage(msg['from']['id'],'¿Nuestros proveedores directos (Nivel 1)?\n1. Sí\n2. No\n3. No sé')
        elif paso==13:
            verificar("respuesta6b",command)
            paso=14
            bot.sendMessage(msg['from']['id'],'¿Más allá de los proveedores de Nivel 1, incluyendo algunos de nuestras materias primas y otras relaciones comerciales, como nuestros clientes?\n1. Sí\n2. No\n3. No sé')
        elif paso==14:
            verificar("respuesta6c",command)
            paso=15
            bot.sendMessage(msg['from']['id'],'Módulo 7: Prácticas de Empleo')
            bot.sendMessage(msg['from']['id'],'Sobre las prácticas de empleo en nuestra empresa, nos gustaría saber tu opinión y conocimiento respecto a lo siguiente:')
            bot.sendMessage(msg['from']['id'],'¿Consideras que te pagan un salario justo?\n1. Sí\n2. No\n3. No sé')
        elif paso==15:
            verificar("respuesta7a",command)
            paso=16
            bot.sendMessage(msg['from']['id'],'¿Recibes tu salario y otros beneficios a tiempo?\n1. Sí\n2. No\n3. No sé')
        elif paso==16:
            verificar("respuesta7b",command)
            paso=17
            bot.sendMessage(msg['from']['id'],'¿Te piden trabajar horas extras excesivas?\n1. Sí\n2. No\n3. No sé')
        elif paso==17:
            verificar("respuesta7c",command)
            paso=18
            bot.sendMessage(msg['from']['id'],'¿Tuviste que pagar alguna cuota para obtener tu trabajo?\n1. Sí\n2. No\n3. No sé')
        elif paso==18:
            verificar("respuesta7d",command)
            paso=19
            bot.sendMessage(msg['from']['id'],'¿Te sientes en alguna forma de deuda por condiciones vinculadas a tu empleo?\n1. Sí\n2. No\n3. No sé')
        elif paso==19:
            verificar("respuesta7e",command)
            paso=20
            bot.sendMessage(msg['from']['id'],'¿Tu lugar de trabajo y condiciones de vida son seguros y sanitarios?\n1. Sí\n2. No\n3. No sé')
        elif paso==20:
            verificar("respuesta7f",command)
            paso=21
            bot.sendMessage(msg['from']['id'],'¿Tu contrato está redactado en un idioma que entiendes?\n1. Sí\n2. No\n3. No sé')
        elif paso==21:
            verificar("respuesta7g",command)
            paso=22
            bot.sendMessage(msg['from']['id'],'¿Tienes acceso a tu pasaporte o documentos de identidad cuando lo necesitas?\n1. Sí\n2. No\n3. No sé')
        elif paso==22:
            verificar("respuesta7h",command)
            paso=23
            bot.sendMessage(msg['from']['id'],'¿Te sientes libre de dejar tu trabajo o alojamiento cuando lo deseas?\n1. Sí\n2. No\n3. No sé')
        elif paso==23:
            verificar("respuesta7i",command)
            paso=24
            bot.sendMessage(msg['from']['id'],'¿Crees que tus intereses están adecuadamente representados, por ejemplo, a través de sindicatos o asociaciones laborales?\n1. Sí\n2. No\n3. No sé')
        elif paso==24:
            verificar("respuesta7j",command)
            paso=25
            bot.sendMessage(msg['from']['id'],'¿Se verifica la edad de todos los trabajadores para prevenir el trabajo infantil?\n1. Sí\n2. No\n3. No sé')
        elif paso==25:
            verificar("respuesta7k",command)
            paso=26
            bot.sendMessage(msg['from']['id'],'¿Existe discriminación en el lugar de trabajo?\n1. Sí\n2. No\n3. No sé')
        elif paso==26:
            verificar("respuesta7l",command)
            paso=27
            bot.sendMessage(msg['from']['id'],'Módulo 8: Compromiso de proveedores y debida diligencia')
            bot.sendMessage(msg['from']['id'],'Nos gustaría conocer tu percepción sobre cómo nuestra empresa evalúa y maneja los riesgos de esclavitud moderna en nuestra cadena de suministro')
            bot.sendMessage(msg['from']['id'],'¿Sabes si hacemos preguntas sobre las prácticas laborales y políticas de nuestros proveedores?\n1. Sí\n2. No\n3. No sé')
        elif paso==27:
            verificar("respuesta8a",command)
            paso=28
            bot.sendMessage(msg['from']['id'],'¿Estás al tanto de si realizamos visitas o auditorías sociales en los sitios de nuestros proveedores?\n1. Sí\n2. No\n3. No sé')
        elif paso==28:
            verificar("respuesta8b",command)
            paso=29
            bot.sendMessage(msg['from']['id'],'¿Sabes si interactuamos con los trabajadores de nuestros proveedores a través de encuestas, entrevistas o aplicaciones móviles?\n1. Sí\n2. No\n3. No sé')
        elif paso==29:
            verificar("respuesta8c",command)
            paso=30
            bot.sendMessage(msg['from']['id'],'¿Utilizamos otras herramientas de evaluación de riesgos, como la trazabilidad o herramientas de mapeo de riesgos?\n1. Sí\n2. No\n3. No sé')
        elif paso==30:
            verificar("respuesta8d",command)
            paso=31
            bot.sendMessage(msg['from']['id'],'¿Participamos con organizaciones de la sociedad civil para comprender mejor los riesgos?\n1. Sí\n2. No\n3. No sé')
        elif paso==31:
            verificar("respuesta8e",command)
            paso=32
            bot.sendMessage(msg['from']['id'],'¿Estás informado si nuestra empresa publica una lista de sus proveedores?\n1. Sí\n2. No\n3. No sé')
        elif paso==32:
            verificar("respuesta8f",command)
            paso=33
            bot.sendMessage(msg['from']['id'],'Módulo 9: Prácticas de compra')
            bot.sendMessage(msg['from']['id'],'En relación con nuestras prácticas de compra, como los precios de los contratos, las previsiones y los incentivos a proveedores, ¿crees que estas prácticas podrían aumentar los riesgos para los trabajadores de nuestros proveedores?\n1. Sí\n2. No\n3. No sé')
        elif paso==33:
            verificar("respuesta9",command)
            paso=34
            bot.sendMessage(msg['from']['id'],'Módulo 10: Evaluación y Medición')
            bot.sendMessage(msg['from']['id'],'Nos interesa saber tu opinión sobre los mecanismos de quejas disponibles')
            bot.sendMessage(msg['from']['id'],'¿Estás al tanto de algún proceso de quejas que nosotros, como empleados, podemos usar?\n1. Sí\n2. No\n3. No sé')
        elif paso==34:
            verificar("respuesta10a",command)
            paso=35
            bot.sendMessage(msg['from']['id'],'¿Sabes si existe algún mecanismo de quejas que puedan utilizar partes externas como proveedores, trabajadores de nuestros proveedores y comunidades afectadas por nuestras actividades?\n1. Sí\n2. No\n3. No sé')
        elif paso==35:
            verificar("respuesta10b",command)
            paso=36
            bot.sendMessage(msg['from']['id'],'¿Conoces si requerimos que nuestros proveedores clave tengan mecanismos de quejas y que compartan información sobre las quejas relacionadas con nuestro negocio?\n1. Sí\n2. No\n3. No sé')
        elif paso==36:
            verificar("respuesta10c",command)
            paso=37
            bot.sendMessage(msg['from']['id'],'Módulo 11: Respuesta y remediación')
            bot.sendMessage(msg['from']['id'],'Queremos saber tu percepción sobre cómo respondemos a situaciones problemáticas relacionadas con nuestra empresa')
            bot.sendMessage(msg['from']['id'],'¿Estás informado sobre algún proceso documentado que describa nuestra responsabilidad para remediar daños que hayamos causado, contribuido o que estén directamente vinculados a nuestras actividades?\n1. Sí\n2. No\n3. No sé')
        elif paso==37:
            verificar("respuesta11a",command)
            paso=38
            bot.sendMessage(msg['from']['id'],'¿Este proceso incluye pasos claros para investigar y remediar una violación crítica de políticas o un incidente de esclavitud moderna?\n1. Sí\n2. No\n3. No sé')
        elif paso==38:
            verificar("respuesta11b",command)
            paso=39
            bot.sendMessage(msg['from']['id'],'¿Crees que nuestros procesos nos han permitido identificar y remediar (o colaborar en la remediación de) incidentes de esclavitud moderna o explotación relacionada?\n1. Sí\n2. No\n3. No sé')
        elif paso==39:
            verificar("respuesta11c",command)
            #convert info to csv
            with open(empresa+'.csv','a') as f:
                for key in info.keys():
                    f.write("%s;"%(info[key]))
                f.write("\n")
            paso=0
    else:
        empresa = command
        # print(empresa)
        bot.sendMessage(msg['from']['id'], 'Para comenzar la encuesta escribe "Comenzar"')
    
    

def verificar(id, command):
    if command=='1':
        info[id]="Si"
        return "Si"
    elif command=='2':
        info[id]="No"
        return "No"
    else:
        info[id]="Inseguro"
        return "Inseguro"

bot = telepot.Bot('7187218614:AAH8gD1WZBBCivg5yBYSFXRpSzfYZ0GNPG4')
MessageLoop(bot,handle).run_forever()





