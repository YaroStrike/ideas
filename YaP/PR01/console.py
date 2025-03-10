try:
    x = float(input("Вещественное число -> "))
except ValueError:
    print("число надо было")

f_part = x - int(x)

print("Дробная часть: ",f_part)