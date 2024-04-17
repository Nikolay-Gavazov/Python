def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

numberInput = int(input("Въведете число\n"))

if isPrime(numberInput):
    print(f"{numberInput} е просто число")
else:
    print(f"{numberInput} не е просто число")