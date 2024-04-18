def printUniqueElements(lst):
    uniqueElements = set(lst)
    for element in uniqueElements:
        print(element)

myList = [1, 2, 3, 1, 2, 4, 5, 6, 5]

print("Уникалните елементи на списъка са:")
printUniqueElements(myList)