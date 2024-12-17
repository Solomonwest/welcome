import tkinter as tk

screen = tk.Tk()
screen.geometry("500x500")
screen.title("YORUBA DICTION")

entry_text = tk.Entry(screen)
entry_text.pack()

outcome = tk.StringVar()
outcome_label = tk.Label(screen,textvariable=outcome)
outcome_label.pack()


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

def check(word):
    if word in yoruba_dictionary:
        outcome.set(yoruba_dictionary[word])
        print(yoruba_dictionary[word])
    
    else:
        outcome.set("Not found")
        print("Not found")
    
search_btn = tk.Button(screen, text="Yoruba", command = lambda: check(entry_text.get()))
search_btn.pack()

hausa_btn = tk.Button(screen, text="Hausa", command = lambda: check(entry_text.get()))
hausa_btn.pack()

spanish_btn = tk.Button(screen, text="Spanish", command = lambda: check(entry_text.get()))
spanish_btn.pack()


screen.mainloop()