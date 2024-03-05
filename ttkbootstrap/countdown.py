import tkinter as tk
import ttkbootstrap as ttk
import time as tm


def count_down(time_input):
  output_string.set(time_input)
  if time_input > 0:
    root.after(1000, count_down, time_input - 1)


#window 
root = ttk.Window(themename='darkly',)
root.title('Count Down')
root.geometry('350x200')
root.option_add('*font', 'miracode')

#title
title = tk.Label(
  master=root,
  font='-size 24',
  text='Count Down')

title.pack()

#input field
input_frame = ttk.Frame(master=root)
entry_int = tk.IntVar()

entry = ttk.Entry(
  master=input_frame,
  textvariable=entry_int)

button = ttk.Button(
  master=input_frame,
  text='Count Down',
  command=lambda: count_down(entry_int.get()))

entry.pack(side='left',
           padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

#output
output_string = tk.StringVar()
output_label = tk.Label(
  master=root,
  font='-size 24',
  text='output',
  textvariable=output_string
)
output_label.pack(pady=5)


#run
root.mainloop()