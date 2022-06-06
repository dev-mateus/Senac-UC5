from tkinter import *

root = Tk()

root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=2)

fr1 = Frame(root, background='red', width=400, height=200)
fr2 = Frame(root, background='black', width=400, height=200)

lb1 = Label(fr1, text='Label 1', bg='yellow')
lb2 = Label(fr2, text='Label 2', bg='blue')

bt1 = Button(fr1, text='Bt 1')
bt2 = Button(fr2, text='Bt 2')

fr1.grid_rowconfigure(0, weight=2)
fr1.grid_rowconfigure(1, weight=2)

fr1.grid(row=0, sticky=NSEW)
fr2.grid(row=1, sticky=NSEW)

lb1.grid(sticky=NSEW)
lb2.grid(sticky=NSEW)

bt1.grid()
bt2.grid(column=1)

root.mainloop()
