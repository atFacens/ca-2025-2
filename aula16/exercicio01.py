# Escreva um programa em Python que leia uma palavra digitada pelo usuário e:

# 1. informe a quantidade de caracteres da palavra
# 2. exiba cada uma das letra da palavra separadamente
# 3. exiba a palavra ao contrário
# 4. verifique se a palavra digitada é um palíndromo: lida ao contrário é "igual"
# ex: ovo

palavra = input('Digite uma palavra: ')
print('Você digitou:', palavra)

# 1
numero_de_letras = len(palavra)
print('Esta palavra tem', numero_de_letras, 'letras')

#2
for i in range(numero_de_letras):
    print(palavra[i], end=' ')

print()

#3
# pos = numero_de_letras - 1
# while(pos > -1):
#     print(palavra[pos], end=' ')
#     pos -= 1

# print()

for i in range(numero_de_letras-1, -1, -1):
    print(palavra[i], end=' ')

print()

#4
posicao_inicial = 0
posicao_final = numero_de_letras - 1
palindromo = True

while(posicao_inicial < posicao_final and palindromo == True):
    if(palavra[posicao_inicial] != palavra[posicao_final]):
        palindromo = False
    posicao_inicial += 1
    posicao_final -= 1

if(palindromo == True):
    print('A palavra é um palindromo')
else:
    print('A palavra NÃO é um palindromo')

