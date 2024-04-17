def printSetsUnion(firstSet, secondSet):
    union_set = firstSet.union(secondSet)
    print("Обединението на множествата е:", union_set)

firstSet = {1, 2, 3, 4}
secondSet = {3, 4, 5, 6}

printSetsUnion(firstSet, secondSet)