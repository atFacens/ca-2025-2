# Escreva um programa que leia uma lista de nomes de pessoas
# e exiba a lista em ordem alfabética

nomes = []

for i in range(5):
    nome = input('Digite o próximo nome: ')
    nomes.append(nome)

nomes.sort()

print(nomes)
