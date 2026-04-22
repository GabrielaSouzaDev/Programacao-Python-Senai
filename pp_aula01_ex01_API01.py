# Autor: Gabriela Souza
# Desafio API para temperatura

import requests

latitude = float(input('Digite a latitude: '))
longitude = float(input('Digite a longitude: '))

url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

resposta = requests.get(url)
dados = resposta.json()

print(f'Temperatura: {dados["current"]["temperature_2m"]}')
print()
print(f'Velocidade do vento: {dados["current"]["wind_speed_10m"]}')