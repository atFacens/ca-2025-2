# Escreva um programa que leia vários números digitados pelo usuário
# e calcule a média destes números.
# A entrada de dados termina quando o usuário digitar 0 (zero)

soma = 0
numero = 1
cont = 1

#solução 1
# while(numero != 0):
#     msg = 'Digite o '+ str(cont) + 'º número (0=fim): '
#     numero = int(input(msg))
#     if(numero > 0):
#         soma = soma + numero
#         cont += 1

# media = soma / cont
# print('Média = ', media)


#solução 2
while(numero != 0):
    msg = 'Digite o '+ str(cont) + 'º número (0=fim): '
    numero = int(input(msg))
    soma = soma + numero
    cont += 1

media = soma / (cont-1)
print('Média = ', media)