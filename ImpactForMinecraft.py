import tkinter as tk
import random

# Создание главного окна
root = tk.Tk()
root.geometry("400x400")  # Установите размер окна
root.attributes("-fullscreen", True)  # Разворачиваем окно на весь экран

# Список цветов, между которыми будет происходить мигание
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'cyan']

# Функция для мигания экрана
def blink():
    color = random.choice(colors)  # Выбираем случайный цвет
    root.configure(bg=color)  # Изменяем фон окна на выбранный цвет
    root.after(25, blink)  # Вызываем функцию снова через 500 миллисекунд

# Начать мигание
blink()

# Запуск основного цикла приложения
root.mainloop()
