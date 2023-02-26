# A = Rock = 1
# B = Paper = 2
# C = Scissors = 3

# Z = Win = 6
# Y = Draw = 3
# X = Lose = 0

# A X = 3 + 0 = 3
# A Y = 1 + 3 = 4
# A Z = 2 + 6 = 8
# B X = 1 + 0 = 1
# B Y = 2 + 3 = 5
# B Z = 3 + 6 = 9
# C X = 2 + 0 = 2
# C Y = 3 + 3 = 6
# C Z = 1 + 6 = 7


soma = 0

with open("sample.in", "r") as f:
    data = f.read().splitlines()
    
    for i in range(0, len(data)):
        if data[i] == "A X":
            soma += int(3)
        elif data[i] == "B X":
            soma += int(1)
        elif data[i] == "C X":
            soma += int(2)
        elif data[i] == "A Y":
            soma += int(4)
        elif data[i] == "B Y":
            soma += int(5)
        elif data[i] == "C Y":
            soma += int(6)
        elif data[i] == "A Z":
            soma += int(8)
        elif data[i] == "B Z":
            soma += int(9)
        elif data[i] == "C Z":
            soma += int(7)
        else:
            print("Error")
    
    print(f'Meu score: {soma}')