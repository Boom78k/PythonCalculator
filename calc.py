from tkinter import * 
import tkinter as tk
root = Tk() 

root.title("Caclculator")
root.geometry(f"300x270+100+100")

def add(num):
	value = calc.get() + str(num)
	calc.delete(0, tk.END)
	calc.insert(0, value)

calc = tk.Entry(root, justify=tk.RIGHT, font=('Arial', 14))
calc.grid(row=0, column=0, columnspan=3, stick='we')	
tk.Button(text='1', bd=3, font=('Arial', 13), command=lambda : add(1)).grid(row=1, column=0, stick='wens', padx='4', pady='4')
tk.Button(text='2', bd=3, font=('Arial', 13), command=lambda : add(2)).grid(row=1, column=1, stick='wens', padx='4', pady='4')
tk.Button(text='3', bd=3, font=('Arial', 13), command=lambda : add(3)).grid(row=1, column=2, stick='wens', padx='4', pady='4')
tk.Button(text='4', bd=3, font=('Arial', 13), command=lambda : add(4)).grid(row=2, column=0, stick='wens', padx='4', pady='4')
tk.Button(text='5', bd=3, font=('Arial', 13), command=lambda : add(5)).grid(row=2, column=1, stick='wens', padx='4', pady='4')
tk.Button(text='6', bd=3, font=('Arial', 13), command=lambda : add(6)).grid(row=2, column=2, stick='wens', padx='4', pady='4')
tk.Button(text='7', bd=3, font=('Arial', 13), command=lambda : add(7)).grid(row=3, column=0, stick='wens', padx='4', pady='4')
tk.Button(text='8', bd=3, font=('Arial', 13), command=lambda : add(8)).grid(row=3, column=1, stick='wens', padx='4', pady='4')
tk.Button(text='9', bd=3, font=('Arial', 13), command=lambda : add(9)).grid(row=3, column=2, stick='wens', padx='4', pady='4')
tk.Button(text='0', bd=3, font=('Arial', 13), command=lambda : add(0)).grid(row=4, column=0, stick='wens', padx='4', pady='4')
root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)

root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)

root.mainloop() 
