contador = 0

while contador <= 100:
    contador += 1
    if contador == 6:
        print('pulando o número 6')
        continue
    if contador >= 10 and contador <= 27:
        print('pulando o número', contador)
        continue
    
    print(contador)
    if contador == 40:
        print('chegou no número 40')
        break
