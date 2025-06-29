primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

if primeiro_valor == '' or segundo_valor == '':
    print("Um dos valores está vazio. Por favor, insira valores válidos.")

elif primeiro_valor > segundo_valor:
    print(f"O primeiro valor ({primeiro_valor}) é maior que o segundo valor ({segundo_valor}).")

elif primeiro_valor < segundo_valor:
    print(f"O primeiro valor ({primeiro_valor}) é menor que o segundo valor ({segundo_valor}).")

elif primeiro_valor == segundo_valor:
    print(f"O primeiro valor ({primeiro_valor}) é igual ao segundo valor ({segundo_valor}).")


else:
    print("Erro inesperado. Verifique os valores inseridos.")

