


with open('sample.in', 'r') as f:
    linhas = f.readline().strip()

for i in range(len(linhas)):
    if len(set(linhas[i:i+14]))==14:
        print(i+14)
        break