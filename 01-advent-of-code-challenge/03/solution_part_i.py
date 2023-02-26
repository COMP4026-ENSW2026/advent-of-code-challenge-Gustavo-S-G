with open('sample.in', 'r') as f:
    data = f.readlines()
    sacos = [entry.strip() for entry in data]

    soma_sacos = 0

    for saco in sacos:
         
        first_half = set(saco[:len(saco)//2])
        second_half = set(saco[len(saco)//2:])
        
        overlap_char = (first_half.intersection(second_half)).pop()

        if overlap_char.isupper():
            soma_sacos += ord(overlap_char) - ord('A') + 27
        else:
            soma_sacos += ord(overlap_char) - ord('a') + 1
    soma_sacos

print(soma_sacos)