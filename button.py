# This code is to create a functional button that counts when it's been clicked.
import tkinter as tk

window = tk.Tk()  
window.geometry("600x600")
window.title("button test")

count = 0

def click(): 
    global count
    count += 1
    label.config(text=count)


btn = tk.Button(window,
                text='hello there!',
                bg='blue',
                font=('Arial',50),
                activebackground='cyan',
                state='active')
btn.config(command=click)
label = tk.Label(window, text=count,
                compound='top',
                font=('monospace',50))
label.pack()
btn.pack()



window.mainloop()