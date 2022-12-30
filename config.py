from ast import Import
from telebot import util
from time import time
import yDados
import time
import telegram
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

api_key = '5462348099:AAHtG3Hm2_cEr0Rcxb8kLoHDBxdMUb7A-LI'  # TOKEN DO SEU BOT
chat_id = '-1001882023401'  # ID DO GRUPO OU CANAL

###############################################################################

gales = 0
voltas = 0
possoLer = False
possoLer1 = False
possoLer2 = False
podeContar = "nao"
contadorDeWIN = 0
contadorDeLOSS = 0
contadorSG = 0
contadorG1 = 0
contadorG2 = 0
total = 0

winconsecutive = 0


#MENSAGEM COM O LINK, QUE VAI TE REDIRECIONAR PARA A PÁGINA DO JOGO


mensagem =  'Aposte Aqui'


class TelegramSTZ():
    def send_message(self, yTOKEN, yCHAT_ID, yMESSAGE):
        yURL = f'https://api.telegram.org/bot{yTOKEN}/'
        yLINK_REQ = f'{yURL}sendMessage?chat_id={yCHAT_ID}&text={yMESSAGE}'
        requests.get(yLINK_REQ)
bot = TelegramSTZ()
#bot.send_message(api_key, chat_id, f"🤖BOT LIGADO🤖") #Caso queira uma um alerta de que ligou o Bot
def martingale():
    global possoLer
    global gales
    global contadorDeWIN
    global contadorDeLOSS
    global contadorSG
    global contadorG1
    global contadorG2   
    global total
    global winconsecutive


    if yDados.ultimoCrash >= 2:
        if gales == 0:
            bot.send_message(api_key, chat_id, f"""

PAAAGA O PAAI✅✅✅✅✅✅            
Crash: {yDados.ultimoCrash}X  🤑""")

            print(f"""✅✅✅✅✅✅✅
Crash: {yDados.ultimoCrash} """)
            contadorSG += 1
            total += 1
            winconsecutive += 1
            print(f"""✅ WINN SEM GALE ✅✅
💰Resultado: {yDados.ultimoCrash}X💰 """)
            bot.send_message(api_key, chat_id, f'''

ESTAMOS A {winconsecutive} GREEN SEGUIDOS 🔥🤑

                ''')
        elif gales == 1:
            contadorG1 += 10
            total += 1
            winconsecutive += 1
            bot.send_message(api_key, chat_id, f"""
PAAAGA O PAAI✅✅✅✅✅✅           
Crash: {yDados.ultimoCrash} 🤑      🔥🔥{gales}""")
            bot.send_message(api_key, chat_id, f'''
            
            ESTAMOS A {winconsecutive} GREEN SEGUIDOS 🔥🤑
                ''')

        elif gales == 2:
            contadorG2 += 1
            total += 1
            winconsecutive += 1
            bot.send_message(api_key, chat_id, f"""
PAAAGA O PAAI✅✅✅✅✅✅           
Crash: {yDados.ultimoCrash} 🤑      🔥🔥🔥{gales}""")
            bot.send_message(api_key, chat_id, f'''
            
            ESTAMOS A {winconsecutive} GREEN SEGUIDOS 🔥🤑
                ''')
            
        possoLer = False
        gales = 0
    elif gales < yDados.martingales:
        gales += 1
        bot.send_message(api_key, chat_id, f"♻ Agora {gales} GALE")
        print(f"♻ Agora {gales} GALE")      
        
    else:
        winconsecutive = 0
        contadorDeLOSS += 1
        bot.send_message(api_key, chat_id, f""" 
        
             
🚨 RED, CALMA VOLTAREMOS APÓS 2 GREEN.
Crash: {yDados.ultimoCrash}X  """)
        print(f"""❌❌❌❌{gales}❌❌❌❌ 
Crash: {yDados.ultimoCrash} """)
        
       
        possoLer = False
        gales = 0
def estrategies():
    global gales
    global voltas
    global podeContar
    global possoLer
    global contadorSG    
    global contadorG1
    global contadorG2
    global winconsecutive
    print(yDados.dadosCrash)
    if possoLer == True:
        martingale()
    if possoLer == False and yDados.dadosCrash[0] <= 1.99 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] <= 1.99:
        possoLer = True
        
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X  
 🌐   {mensagem}   
 

''')

        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 01")

    if possoLer == False and yDados.dadosCrash[0] <= 1.99 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] == 1.20:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X   
 🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 02")

    if possoLer == False and yDados.dadosCrash[0] <= 1.99 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] == 1.22:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X   
 🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 03")

    if possoLer == False and yDados.dadosCrash[0] <= 1.99 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] == 1.25:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X   
 🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 04")

    if possoLer == False and yDados.dadosCrash[0] <= 1.99 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] == 1.27:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X   
 🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 05")

    if possoLer == False and yDados.dadosCrash[0] <= 1.99 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] == 1.28:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X   
 🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 06")

    if possoLer == False and yDados.dadosCrash[0] <= 1.50 and yDados.dadosCrash[1] <= 1.35 and yDados.dadosCrash[2] <= 1.0 and yDados.dadosCrash[3] == 1.29:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X   
 🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 07")

    if possoLer == False and yDados.dadosCrash[0] <= 1.99 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] >= 2:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X   
 🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 08")

    if possoLer == False and yDados.dadosCrash[0] <= 1.99 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] >= 5:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X   
 🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 09")

    if possoLer == False and yDados.dadosCrash[0] <= 1.99 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] >= 3:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X   
 🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 10")

    if possoLer == False and yDados.dadosCrash[0] <= 1.99 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] >= 1.28 and yDados.dadosCrash[4] >= 5:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X   
 🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 11")

    if possoLer == False and yDados.dadosCrash[0] >= 2 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] <= 1.99 and yDados.dadosCrash[4] >= 2:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X   
 🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 12")

    if possoLer == False and yDados.dadosCrash[0] >= 2 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] >= 1.28 and yDados.dadosCrash[4] <= 1.99:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
 🤞    BUSCAR: 2X   
 🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 13")

    if possoLer == False and yDados.dadosCrash[0] >= 5 and yDados.dadosCrash[1] <= 1.99 and yDados.dadosCrash[2] <= 1.99 and yDados.dadosCrash[3] <= 1.99 and yDados.dadosCrash[4] <= 1.99:
        
        possoLer = True
        print(
            f"🚧MENSAGEM EVIADA🚧")
        bot.send_message(api_key, chat_id,
                         f'''

ENTRADA CONFIRMADA: HNCRASH 🥇🏆
 ✅   ENTRAR APÓS: {yDados.dadosCrash[0]}X  ✅
  🤞    BUSCAR: 2X  
  🌐   {mensagem}    ''')
        print(
            f"🚧Sinal encontrado!🚧 VELA 2 PADRÃO 14")


