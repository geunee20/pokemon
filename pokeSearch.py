import tkinter as tk
from tkinter import ttk
import sys
import os
import csv

types = ["", "노말", "불꽃", "물", "풀", "전기", "얼음", "격투", "독", "땅", "비행", "에스퍼", "벌레", "바위", "고스트", "드래곤", "악", "강철", "페어리"]

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Create a function to search for Pokemon based on their type
def search_pokemon(pokemon_type_1, pokemon_type_2):
    # Create a list of Pokemon and their types
    pokemons = []
    if pokemon_type_1 == "": pokemon_type_1 = pokemon_type_2
    if pokemon_type_2 == "": pokemon_type_2 = pokemon_type_1
    
    with open(resource_path("./list.csv"), 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if pokemon_type_1 in row and pokemon_type_2 in row:
                pokemons.append(row)

    for item in table.get_children():
        table.delete(item)

    for r in pokemons:
        table.insert('', tk.END, values=r)

# Create the main window
window = tk.Tk()
window.title("Pokemon Search")

# Set the window size to 500 pixels in width and 300 pixels in height
window.geometry("400x290")

# Create a label to prompt the user to select Pokemon types
label = tk.Label(text="Types", font=("Arial", 18))
label.place(x = 20, y = 20, anchor = "w")

# Create the first dropdown menu for selecting a Pokemon type
type_1 = tk.StringVar()
type_1_dropdown = tk.OptionMenu(window, type_1, *types)
type_1_dropdown.place(x = 0, y = 60, anchor = "w")
type_1_dropdown.config(width = 10, height=1)
type_1_dropdown['menu'].configure(font=('Futura',13))

# Create the second dropdown menu for selecting a Pokemon type
type_2 = tk.StringVar()
type_2_dropdown = tk.OptionMenu(window, type_2, *types)
type_2_dropdown.place(x = 0, y = 90, anchor = "w")
type_2_dropdown.config(width = 10, height=1)
type_2_dropdown['menu'].configure(font=('Futura',13))

# Create a button to initiate the search
button = tk.Button(text="Search", command=lambda: search_pokemon(type_1.get(), type_2.get()))
button.place(x = 35, y = 120, anchor = "w")

# Create a canvas widget to hold the search results
table = ttk.Treeview(window, columns=4, show='headings')
table['columns'] = ("No", "이름", "타입1", "타입2")
table.heading('No', text="No.")
table.heading('이름', text="이름")
table.heading('타입1', text="타입")
table.heading('타입2', text="타입")
table.column('No', width=15, anchor=tk.CENTER)
table.column('이름', width=45, anchor=tk.CENTER)
table.column('타입1', width=25, anchor=tk.CENTER)
table.column('타입2', width=25, anchor=tk.CENTER)
table.place(x = 120, y = 20, width = 250, height=250)

# Create a scrollbar for the canvas widget
scrollbar = tk.Scrollbar(window, orient="vertical", command=table.yview)
scrollbar.place(x = 370, y = 20, width = 20, height=250)
table.configure(yscrollcommand=scrollbar.set)

# Set the canvas widget's scrollregion to the desired size
table.configure(yscroll=scrollbar.set)

# Run the main loop
window.mainloop()