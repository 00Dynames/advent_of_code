import sys

# Process input
# i.e. get input and store in some data structure
catalogue = list()

item = 0
# assume first line in input is not empty
for line in sys.stdin:
    line = line.strip()
    if line == '':
        # add sum to catalogue
        catalogue.append(item)
        item = 0
    else:
        item += int(line)

# add last item
catalogue.append(int(item))

# part1 function
def maxCalories(calories):
    return max(calories)

def topThreeTotal(calories):
    return sum(sorted(calories, reverse=True)[0:3])

# call part 1 function
print(maxCalories(catalogue))

# part 2 function
print (topThreeTotal(catalogue))
