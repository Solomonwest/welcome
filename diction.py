import tkinter as tk

window = tk.Tk()
window.geometry("600x400")
window.title("YORUBA DICTIONARY")

entry_text = tk.Entry(window)
entry_text.pack()

result = tk.StringVar()
result_label = tk.Label(window,textvariable=result)
result_label.pack()


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
    "woman":'Obirin',
    "Come":'Wa',
    "Child":'Omo',
    "Man":'Okurin',
    "Cap":'Fila',
    "House":'Ile',
    "Beans":'Ewa',
    "Friend":'Ore',
    "Festival":'Odun',
    "Crown":'Ade',
    "Clock":'Ago',
}

def check(word):
    if word in yoruba_dictionary:
        result.set(yoruba_dictionary[word])
        print(yoruba_dictionary[word])
    
    else:
        result.set("Not found")
        print("Not found")
    
search_btn = tk.Button(window, text="Yoruba", command = lambda: check(entry_text.get()))
search_btn.pack()

hausa_btn = tk.Button(window, text="Hausa", command = lambda: check(entry_text.get()))
hausa_btn.pack()

spanish_btn = tk.Button(window, text="Spanish", command = lambda: check(entry_text.get()))
spanish_btn.pack()


window.mainloop()