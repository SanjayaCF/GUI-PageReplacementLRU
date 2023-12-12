import customtkinter as ctk
from tkinter import ttk
from script import AlgoritmaLRU

def add_table(_dict):
    style = ttk.Style()
    style.layout('my.Treeview',
                 [('Treeview.field', {'sticky': 'nswe', 'border': '1', 'children': [
                     ('Treeview.padding', {'sticky': 'nswe', 'children': [
                         ('Treeview.treearea', {'sticky': 'nswe'})
                         ]})
                     ]})
                  ])
    style.theme_use('clam')
    style.configure('Treeview',
                    background='#2E2E2E', 
                    foreground='white',   
                    rowheight=25,
                    fieldbackground='#2E2E2E',
                    )
    style.map('Treeview', background=[('selected', '#3E3E3E')])
    style.configure('Treeview.Heading', font=('Times New Roman', 12, 'bold'), foreground='#000000')

    for widget in root.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()

    table = ttk.Treeview(root, columns=('step', 'page', 'state', 'hit/Miss'), show='headings', style='my.Treeview')
    table.heading('step', text='Step', )
    table.heading('page', text='Page')
    table.heading('state', text='LRU Cache State')
    table.heading('hit/Miss', text='Hit/Miss')

    for col in ('step', 'page', 'state', 'hit/Miss'):
        table.tag_configure(f'{col}_center', anchor='center')
        table.column(col, anchor='center')
        table.heading(col, text=col.title(), anchor='center')

    table.pack(fill='both', expand=True)
    for iteration in _dict:
        data = (iteration, _dict[iteration][0], _dict[iteration][1], _dict[iteration][2])
        table.insert(parent='', index=ctk.END, values=data, tag=(_dict[iteration][2] == "✓"))
        table.tag_configure(tagname=True, background="#00ff00")

def add_output():
    output = AlgoritmaLRU().simulasi_LRU(references.get(),frames.get())
    label.configure(text=output[0])
    references.delete(0, ctk.END)
    frames.delete(0, ctk.END)
    add_table(output[1])

# Function to navigate to the LRU simulation page
def navigate_to_simulation():
    notebook.select(1)  # Select the second tab (index starts from 0)
    references.delete(0, ctk.END)
    frames.delete(0, ctk.END)
    add_table(AlgoritmaLRU().simulasi_LRU(references.get(), frames.get())[1])
    references.focus_set()  # Set focus on the references entry
    frames.focus_set()

root = ctk.CTk()
root.geometry("750x450")
root.title("Aplikasi Simulasi Algoritma LRU")

# Create a notebook to hold multiple pages
notebook = ttk.Notebook(root)

# Opening Page
opening_frame = ctk.CTkFrame(notebook)
notebook.add(opening_frame, text="Opening Page")

# Introduction Label and Navigation Button
intro_label = ctk.CTkLabel(opening_frame, text="Welcome to the LRU Simulation App!", font=ctk.CTkFont(size=18))
intro_label.pack(pady=20)

navigate_button = ctk.CTkButton(opening_frame, text="Start Simulation", width=500, command=navigate_to_simulation)
navigate_button.pack(pady=20)

# LRU Simulation Page
simulation_frame = ctk.CTkFrame(notebook)
notebook.add(simulation_frame, text="LRU Simulation")

# Title Label and other UI elements for the LRU simulation page (same as your provided code)
title_label = ctk.CTkLabel(simulation_frame, text="Simulasi Algoritma LRU Page Replacement", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

references = ctk.CTkEntry(simulation_frame, placeholder_text="References")
references.pack(fill="x")

frames = ctk.CTkEntry(simulation_frame, placeholder_text="Frames")
frames.pack(fill="x")

add_button = ctk.CTkButton(simulation_frame, text="Simulasi Jadwal", width=500, command=add_output)
add_button.pack(pady=20)

label = ctk.CTkLabel(simulation_frame, text="")
label.pack()

sizegrip = ttk.Sizegrip(simulation_frame)
sizegrip.pack(side="bottom", anchor="se")

notebook.pack(expand=True, fill="both")

root.mainloop()
