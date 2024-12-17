import tkinter as tk

screen = tk.Tk()
screen.geometry("500x500")
screen.title("let's start")

entry_text = tk.Entry(screen)
entry_text.pack()

outcome = tk.StringVar()
outcome_label = tk.Label(screen,textvariable=outcome)
outcome_label.pack()

screen.mainloop()

yoruba_dictionary = {
    "Stand":'Duro',
    "Joy":'Ayo',
    "Healthy":'Alafia',
    "Light":'Imole',
    "Sit":'Jokoo',
    "Black":'Dudu',
    "Lies":'Iro',
    "Sickness":'Aisan',
    "Fire":'Ina',
    "world":'Aye',
    "Earth":'Ile',
    "Air":'Afefe',
    "Water":'Omi',
    "Good morning":'Ekaro',
    "Love":'Ife',
    "Wealth":'Ola',
    "God":'Oluwa',
    "Rest":'Simi',
    "Enjoyment":'igbadun',
    "Obirin":'woman',
}
