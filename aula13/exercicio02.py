# Um consultório atende adultos e jovens (menos 18 anos) apenas
# No início do dia temos uma lista de atendimentos contendo a idade
# de cada paciente a ser atendido
# Escreva um programa que, dada a lista de idades, conte quantos
# pacientes são adultos e quantos são jovens

idades = [14, 43, 17, 16, 32, 21, 20, 32, 12, 29]

numero_adultos = 0
# numero_jovens = 0

for idade in idades:
    if(idade > 17):
        numero_adultos += 1
    # else:
    #     numero_jovens += 1

print('Adultos =', numero_adultos)
# print('Jovens =', numero_jovens)
print('Jovens =', len(idades) - numero_adultos)