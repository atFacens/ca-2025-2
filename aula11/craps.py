import random

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
somaDados = dado1 + dado2

print(dado1, dado2, somaDados)

if(somaDados == 7 or somaDados == 11):
    print('O jogador ganhou de primeira!!!')
else:
    if(somaDados == 2 or somaDados == 3 or somaDados == 12):
        print('O jogador perdeu de primeira...')
    else:
        objetivo = somaDados
        fimDeJogo = False
        while(not fimDeJogo):
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            somaDados = dado1 + dado2
            print('obj:',objetivo, dado1, dado2, 'soma:',somaDados)
            if(somaDados == objetivo):
                print('Jogador Ganhou!')
                fimDeJogo = True
            else:
                if(somaDados == 7):
                    print('Jogador Perdeu...')
                    fimDeJogo = True
        

