# for variavel in sequencia:
#     bloco de codigo 
#     instruções

frutas = ['maçã', 'banana', 'laranja', 'uva']

for fruta in frutas:
    print(f"{fruta} ta podi")

condição = 90

mudanca = input("Digite uma numero que nao seja zero: ")
condição = int(mudanca)
while condição > 0 and mudanca != "0":
    print(f"Condição é {condição}")
    condição -= 1

print("Fim do loop")


    