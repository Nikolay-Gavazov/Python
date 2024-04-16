def evenOrOdd(numberInput):
  if numberInput == 0:
    return "Числото е 0!"
  elif numberInput % 2 == 0:
    return "Четно число!"
  else:
    return("Нечетно число!")
numberInput = int(input("Въведете число за проверка дали е четно или нечетно!\nВходни данни "))
print(evenOrOdd(numberInput))