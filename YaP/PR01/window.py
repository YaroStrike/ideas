import tkinter as tk
from tkinter import messagebox

# Функция для вычисления дробной части
def calculate_fractional_part():
    try:
        # Получаем введённое значение из поля ввода
        x = float(entry.get())

        # Вычисляем дробную часть
        f_part = x - int(x)

        # Выводим результат в метку
        result_label.config(text=f"Дробная часть: {f_part}")
    except ValueError:
        # Если введено не число, показываем сообщение об ошибке
        messagebox.showerror("Ошибка", "Введите корректное вещественное число!")

# Создаём главное окно
root = tk.Tk()
root.title("Дробная часть числа")
root.geometry("300x150")  # Размер окна

# Поле ввода
entry_label = tk.Label(root, text="Введите вещественное число:")
entry_label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

# Кнопка для вычисления
calculate_button = tk.Button(root, text="Вычислить дробную часть", command=calculate_fractional_part)
calculate_button.pack(pady=10)

# Метка для вывода результата
result_label = tk.Label(root, text="Дробная часть: ")
result_label.pack(pady=5)

# Запуск основного цикла обработки событий
root.mainloop()