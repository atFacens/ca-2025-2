# Crie uma função chamada estatisticas que recebe 
# uma lista de números e retorna um dicionário contendo a média, 
# o maior valor, o menor valor e a mediana dos números.

def estatisticas(lista): 
    lista_ordenada = sorted(lista)
    # print(lista_ordenada)
    maior = max(lista)
    menor = min(lista)
    # print(menor, maior)
    tamanho = len(lista_ordenada)
    if(tamanho % 2 == 0):
        mediana = (lista_ordenada[tamanho // 2 -1] + lista_ordenada[tamanho // 2]) / 2
    else:
        mediana = lista_ordenada[tamanho // 2]
    # print(mediana)

    dados = {
        "menor":menor,
        "maior":maior,
        "mediana":mediana 
    }

    return dados


retorno = estatisticas([3, 7, 1, 9, 2, 10, 6])

print(retorno)