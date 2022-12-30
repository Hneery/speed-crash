import requests
import yDados
from config import estrategies

url = 'https://blaze.com/api/crash_games/recent'

yDadosCrash = []


def Atualizando_Dados():
    global url

    while True:
        try:
            results = requests.get(
                url).json()
            break
        except:
            continue

    lista = []

    for i in results:
        lista.append(float(i["crash_point"]))
    yDados.dadosCrash = lista
    yDados.ultimoCrash = float(lista[0])


while True:
    Atualizando_Dados()

    if yDados.dadosCrash != yDadosCrash:
        yDadosCrash = yDados.dadosCrash
        estrategies()
