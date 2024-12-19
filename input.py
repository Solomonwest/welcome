import tkinter as tk

def submit():
    username = input.get()
    print("hey", username)

screen = tk.Tk()
screen.geometry("300x300")
screen.title("entry check")

input = tk.Entry()
input.config(font=('Ink Free',50))
btn = tk.Button(screen, text='click me',
                bg='#23FF43',
                font=('Ink Free',30))
btn.config(command='submit')
btn.pack()
input.pack()
screen.mainloop()