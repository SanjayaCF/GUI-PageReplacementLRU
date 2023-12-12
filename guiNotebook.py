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
        table.tag_configure(tagname=True, background="#00ff00", foreground='black')

def add_output():
    output = AlgoritmaLRU().simulasi_LRU(references.get(),frames.get())
    label.configure(text=output[0])
    #references.delete(0, ctk.END)
    #references.insert(0, "7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1")
    #frames.delete(0, ctk.END)
    #frames.insert(0, "3")
    add_table(output[1])

def navigate_to_simulation():
    notebook.select(1) 
    references.delete(0, ctk.END)
    references.insert(0, "7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1")
    frames.delete(0, ctk.END)
    frames.insert(0, "3")
    references.focus_set() 
    frames.focus_set()

root = ctk.CTk()
root.geometry("750x450")
root.title("Aplikasi Simulasi Algoritma LRU")

notebook = ttk.Notebook(root)

page_intro = ctk.CTkFrame(notebook)
notebook.add(page_intro, text="Opening Page")

intro_label = ctk.CTkLabel(page_intro, text="Tugas Akhir Mata Kuliah Sistem Operasi", font=ctk.CTkFont(size=30, weight="bold"))
intro_label.pack(pady=20)
kelompok = '''
Rendy Ananta Kristanto - 71220840
Vittorio Emmanuel Harianto - 71220912
Leif Sean Kusumo - 71220915
Sanjaya Cahyadi Fuad - 71220965
'''
perkenalan = ctk.CTkLabel(page_intro, text=kelompok, font=('Arial', 12))
perkenalan.configure(text_color='white', font=('Courier',20), corner_radius = 5)
perkenalan.pack()

navigate_button = ctk.CTkButton(page_intro, text="Start", width=500, command=navigate_to_simulation)
navigate_button.configure(hover_color='#ADD8E6', border_width=2)
navigate_button.pack(pady=20)

simulation_frame = ctk.CTkFrame(notebook)
notebook.add(simulation_frame, text="LRU Simulation")

title_label = ctk.CTkLabel(simulation_frame, text="Simulasi Algoritma LRU Page Replacement", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

references = ctk.CTkEntry(simulation_frame, placeholder_text="References")
references.pack(fill="x")

frames = ctk.CTkEntry(simulation_frame, placeholder_text="Frames")
frames.pack(fill="x")

add_button = ctk.CTkButton(simulation_frame, text="Simulasi Jadwal", width=500, command=add_output)
add_button.configure(hover_color='#ADD8E6', border_width=2)
add_button.pack(pady=20)

label = ctk.CTkLabel(simulation_frame, text="")
label.pack()

sizegrip = ttk.Sizegrip(simulation_frame)
sizegrip.pack(side="bottom", anchor="se")

notebook.pack(expand=True, fill="both")

root.mainloop()
