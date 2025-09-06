#  Operadores Lógicos
#  E(AND) OU(OR) NÃO(NOT)
#   and or not

estaSol = True
ehFeriado = True

vouParaAPraia = estaSol and ehFeriado

print('Vou para a praia?', vouParaAPraia)

tenhoLampadaIgual = False
tenhoLamparaEquivalente = False

trocarALampada = tenhoLampadaIgual or tenhoLamparaEquivalente

print('troca a lampada?', trocarALampada)

print('Não tenho lampada igual:', not tenhoLampadaIgual )