import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("My First Calculator!")

label =tk.Label(root, text="Hello World!", font=("helvetica", 18))
label.pack()

textbox = tk.Text(root, height=3, font=("helvetica", 18))
textbox.pack()

frame = tk.Frame(root)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

btn1 = tk.Button(frame, text="1", font=("helvetica", 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(frame, text="2", font=("helvetica", 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(frame, text="3", font=("helvetica", 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(frame, text="4", font=("helvetica", 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(frame, text="5", font=("helvetica", 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(frame, text="6", font=("helvetica", 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn7 = tk.Button(frame, text="7", font=("helvetica", 18))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(frame, text="8", font=("helvetica", 18))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(frame, text="9", font=("helvetica", 18))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

btn0 = tk.Button(frame, text="0", font=("helvetica", 18))
btn0.grid(row=0, column=0, sticky=tk.W+tk.E)

frame.pack(fill='both')

anotherButton = tk.Button(root, text="Test")

root.mainloop()
