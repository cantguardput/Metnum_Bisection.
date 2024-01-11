import tkinter as tk
import math

class MetodeBagiDuaApp:
    def __init__(self, root):
        self.root = root
        root.title("Metode Bagi 2")

        self.initial_balance_label = tk.Label(root, text="Saldo Awal:")
        self.initial_balance_label.grid(row=0, column=0)

        self.initial_balance_input = tk.Entry(root, width=20)
        self.initial_balance_input.grid(row=0, column=1)

        self.target_balance_label = tk.Label(root, text="Perkiraan Saldo:")
        self.target_balance_label.grid(row=1, column=0)

        self.target_balance_input = tk.Entry(root, width=20)
        self.target_balance_input.grid(row=1, column=1)

        self.investment_percentage_label = tk.Label(root, text="Persentase Investasi per Tahun:")
        self.investment_percentage_label.grid(row=2, column=0)

        self.investment_percentage_input = tk.Entry(root, width=20)
        self.investment_percentage_input.grid(row=2, column=1)

        self.calculate_button = tk.Button(root, text="Hitung Tahun untuk Perkiraan Saldo", command=self.calculate_years)
        self.calculate_button.grid(row=3, column=1)

        self.result_area = tk.Text(root, height=10, width=30, wrap=tk.WORD)
        self.result_area.grid(row=4, column=0, columnspan=2)

    def calculate_years(self):
        try:
            initial_balance = float(self.initial_balance_input.get())
            target_balance = float(self.target_balance_input.get())
            investment_percentage = float(self.investment_percentage_input.get())

            years = 0
            current_balance = initial_balance

            result_text = "Pertumbuhan saldo investasi setiap tahun:\n"
            while current_balance < target_balance:
                current_balance += current_balance * (investment_percentage / 100)
                years += 1
                result_text += f"Tahun {years}: Jumlah investasi = {current_balance:.2f}\n"

            result_text += f"\nSaldo investasi mencapai atau melebihi perkiraan saldo pada Tahun {years}.\n"
            result_text += f"Jumlah investasi pada Tahun {years}: {current_balance:.2f}"

            self.result_area.delete(1.0, tk.END)
            self.result_area.insert(tk.END, result_text)
        except ValueError:
            self.result_area.delete(1.0, tk.END)
            self.result_area.insert(tk.END, "Masukkan yang tidak valid. Harap masukkan angka untuk semua input.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MetodeBagiDuaApp(root)
    root.mainloop()
