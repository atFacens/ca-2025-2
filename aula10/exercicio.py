candidato1 = 0
candidato2 = 0
candidato3 = 0
brancos = 0
nulos = 0
numero_eleitores = 0

numero_eleitores = int(input('Quantos eleitores teremos? '))

for cont in range(1, numero_eleitores+1):
    print('1-4 = voto do seu candidato, 4 = branco')
    voto = int(input('Qual seu voto? '))

    match voto:
        case 1: candidato1 += 1
        case 2: candidato2 += 1
        case 3: candidato3 += 1
        case 4: brancos += 1
        case _: nulos += 1

votos_validos = numero_eleitores - brancos - nulos

print('-------------------------------------------------')
print('Candidato 1: ', candidato1, " - ", (candidato1 / votos_validos) * 100, "%")
print('Candidato 2: ', candidato2, " - ", (candidato2 / votos_validos) * 100, "%")
print('Candidato 3: ', candidato3, " - ", (candidato3 / votos_validos) * 100, "%")
print('Brancos: ', brancos, " - ", (brancos / numero_eleitores) * 100, "%")
print('Nulos: ', nulos, " - ", (nulos / numero_eleitores) * 100, "%")


vencedor = 0 # começa assumindo empate

#verifica se um deles teve mais votos
if(candidato1 > candidato2 and candidato1 > candidato3):
    vencedor = 1
else:
    if(candidato2 > candidato1 and candidato2 > candidato3):
        vencedor = 2
    else:
        if(candidato3 > candidato1 and candidato3 > candidato2):
            vencedor = 3   

print("*** Resultado: ***")
if(vencedor == 0):
    print('Tivemos um empate!')
else:
    print('O candidato', vencedor, ' ganhou a eleição!')