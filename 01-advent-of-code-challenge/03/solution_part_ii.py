with open('sample.in', 'r') as f:
    data = f.readlines()
    sacos = [entry.strip() for entry in data]

    soma_sacos = 0

    while len(sacos) > 0:
        # take out first 3 entries
        primeiro_saco = set(sacos.pop())
        segundo_saco = set(sacos.pop())
        terceiro_saco = set(sacos.pop())
        # get overlap through set logic (intersection of two sets applied twice)
        overlap_char = ((primeiro_saco.intersection(segundo_saco)).intersection(terceiro_saco)).pop()

        # translate to ascii and substract the base ('A' is 65, 'B' is 66 and so on) and add the new base
        if overlap_char.isupper():
            soma_sacos += ord(overlap_char) - ord('A') + 27
        else:
            soma_sacos += ord(overlap_char) - ord('a') + 1
        soma_sacos

print(soma_sacos)