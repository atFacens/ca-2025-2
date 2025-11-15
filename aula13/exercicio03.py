# Dado um conjunto contendo o número de itens vendidos em 20 dias de trabalho,
# deseja-se saber:
# - a quantidade total de itens vendidos
# - a media de vendas por dia
# - qual a maior quantidade de itens vendidos

vendas = [20, 21, 30, 15, 10, 12, 22, 25, 9, 32, 40, 15, 23, 43, 32, 11, 9, 7, 10, 12]

total_vendas = sum(vendas)
print('Total de vendas:', total_vendas)

media_vendas = total_vendas / len(vendas)
print('Média de vendas:', media_vendas)

maior = vendas[0] # assume que o maior é o primeiro
for i in range(len(vendas)):
    if(vendas[i] > maior): # se encontrou alguém maior, esse passa a ser o maior
       maior = vendas[i]

print('A maior quantidade de vendas foi:', maior)