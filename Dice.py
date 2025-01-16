from random import randint
import tkinter as tk

def roll():
	num['text'] = randint(1,6)

window = tk.Tk()

window.rowconfigure([0,1], minsize=70, weight=1)
window.columnconfigure(0, minsize=50, weight=1)


btn = tk.Button(text='Roll', master=window, command=roll)
btn.grid(row=0, column=0, sticky='nsew')

num = tk.Label(text='Roll the dice', master=window)
num.grid(row=1, column=0, sticky='nsew')

window.mainloop()