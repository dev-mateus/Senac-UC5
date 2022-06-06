from tkinter import *

root = Tk()

root.geometry('400x200')

fr0 = Frame(root)
fr1 = Frame(root, bg='black')
fr2 = Frame(root, bg='red')

lb1_fr1 = Label(fr1, text='Texto no frame 1', font='Arial 32')
bt1_fr1 = Button(fr1, text='Voltar', font='Arial 32', command=lambda: [fr0.pack(), fr1.pack_forget()])

lb1_fr2 = Label(fr2, text='Texto no frame 2', font='Arial 32')
bt1_fr2 = Button(fr2, text='Voltar', font='Arial 32', command=lambda: [fr0.pack(), fr2.pack_forget()])

bt1 = Button(fr0, text='Abrir Frame 1', font='Arial 32', command=lambda: [fr1.pack(), fr0.pack_forget()])
bt2 = Button(fr0, text='Abrir Frame 2', font='Arial 32', command=lambda: [fr2.pack(), fr0.pack_forget()])

# janela principal
fr0.pack()
bt1.pack()
bt2.pack()

# frame 1
lb1_fr1.pack()
bt1_fr1.pack()

# frame 2
lb1_fr2.pack()
bt1_fr2.pack()

root.mainloop()
