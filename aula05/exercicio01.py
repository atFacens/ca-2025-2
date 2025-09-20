# Escreva um programa que leia dois valores e 
# uma das operações matemáticas (+, -, *, /)
# e exiba o resultado da operação
# utilize o match para as decisões


entrada = input('Digite o primeiro número: ')
numero1 = float(entrada)

entrada = input('Digite o segundo número: ')
numero2 = float(entrada)

operacao = input('Qual a operação( + - * / ): ')

match operacao:
    case '+': print(' = ',(numero1 + numero2))
    case '-': print(' = ',(numero1 - numero2))
    case '*': print(' = ',(numero1 * numero2))
    case '/': 
        # if(numero2 == 0):
        #     print('Divisão por zero não existe')
        # else:
        #     print(' = ',(numero1 / numero2))
        resposta = (numero1 / numero2) if numero2 != 0 else 'Divisão por zero não existe'
        print(resposta)
    case _: print('Operação não implementada')