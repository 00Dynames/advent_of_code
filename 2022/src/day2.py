import sys

strategy_guide = list()

for line in sys.stdin:
    line = line.strip().split(' ')
    strategy_guide.append((line[0], line[1]))

#print(strategy_guide)

def countPoints(strategy_guide):
    points = 0

    for round in strategy_guide:

        shape = 1 if round[1] == 'X' else (2 if round[1] == 'Y' else 3)

        # wins
        if (round[0] == 'A' and round[1] == 'Y')\
            or (round[0] == 'B' and round[1] == 'Z')\
            or (round[0] == 'C' and round[1] == 'X'):
            points += (6 + shape)
        # draws
        elif (round[0] == 'A' and round[1] == 'X')\
            or (round[0] == 'B' and round[1] == 'Y')\
            or (round[0] == 'C' and round[1] == 'Z'):
            points += (3 + shape)
        # losses
        else:
            points += shape

    return points

def countPoints2(strategy_guide):
    points = 0

    for opponent, result in strategy_guide:
        # wins
        if (result == 'Z'):
            shape = 1 if opponent == 'C' else (2 if opponent == 'A' else 3)
            points += (6 + shape)
        # draws
        elif (result == 'Y'):
            shape = 1 if opponent == 'A' else (2 if opponent == 'B' else 3)
            points += (3 + shape)
        # losses
        else:
            shape = 1 if opponent == 'B' else (2 if opponent == 'C' else 3)
            points += shape

    return points

# print(countPoints(strategy_guide))
print(countPoints2(strategy_guide))