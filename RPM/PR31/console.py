try:
    x = float(input("Вещественное число -> "))
except ValueError:
    print("число надо было")

f_part = x - int(x)
rounded = round(f_part, 15)

print("Дробная часть: ",rounded)