#  Leia 5 valores positivos e some 

cont = 1 
soma = 0

while(cont <= 5): 
    numero = int(input('Digite um número: '))
    if numero < 0:
        continue # volte ao início do laço
    soma = soma + numero
    cont = cont + 1

print(soma)