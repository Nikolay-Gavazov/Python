def sumТupleNumbers(t):
    sum = 0
    for num in t:
        sum += num
    return sum

myTuple = (6, 3, 1, 12, 100)

result = sumТupleNumbers(myTuple)

print(f"Сумата на eлементите на кортежа е: {result}")