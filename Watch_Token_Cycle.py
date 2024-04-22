import tkinter as tk
from tkinter import ttk

class TokenTradingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Трейдинг токенами")
        self.root.geometry("800x600")

        self.token_name = "ETH"
        self.token_price = 2000
        self.chosen_operation_type = tk.StringVar()

        self.label_name = tk.Label(self.root, text=f"Токен: {self.token_name}")
        self.label_name.pack()

        self.label_price = tk.Label(self.root, text=f"Цена токена: {self.token_price}")
        self.label_price.pack()

        self.operation_type_combo = ttk.Combobox(self.root, textvariable=self.chosen_operation_type, values=["Buy", "Sell"])
        self.operation_type_combo.pack()

        self.button_execute = tk.Button(self.root, text="Выполнить операцию", command=self.execute_operation)
        self.button_execute.pack()

    def execute_operation(self):
        operation_name = "Покупка" if self.chosen_operation_type.get() == "Buy" else "Продажа"
        print(f"Операция {operation_name} токенов {self.token_name} выполнена")
        self.root.after(5000, self.reset_label)

    def reset_label(self):
        self.label_name.config(text=f"Токен: {self.token_name}")
        self.label_price.config(text=f"Цена токена: {self.token_price}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TokenTradingApp(root)
    root.mainloop()