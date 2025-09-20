
dia = 0

if(dia == 0):
    print('Domingo')
else:
    if(dia == 1):
        print('Segunda-feira')
    else:       
        if(dia == 2):
            print('Terça-feira')
        else:       
            if(dia == 3):
                print('Quarta-feira')
            else:       
                print('Outro')

# match case

numero = 0
match numero:
    case 0: print('Domingo')
    case 1: print('Segunda-feira')
    case 2: print('Terça-feira')
    case 3: print('Quarta-feira')
    case _: print('Outro')

