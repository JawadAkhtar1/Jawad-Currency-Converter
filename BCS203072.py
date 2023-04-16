import tkinter as tk
import requests


class CurrencyConverter:
    API_URL = "https://openexchangerates.org/api/latest.json?app_id=7fb636abd88145aba609639e30ca5843"

    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Currency Converter")

        # Define currencies
        self.currencies = self.get_currencies()

        # Define variables
        self.from_currency = tk.StringVar()
        self.to_currency = tk.StringVar()
        self.amount = tk.StringVar()
        self.converted_amount = tk.StringVar()

        # Create widgets
        tk.Label(self.parent, text="From currency").grid(row=0, column=0)
        tk.OptionMenu(self.parent, self.from_currency, *self.currencies).grid(row=0, column=1)
        tk.Label(self.parent, text="To currency").grid(row=1, column=0)
        tk.OptionMenu(self.parent, self.to_currency, *self.currencies).grid(row=1, column=1)
        tk.Label(self.parent, text="Amount").grid(row=2, column=0)
        tk.Entry(self.parent, textvariable=self.amount).grid(row=2, column=1)
        tk.Button(self.parent, text="Convert", command=self.convert).grid(row=3, column=0)
        tk.Label(self.parent, text="Converted amount").grid(row=4, column=0)
        tk.Entry(self.parent, textvariable=self.converted_amount, state="readonly").grid(row=4, column=1)
        tk.Button(self.parent, text="Reset", command=self.reset).grid(row=5, column=0)

    def get_currencies(self):
        return ["USD", "EUR", "GBP", "JPY", "AUD", "CAD"]

    def convert(self):
        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()
        amount = float(self.amount.get())

        response = requests.get(f"{self.API_URL}&symbols={from_currency},{to_currency}")
        rates = response.json()["rates"]
        converted_amount = round(amount * rates[to_currency] / rates[from_currency], 2)

        self.converted_amount.set(converted_amount)

    def reset(self):
        self.from_currency.set("")
        self.to_currency.set("")
        self.amount.set("")
        self.converted_amount.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
