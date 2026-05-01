# QUEM PERMITE ACESSAR?
import requests

# ENTRADA DE DADOS - CEP DESEJADO
cep = input('Digite seu cep: ')

# PEGAR O ENDEREÇO DA INTERNET QUE TEM TODOS OS CEPS
url = f'https://viacep.com.br/ws/{cep}/json/'

# BUSCAR A INFORMAÇÃO CONTIDA NA URL
resposta = requests.get(url)

# DICIONÁRIO COM TODOS OS DADOS
dados = resposta.json()


# MONTAGEM DO ENDEREÇO
print(f"Logradouro: {dados['logradouro']}")
print(f"Bairro: {dados['bairro']}")
print(f"Cidade: {dados['localidade']}")
print(f"UF: {dados['uf']}")
