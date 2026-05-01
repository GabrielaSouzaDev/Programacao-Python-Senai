# Autor: Gabriela Souza
# Função com evl


# opala é variavel para 1° valor
# chevette é variavel para 2° valor
# mecanico é a veriavel para operação

def calcular(opala, mecanico, chevette):
    # CUIDADOOO!!
    # eval - executa expressão em um texto string
    return eval(f'{opala}{mecanico}{chevette}')

n1 = float(input('Digite o 1° valor: '))
n2 = float(input('Digite o 2° valor: '))
op = input('Escolha a operação: ')

print('O resultado é ', calcular(n1,op,n2))