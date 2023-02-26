

with open('sample.in', 'r') as f:
    linhas = f.readline().strip()

for i in range(len(linhas)):
    if len(set(linhas[i:i+4]))==4:
        print(i+4)
        break