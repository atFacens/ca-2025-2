# escreva um programa que leia uma frase digitada pelo usuário e:
# 1. conte quantas vogais existem na frase
# 2. monte uma nova frase removendo todas as vogais da frase anterior

frase = input('Digite uma frase: ')
lista = []
numero_vogais = 0
numero_letras = len(frase)

frase = frase.lower()

for i in range(numero_letras):
    if(frase[i] == 'a' or frase[i] == 'e' or frase[i] == 'i' or frase[i] == 'o' or frase[i] == 'u'):
        numero_vogais += 1
    else:
        lista.append(frase[i])
    
print('Esta frase tem', numero_vogais, 'vogais')

frase_sem_vogais = ''.join(lista)
print('Frase sem as vogais:', frase_sem_vogais)
