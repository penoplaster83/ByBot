import tkinter as tk

root = tk.Tk()
root.geometry("800x600")

# Создаем главный фрейм, занимающий половину ширины окна
main_frame = tk.Frame(root, borderwidth=2, relief="groove")
main_frame.pack(side="left", fill="both", expand=True)

# Создаем вложенный фрейм в главном фрейме, занимающий половину ширины родительского фрейма
nested_frame = tk.Frame(main_frame, borderwidth=2, relief="groove")
nested_frame.pack(side="left", fill="both", expand=True)
# Создаем вложенный фрейм в главном фрейме, занимающий половину ширины родительского фрейма
nested_frame2 = tk.Frame(main_frame, borderwidth=2, relief="groove")
nested_frame2.pack(side="left", fill="both", expand=True)

# Добавим видимые элементы во вложенный фрейм для наглядности
label = tk.Label(nested_frame, text="Это вложенный фрейм")
label.pack()
label = tk.Label(nested_frame2, text="Это вложенный фрейм")
label.pack()

root.mainloop()