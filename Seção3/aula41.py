# while/ else GB

string = 'valor qualquer'
i = 0
while i < len(string):
    letra = string[i]

    print(letra)
    i+= 1
else:
    print('o else foi executado.')
print('Fim do loop while.')

# se tiver break o else nao vai ser executado