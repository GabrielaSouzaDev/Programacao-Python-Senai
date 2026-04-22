# Autor: Gabriela Souza
# Desafio API de temperatura com API de CEP

import requests
# API CEP
cep = int(input('Digite um cep [apenas números]'))
url_cep = f'https://viacep.com.br/ws/{cep}/json/'
resposta_cep = requests.get(url_cep)
dados_cep = resposta_cep.json()

cidade = resposta_cep["localidade"]
url_localidade = f'https://geocoding-api.open-meteo.com/v1/search'

# API Temperatura
latitude = resposta_cep
longitude = resposta_cep

url_clima = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

resposta = requests.get(url_clima)
dados = resposta.json()

print(f'Temperatura: {dados["current"]["temperature_2m"]}')
print()
print(f'Velocidade do vento: {dados["current"]["wind_speed_10m"]}')