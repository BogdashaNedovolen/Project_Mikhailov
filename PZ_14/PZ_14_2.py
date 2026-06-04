"""
Составить функцию решения задачи. Из заданного числа вычли сумму его цифр. 
Из результата вновь вычли сумму его цифр и т.д. 
Через сколько таких действий получится нуль?
"""

# PZ_5_2

import tkinter as tk
from tkinter import messagebox


def rasschoyt(n):
    if n == 0:
        return 0
    
    count = 0
    current = n

    while current != 0:
        digit_sum = 0
        temp = current

        while temp > 0:
            digit_sum = digit_sum + (temp % 10)
            temp = temp // 10

        current = current - digit_sum
        count = count + 1

        if current < 0:
            current = -current

    return count


root = tk.Tk()
root.title("Практическая")
root.geometry("350x200")

tk.Label(root, text="Введите число:", font=("Arial", 12, 'bold')).pack(pady=15)
entry = tk.Entry(root, font=("Arial", 12), width=15)
entry.pack()

def calculate():
    try:
        n = int(entry.get())
        result_label.config(text=f"Количество действий: {rasschoyt(n)}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число!")

tk.Button(root, text="Рассчитать", command=calculate, font=("Arial", 10, 'bold'), bg="#345469", fg="white", padx=15, pady=5).pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="#2c3e50")
result_label.pack(pady=10)

root.mainloop()
