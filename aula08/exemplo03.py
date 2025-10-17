#  Leia 5 valores e some somente os positivos

cont = 1 
soma = 0

while(cont <= 5): 
    numero = int(input('Digite um número: '))
    cont = cont + 1
    if numero < 0:
        continue # volte ao início do laço
    soma = soma + numero

print(soma)