while True:
    escolha = input('Escolha uma opção: [1] Continuar [2] Sair: ')
    if escolha == '1':
        print('Você escolheu continuar.')
        print('por favor escolha dois numeros e a operação desejada')
        num1 = input('Digite o primeiro número: ')
        num2 = input('Digite o segundo número: ')
        print('+ = adição, - = subtração, * = multiplicação, / = divisão')
        operacao = input('Digite a operação (+, -, *, /): ')
        num1int = int(num1)
        num2int = int(num2)
        resultado = None
        try:
            if operacao == '+':
                resultado = num1int + num2int
                print(f'O resultado da adição é: {resultado}')
            elif operacao == '-':
                resultado = num1int - num2int
                print(f'O resultado da subtração é: {resultado}')
            elif operacao == '*':
                resultado = num1int * num2int
                print(f'O resultado da multiplicação é: {resultado}')
            elif operacao == '/':
                resultado = num1int / num2int
                print(f'O resultado da divisão é: {resultado}')
            else:
                print('Operação inválida seu merda coloca esta bosta direito')
            
        except ValueError:
            print('Erro: escreva numero nessa caceta, plmds o tal do usuario é um merda memo viu')
        continue
    if escolha == '2':
        print('Você escolheu sair.')
        break
        