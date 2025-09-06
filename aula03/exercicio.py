# Um jogador passa de fase em um game quando ele atinge pelo menos 1000 pontos e
# ele encontra as 3 chaves que abrem a porta do final da fase.

# Sua tarefa é escrever um código em Python que verifica se o jogador pode ir para 
# a próxima fase do game

# Entrada de Dados / Processamento / Saída(resposta)

entrada = input('Quantos pontos você fez? ')
pontos = int(entrada)

entrada = input('Quantas chaves você encontrou? ')
chaves = int(entrada)

passaDeFase = pontos >= 1000 and chaves == 3

print('Passou de fase?', passaDeFase)