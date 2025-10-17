cont = 1 
soma = 0

while(cont <= 5): 
    numero = int(input('Digite um número: '))
    if numero < 0:
        break # interrompe a execução do laço
    soma = soma + numero
    cont = cont + 1

print(soma)