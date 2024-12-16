number1 = float(input("Введите первое число: "))
number2= float(input("Введите второе число: "))

result = "Числа равны" if number1 == number2
    else (f"Наименьшее число: {number1}" if number1 < number2 else f"Наименьшее число: {number2}")

print(result)
