# aprovado se média >= 7
# exame se média >= 5
# reprovado se média < 5

media = 4

if(media >= 7):
    print('Aprovado')
else:
    if(media >= 5):
        print('Exame')
    else:
        print('Reprovado')

if(media < 5):
    print('Reprovado')
else:
    if(media < 7):
        print('Exame')
    else:
        print('Aprovado')