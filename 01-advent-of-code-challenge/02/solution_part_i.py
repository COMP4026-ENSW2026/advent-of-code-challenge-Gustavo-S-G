# A, X = Rock = 1
# B, Y = Paper = 2
# C, Z = Scissors = 3

# Win = 6
# Lose = 0
# Draw = 3

# A X = 1 + 3 = 4
# A Y = 2 + 6 = 8
# A Z = 3 + 0 = 3
# B X = 1 + 0 = 1
# B Y = 2 + 3 = 5
# B Z = 3 + 6 = 9
# C X = 1 + 6 = 7
# C Y = 2 + 0 = 2
# C Z = 3 + 3 = 6


soma = 0

with open("sample.in", "r") as f:
    data = f.read().splitlines()
    
    for i in range(0, len(data)):

        if data[i] == "A X":
            soma += int(4)
        elif data[i] == "B X":
            soma += int(1)
        elif data[i] == "C X":
            soma += int(7)
        elif data[i] == "A Y":
            soma += int(8)
        elif data[i] == "B Y":
            soma += int(5)
        elif data[i] == "C Y":
            soma += int(2)
        elif data[i] == "A Z":
            soma += int(3)
        elif data[i] == "B Z":
            soma += int(9)
        elif data[i] == "C Z":
            soma += int(6)
        else:
            print("Error")
    
    print(f'Meu score: {soma}')
