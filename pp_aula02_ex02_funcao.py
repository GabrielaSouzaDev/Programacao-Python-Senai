# Autor: Gabriela Souza
# Operações com função

# Variáveis globais do sistema
valor1 = float(input('Digite o 1° valor: '))
valor2 = float(input('Digite o 2° valor: '))

# Função para calculos
def calcular(valor1, valor2):
    # Variáveis locais da função
    soma = valor1 + valor2
    subtracao = valor1 - valor2
    multiplicacao = valor1 * valor2
    divisao = valor1 / valor2



    print(f'''
          A soma é {soma} 
          a subtração é {subtracao} 
          a multiplicação é {multiplicacao} 
          e a divisão é {divisao}
          ''')


# Chamando a função
calcular(valor1, valor2)