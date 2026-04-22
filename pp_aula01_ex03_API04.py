# Autor: Gabriela Souza
# Desafio API para conversor de moeda
# [Versão do Professor]

import requests


url = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
resposta = requests.get(url)
dados = resposta.json()

valor_dolar = dados['USDBRL']['bid']
valor_euro = dados['EURBRL']['bid']
valor_bitcoin = dados['BTCBRL']['bid']

print(f'A cotação atual do Dólar é {valor_dolar}')
print(f'A cotação atual do Euro é {valor_euro}')
print(f'A cotação atual do Bitcoin é {valor_bitcoin}')