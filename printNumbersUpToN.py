def printNumbersUpToN(n):
    number = 1
    while number <= n:
        print(number)
        number += 1

numberInput = int(input("Въведете число N\n"))
print("Числата от 1 до", numberInput, "са:")
printNumbersUpToN(numberInput)