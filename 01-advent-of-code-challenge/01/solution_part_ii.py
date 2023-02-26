import sys

valores = []
soma = 0

for linhas in sys.stdin:
    if linhas != "\n":
        soma += int(linhas)
    else:    
        valores.append(soma)
        soma = 0

valores.sort(reverse=True)
soma = valores[0] + valores[1] + valores[2]

print(f'Soma das calorias carregadas pelos 3 elfos com mais calorias: {soma}')