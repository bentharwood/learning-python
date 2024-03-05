from tkinter import *
import ttkbootstrap as ttk

#create a window
root = ttk.Window(themename = 'darkly')
root.geometry('800x700')

#create widgets
text_field = Text(root, font = 'miracode 16')
text_field.pack()
#run
root.mainloop()