# Escreva um programa que leia vários números digitados pelo usuário
# e calcule a média destes números

qtde = int(input('Quantos números você vai digitar? '))
soma = 0

for cont in range(1, qtde+1):
    msg = 'Digite o '+ str(cont) + 'º número de 4: '
    numero = int(input(msg))
    soma = soma + numero

media = soma / qtde
print('Média = ', media)