def getDayOfWeek(dayNumberInput):
    if dayNumberInput == 1:
      return "Понеделник"
    elif dayNumberInput == 2:
      return "Вторник"
    elif dayNumberInput == 3:
      return "Сряда"
    elif dayNumberInput == 4:
      return "Четвъртък"
    elif dayNumberInput == 5:
      return "Петък"
    elif dayNumberInput == 6:
      return "Събота"
    elif dayNumberInput == 7:
      return "Неделя"
    else:
      return "Това не е номер на ден от седмицата!"
dayNumberInput = int(input("Въведете номер на ден от седмицата между 1 и 7.\nВходни данни "))
print(getDayOfWeek(dayNumberInput))