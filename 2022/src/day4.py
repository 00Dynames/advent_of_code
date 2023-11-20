import sys

pairs = list(map(lambda x: x.strip().split(","), sys.stdin.readlines()))
pairs = list(map(lambda x: list(map(lambda y: y.split("-"), x)), pairs))

def contains(sectionA, sectionB):

    x, y = sectionA[0], sectionA[1]
    a, b = sectionB[0], sectionB[1]

    print(sectionA, sectionB)

    boolA = bool(int(a) >= int(x) and int(b) <= int(y))
    boolB = bool(int(x) >= int(a) and int(y) <= int(b))

    print(boolA, boolB)

    if boolA or boolB:
        return True

    return False

# print(pairs)

def overlap(sectionA, sectionB):
    
    x, y = sectionA[0], sectionA[1]
    a, b = sectionB[0], sectionB[1]

    print(sectionA, sectionB)

    boolA = bool(int(a) >= int(x) and int(a) <= int(y))
    boolB = bool(int(x) >= int(a) and int(x) <= int(b))

    print(boolA, boolB)
    
    if boolA or boolB:
        return True

    return False

count = 0
for pair in pairs:

    result = overlap(pair[0], pair[1])
    print(result)
    if result:
        count += 1

print(count)