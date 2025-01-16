import tkinter as tk

cel_to_farh_var = True

def convert():
	try:
		if cel_to_farh_var:
			lbl_result['text'] = float(ent_temp.get()) * 1.8 + 32
		else:
			lbl_result['text'] = (float(ent_temp.get())-32) * 5/9
	except ValueError:
		pass

def cel_to_farh():
	global cel_to_farh_var
	if cel_to_farh_var:
		lbl_unit['text'] = '\N{DEGREE FAHRENHEIT}'
		lbl_unit2['text'] = '\N{DEGREE CELSIUS}'
	else:
		lbl_unit['text'] = '\N{DEGREE CELSIUS}'
		lbl_unit2['text'] = '\N{DEGREE FAHRENHEIT}'	
	cel_to_farh_var = not cel_to_farh_var

window = tk.Tk()
window.title('Converter')

window.rowconfigure([0,1], minsize=10, weight=1)
window.columnconfigure([0,1,2,3,4], minsize=50, weight=1)


frm_entry = tk.Frame(master=window)
frm_unit = tk.Frame(master=window)
frm_btn = tk.Frame(master=window)
frm_result = tk.Frame(master=window)
frm_unit2 = tk.Frame(master=window)
frm_change = tk.Frame(master=window)

ent_temp = tk.Entry(master=frm_entry, text='Enter a number')
lbl_unit = tk.Label(master=frm_unit, text='\N{DEGREE CELSIUS}')
btn_convert = tk.Button(master=frm_btn, text='\N{RIGHTWARDS BLACK ARROW}', command=convert)
lbl_result = tk.Label(master=frm_result)
lbl_unit2 = tk.Label(master=frm_unit2, text='\N{DEGREE FAHRENHEIT}')
btn_change = tk.Button(master=frm_change, text='Switch', command=cel_to_farh)

ent_temp.pack()
lbl_unit.pack()
btn_convert.pack()
lbl_result.pack()
lbl_unit2.pack()
btn_change.pack()

frm_entry.grid(row=0, column=0, sticky='nsew')
frm_unit.grid(row=0, column=1, sticky='nsew')
frm_btn.grid(row=0, column=2, sticky='nsew')
frm_result.grid(row=0, column=3, sticky='nsew')
frm_unit2.grid(row=0, column=4, sticky='nsew')
frm_change.grid(row=1, column=2, sticky='ew')


window.mainloop()

