import tkinter as tk

def second():
    screen = tk.Tk()
    screen.geometry('200x200')
    screen.title('second screen')
    screen.mainloop()


window = tk.Tk()
window.geometry("400x400")
window.title('First window')

change = tk.Button(window, text="click")
change.config(command=second,
              background="#44ff29",
              font=('monospace',30))
change.pack()
window.mainloop()