"""
repetições
while(enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito quando um codigo nao tem fim
"""
condicao = True

while condicao:
    nome = input("qual o seu nome: ")
    if nome == "sair":
        break
    print(f"seu nome é {nome}")
   