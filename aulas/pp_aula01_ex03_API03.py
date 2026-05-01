# Autor: Gabriela Souza
# Desafio API para conversor de moeda

import requests

real = float(input('Digite o valor em reais: '))

url = f'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
resposta = requests.get(url)
dados = resposta.json()

dolar = float(dados["USDBRL"]["bid"])
euro = float(dados['EURBRL']['bid'])
bitcoin = float(dados['BTCBRL']['bid'])

conversao_dolar = real / dolar
conversao_euro = real / euro
conversao_bitcoin = real / bitcoin

print(f'Com R${real:.2f} você terá U${conversao_dolar:.2f}dolares')
print(f'Com R${real:.2f} você terá U${conversao_euro:.2f} euros')
print(f'Com R${real:.2f} você terá U${conversao_bitcoin:.2f} bitcoins')