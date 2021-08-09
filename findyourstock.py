import requests
from tkinter import *


def getStock(gui):
    stock_name = textfield_name.get()
    stock_date = textfield_date.get()

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + stock_name + '&apikey=YBD78NB4MGIKAAIE'
    r = requests.get(url)
    json_data = r.json()

    open_price = float(json_data['Time Series (Daily)'][stock_date]['1. open'])
    closing_price = float(json_data['Time Series (Daily)'][stock_date]['4. close'])
    gain_in_price = closing_price - open_price
    high_price = float(json_data['Time Series (Daily)'][stock_date]['2. high'])
    low_price = float(json_data['Time Series (Daily)'][stock_date]['3. low'])


    data_label_text = '\nOpening Price : $' + str(open_price) + '\n' + '\n' + 'Closing Price : $' + str(closing_price) + '\n' + '\n' + 'Gain in Price : $' + str(gain_in_price) + '\n' + '\n' + 'High Price : $' + str(high_price) + '\n' + '\n' + 'Low Price : $' + str(low_price) + '\n'
    data_label.config(text = data_label_text, bg = 'black', fg = 'white')

title_font = ("candara", 50, "bold")
text_font = ("candara", 35, "bold")
gui = Tk()
gui.configure(background="black")
gui.title("Calculator8")
gui.geometry("800x1000")

textfield_name = Entry(gui, font = title_font)
textfield_name.pack(pady = 20)
textfield_name.focus()
textfield_name.bind('<Return>', getStock)

textfield_date = Entry(gui, font = title_font)
textfield_date.pack(pady = 20)
textfield_date.focus()
textfield_date.bind('<Return>', getStock)

data_label = Label(gui, font = text_font, bg = 'black')
data_label.pack()

gui.mainloop()

