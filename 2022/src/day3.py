import sys

# read input and partition into 2 sacks part 1
# sacks = list()
# for line in sys.stdin:
#     line = line.strip()
#     midIndex = int(line.__len__()/2)
#     sacks.append((line[0:midIndex], line[midIndex:]))
    # print((line[0:midIndex], line[midIndex:]))
    
# read input and partition into groups pf 3 lines part 2
groups = list(map(lambda x: x.strip(), sys.stdin.readlines()))
# groups = 
print(groups)


# print(sacks)

# find common item in two sacks (assuming there's only one common item)
def findCommonItem(sackA, sackB):
    for item in sackA:
        if item in sackB:
            return item

    return None

# find common item in three sacks (assuming there's exactly one common item)
def findCommonItemInThreeSacks(sackA, sackB, sackC):
    for item in sackA:
        if item in sackB and item in sackC:
            return item
    
    return None

# get priority of item
def getPriority(item):
    itemOrd = ord(item)
    if itemOrd >= ord('a') and itemOrd <= ord('z'):
        return itemOrd - ord('a') + 1
    # elif itemOrd >= ord('A') and itemOrd <= ord('Z'):
    # assuming only valid characters are given
    else:
        return itemOrd - ord('A') + 27

# find common items in a list of sacks and sum their priorities
def sumPrioritiesOfDuplicates(sacks):
    result = 0

    for sackA, sackB in sacks:
        commonItem = findCommonItem(sackA, sackB)
        # print(commonItem, getPriority(commonItem))
        result += getPriority(commonItem)

    return result

# print(sumPrioritiesOfDuplicates(sacks))