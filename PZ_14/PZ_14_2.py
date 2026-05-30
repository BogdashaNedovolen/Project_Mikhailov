# 4 работа

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Форма регистрации пользователя")
root.geometry("400x550")


main_frame = tk.Frame(root, borderwidth=2, relief="solid", padx=15, pady=15)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)

tk.Label(main_frame, text="Форма регистрации пользователя", font=("Arial", 12, "bold")).grid(
    row=0, column=0, columnspan=3, pady=(0, 15)
)



tk.Label(main_frame, text="Ваше имя:").grid(row=1, column=0, sticky="e", pady=5)
name_entry = tk.Entry(main_frame, bg="#E0E0E0", width=25)
name_entry.grid(row=1, column=1, columnspan=2, sticky="w", pady=5)



tk.Label(main_frame, text="Пароль:").grid(row=2, column=0, sticky="e", pady=5)
password_entry = tk.Entry(main_frame, bg="#E0E0E0", width=25, show="*")
password_entry.grid(row=2, column=1, columnspan=2, sticky="w", pady=5)



tk.Label(main_frame, text="Возраст:").grid(row=3, column=0, sticky="e", pady=5)
age_entry = tk.Entry(main_frame, bg="#E0E0E0", width=25)
age_entry.grid(row=3, column=1, columnspan=2, sticky="w", pady=5)



tk.Label(main_frame, text="Пол:").grid(row=4, column=0, sticky="e", pady=5)
gender_var = tk.StringVar()
tk.Radiobutton(main_frame, text="Мужской", variable=gender_var, value="male").grid(
    row=4, column=1, sticky="w", padx=5
)
tk.Radiobutton(main_frame, text="Женский", variable=gender_var, value="female").grid(
    row=4, column=2, sticky="w", padx=5
)



tk.Label(main_frame, text="Ваши увлечения:").grid(row=5, column=0, sticky="ne", pady=5)
hobbies_frame = tk.Frame(main_frame)
hobbies_frame.grid(row=5, column=1, columnspan=2, sticky="w")
music_var = tk.IntVar()
video_var = tk.IntVar()
drawing_var = tk.IntVar()
tk.Checkbutton(hobbies_frame, text="Музыка", variable=music_var).pack(side="left", padx=2)
tk.Checkbutton(hobbies_frame, text="Видео", variable=video_var).pack(side="left", padx=2)
tk.Checkbutton(hobbies_frame, text="Рисование", variable=drawing_var).pack(side="left", padx=2)



tk.Label(main_frame, text="Ваша страна:").grid(row=6, column=0, sticky="e", pady=5)
country_combobox = ttk.Combobox(main_frame, width=22)
country_combobox.grid(row=6, column=1, columnspan=2, sticky="w", pady=5)



tk.Label(main_frame, text="Ваш город:").grid(row=7, column=0, sticky="e", pady=5)
city_combobox = ttk.Combobox(main_frame, width=22)
city_combobox.grid(row=7, column=1, columnspan=2, sticky="w", pady=5)



tk.Label(main_frame, text="Кратко о себе:").grid(row=8, column=0, sticky="ne", pady=5)
about_text = tk.Text(main_frame, bg="#E0E0E0", height=3, width=25)
about_text.grid(row=8, column=1, columnspan=2, sticky="w", pady=5)



tk.Label(main_frame, text="Решите пример, запишите результат в поле ниже:").grid(
    row=9, column=0, columnspan=3, sticky="w", pady=(15, 5)
)
math_entry = tk.Entry(main_frame, bg="#E0E0E0", width=25)
math_entry.grid(row=10, column=1, columnspan=2, sticky="w", pady=5)


button_frame = tk.Frame(main_frame)
button_frame.grid(row=11, column=1, columnspan=2, pady=15, sticky="w")
tk.Button(button_frame, text="Отменить ввод", width=18).pack(side="left", padx=5)
tk.Button(button_frame, text="Данные подтверждаю", width=18).pack(side="left", padx=5)

root.mainloop()
