# Autor: Gabriela Souza
# Função com dicionarios]

def calcular(a, b, op):
    operacoes = {
        # () -> tuplas - imultavel
        # [] -> listas - multavel
        '+': a + b ,
        '-': a - b ,
        '*': a * b ,
        '/': a / b,
        '**': a ** b,
        '//': a // b,
        '%': a % b
    }
    return operacoes [op]

n1 = float(input('Digite o 1° valor: '))
n2 = float(input('Digite o 2° valor: '))
op = input('Digite a operação desejada: ')

print(calcular(n1,n2,op))