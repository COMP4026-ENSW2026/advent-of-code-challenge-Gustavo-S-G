


with open('sample.in', 'r') as f:
    data = f.readlines()
    pares_att = [entry.strip() for entry in data]

    def is_range_a_in_range_b(range_a, range_b):
        start_a, end_a = map(int, range_a.split('-'))
        start_b, end_b = map(int, range_b.split('-'))
        return start_b <= start_a and end_a <= end_b

    sobreposicoes = 0

    for par_att in pares_att:
        first_range, second_range = par_att.split(',')
        start_a, end_a = map(int, first_range.split('-'))
        start_b, end_b = map(int, second_range.split('-'))
        if start_a in range(start_b, end_b+1) or end_a in range(start_b, end_b+1) or  start_b in range(start_a, end_a+1) or end_b in range(start_a, end_a+1):
            sobreposicoes += 1
    sobreposicoes

print(sobreposicoes)