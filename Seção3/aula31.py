"""
flag(bandeira) - marcar um local
None = não valor
is e is not = é ou nao é (tipo, valor, identidade)
id = identidade de um objeto (endereço de memória)
"""

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print("meus ovinhos")
else:
    print('meus ovinhos 2')

if passou_no_if is None:
    print("não passou no if")

if passou_no_if is not None:
    print("passou no if")
