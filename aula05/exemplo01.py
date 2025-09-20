numero = 17
resto = numero % 2 # % significa resto da divisão

if(resto == 0):
    resposta = "Número par"
else:
    resposta = "Número impar"

print(resposta)

# if ternário

resposta = "Número par" if resto == 0 else "Número impar"
print(resposta)
