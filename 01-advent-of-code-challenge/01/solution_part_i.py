import sys

soma = 0
alto = 0

for linhas in sys.stdin:

    if linhas != "\n":
        soma += int(linhas)
    else:
        if soma > alto:
            alto = soma
        soma = 0

print(f'Total de calorias carregadas pelo elfo com mais calorias: {alto}')