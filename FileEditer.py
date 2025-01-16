import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():

    """Open a file for editing."""

    filepath = askopenfilename(

        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]

    )

    if not filepath:

        return

    txt_edit.delete("1.0", tk.END)

    with open(filepath, "r") as input_file:

        text = input_file.read()

        txt_edit.insert(tk.END, text)

    window.title(f"Text Editor - {filepath}")


def save_file():

	filepath = asksaveasfilename(filetypes=[("Text Files", ".txt"), ("All Files", "*.*")])

	if not filepath:
		return

	with open(filepath, "w") as output_file:
		text = txt_edit.get("1.0", tk.END)
		output_file.write(text)
	window.title(f'Text Editor - {filepath}')


window = tk.Tk()
window.title('Text Editor')

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

frm_btns = tk.Frame(master=window)
btn_edit = tk.Button(master=frm_btns, text='Open file', command=open_file)
btn_save = tk.Button(master=frm_btns, text='Save as...', command=save_file)
txt_edit = tk.Text(master=window)

btn_edit.grid(row=0, column=0, sticky='ew')
btn_save.grid(row=1, column=0, sticky='ew')

frm_btns.grid(row=0,column=0, sticky='ns')
txt_edit.grid(row=0,column=1, sticky='nsew')


window.mainloop()
