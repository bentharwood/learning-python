import ttkbootstrap as ttk

#make the window
root = ttk.Window(themename='cosmo')

#title
title = ttk.Label(root, text="Theme Switcher", font = 'miracode 24').pack(padx = 10,  pady = 10)


#buttons
buttons_frame = ttk.Frame(root).pack()
# ttk.Button(buttons_frame, text='a', command=lambda: None).grid(column=0, row=0)
# ttk.Button(buttons_frame, text='b', command=lambda: None).grid(column=1, row=0)
# ttk.Button(buttons_frame, text='c', command=lambda: None).grid(column=2, row=0)
# ttk.Button(buttons_frame, text='d', command=lambda: None).grid(column=3, row=0)
# ttk.Button(buttons_frame, text='e', command=lambda: None).grid(column=4, row=0)
# ttk.Button(buttons_frame, text='f', command=lambda: None).grid(column=5, row=0)
# ttk.Button(buttons_frame, text='g', command=lambda: None).grid(column=6, row=0)
# ttk.Button(buttons_frame, text='h', command=lambda: None).grid(column=7, row=0)
# ttk.Button(buttons_frame, text='j', command=lambda: None).grid(column=8, row=0)
# ttk.Button(buttons_frame, text='k', command=lambda: None).grid(column=9, row=0)
# ttk.Button(buttons_frame, text='l', command=lambda: None).grid(column=10, row=0)
# ttk.Button(buttons_frame, text='m', command=lambda: None).grid(column=11, row=0)
# ttk.Button(buttons_frame, text='n', command=lambda: None).grid(column=12, row=0)
root.mainloop()

