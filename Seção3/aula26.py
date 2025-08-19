nome = input('Qual o seu nome?: ')
idade = int(input('Qual a sua idade?: '))

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'e você tem {idade} anos.')
    print(f'seu nome tem {len(nome)} letras.')
    if ' ' in nome:
        print('Seu nome tem espaços.')
    else:
        print('Seu nome não tem espaços.')

else:
    print('Desculpe, você deixou campos vazios.')
# Obs: O comando nome[::-1] inverte a string.
