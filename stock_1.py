from yahoo_fin import stock_info
from tkinter import *

def stock_price():
    try:
        price = stock_info.get_live_price(e1.get())
        Current_stock.set(price)
        error_label.config(text="")
    except:
        error_label.config(text="Error: Stock symbol not found.", fg="red")

def clear_text_field():
    e1.delete(0, END)

def show_info():
    global info_visible
    if info_visible:
        info_label.config(text="", fg="blue")
        info_button.config(text="Info")
        info_visible = False
    else:
        info = " This program reports the current price of a desired stock. \n\n Step 1: Enter the company symbol for the stock you want to check, such as AAPL for Apple Inc. \n Step 2: Click 'Show'. \n Step 3: The reported price will be printed. \n Step 4: Click 'Clear' to erase all content within the text field. \n\n Error Handling: If an stock is unable to be found, an error message will be printed. \n\n Note: This program may not be able to get the stock price if the stock is not publicly traded or if the Yahoo Finance API is unavailable."
        info_label.config(text=info, fg="blue", justify=LEFT)
        info_button.config(text="Hide")
        info_visible = True

master = Tk()
master.geometry("800x350")
Current_stock = StringVar()

Label(master, text="Stock Price Reporter", justify=LEFT).grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky=W)
Label(master, text="*Data gathered from Yahoo Finance*", justify=LEFT).grid(row=10, column=0, padx=5, pady=5, sticky=W)
Label(master, text=" Company Symbol:", justify=LEFT).grid(row=1, sticky=W, pady=5)
Label(master, text="Stock Result (USD):", justify=LEFT).grid(row=2, sticky=W, padx=5, pady=5)

result2 = Label(master, text="", textvariable=Current_stock, justify=LEFT, fg="green").grid(row=2, column=1, sticky=W)

e1 = Entry(master)
e1.grid(row=1, column=1, sticky=W)

b = Button(master, text="Show", command=stock_price)
b.grid(row=1, column=2, columnspan=2, sticky=W)

clear_button = Button(master, text="Clear", command=clear_text_field)
clear_button.grid(row=1, column=4, sticky=W, padx=5)

error_label = Label(master, text="", fg="red", justify=LEFT)
error_label.grid(row=3, column=0, columnspan=2, sticky=W)

info_visible = False
info_button = Button(master, text="Info", command=show_info, justify=LEFT)
info_button.grid(row=4, column=0, sticky=W, pady=5, padx=5)

info_label = Label(master, text="", fg="blue", justify=LEFT)
info_label.grid(row=5, column=0, columnspan=2, pady=10, sticky=W)

mainloop()
