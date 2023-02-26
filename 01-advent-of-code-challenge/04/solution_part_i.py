

with open('sample.in', 'r') as f:
    data = f.readlines()
    pares_att = [entry.strip() for entry in data]

    def is_range_a_in_range_b(range_a, range_b):
        start_a, end_a = map(int, range_a.split('-'))
        start_b, end_b = map(int, range_b.split('-'))
        return start_b <= start_a and end_a <= end_b

    contador = 0

    for par_att in pares_att:
        first_range, second_range = par_att.split(',')
        if is_range_a_in_range_b(first_range, second_range) or is_range_a_in_range_b(second_range, first_range):
            contador += 1
    contador

print(contador)