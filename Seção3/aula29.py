'''
introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''

numero_str = input('Digite um número: ')


try:
    numero_float = float(numero_str)
    print(f'o dobro o numero {numero_float} é {numero_float * 2:.2f}')
except:
    print('Você não digitou um número válido.')




