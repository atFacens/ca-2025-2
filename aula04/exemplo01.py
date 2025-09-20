

tenhoLampadaIgual = False
tenhoLamparaEquivalente = False

trocarALampada = tenhoLampadaIgual or tenhoLamparaEquivalente

if(trocarALampada == True): # SE a condição for verdadeira
    print('Sim! Vou trocar a lâmpada') # será feito SOMENTE se a condição do IF for True
    print('segundo comando do IF')
else:  # SENÃO (caso contrário)
    print('Não! Não vou trocar a Lâmpada')
    print('segundo comando do ELSE')

print('Estou fora')