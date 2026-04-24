# Autor: Gabriela Souza
# Desafio API de temperatura com API de CEP

import requests
# API CEP
cep = int(input('Digite um cep [apenas números]'))
url_cep = f'https://viacep.com.br/ws/{cep}/json/'
resposta_cep = requests.get(url_cep)
dados_cep = resposta_cep.json()

# Tratamento de erros
if "erro" in dados_cep:
    print('CEP não encontrado!')
else:
    cidade = dados_cep["localidade"]
    print(f'Cidade encontrada: {cidade}')

# API Geocoding (trazendo latitude e longitude da cidade)
url_localidade = f'https://open-meteo.com{cidade}&count=1&language=pt'
resposta_localidade = requests.get(url_localidade)
dados_localidade = resposta_localidade.json()

if "resultado" in dados_localidade:
    latitude = dados_localidade["results"][0]["latitude"]
    longitude = dados_localidade["results"][0]["longitude"]

    # API Temperatura
    url_clima = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'

    resposta_clima = requests.get(url_clima)
    dados_clima = resposta.json()

    print(f'Condições em {cidade}:')
    print(f'Temperatura: {dados_clima["current"]["temperature_2m"]}°C')
    print(f'Velocidade do vento: {dados_clima["current"]["wind_speed_10m"]}')
else:
    print("Coordenadas da cidade não encontradas.")