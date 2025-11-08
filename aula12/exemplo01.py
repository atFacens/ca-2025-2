
numeros = [2, 4, 5, 1, 3, 8, 6]

print(numeros)

print('primeiro:', numeros[0])
print('segundo:', numeros[1])

numeros.append(10)
print(numeros)

print('Qtos números:', len(numeros))

# numeros = 7
# numeros[3] = "hoje"

numeros[3] = 7
print('alterado:',numeros)

# Calculando a média dos valores
tamanho = len(numeros)
soma  = 0
for i in range(tamanho):
    soma += numeros[i]

print('media:', soma/tamanho)

# numeros.sort()
numeros.sort(reverse=True)
print(numeros)

