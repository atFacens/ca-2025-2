
entrada = input('Digite um número inteiro: ')
numero = int(entrada)

if(numero > 0):
    print('Esse valor é positivo')
else:
    if(numero < 0):
        print('Esse valor é negativo')
    else:
        print('Esse valor é zero')