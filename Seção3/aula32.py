"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numint = input("Digite um número inteiro: ")


try:
    numintT = int(numint)
    if numintT % 2 == 0:
        print(f"{numintT} é par")
    else:
        print(f"{numintT} é ímpar")
except ValueError:
    print("Não é um número inteiro")



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input("Digite a hora (0-23): "))

if hora < 12:
    print("Bom dia!")

elif hora >= 12 and hora < 18:
    print("Boa tarde!")

elif hora >= 18 and hora < 24:
    print("Boa noite!")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Digite seu primeiro nome: ")

if len(nome) <= 4:
    print("Seu nome é curto")

elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome é normal")

elif len(nome) > 6:
    print("Seu nome é muito grande")