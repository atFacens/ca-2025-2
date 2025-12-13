# Escreva uma função chamada calcular_media, que recebe três números 
# como parâmetros e retorna a média desses números. 
# Em seguida, escreva um código que chame essa função 
# com diferentes conjuntos de valores e exiba os resultados.

def calcular_media(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    return media

print(calcular_media(10, 20, 30))
print(calcular_media(5, 15, 25))