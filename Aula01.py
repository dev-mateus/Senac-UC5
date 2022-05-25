# Aula 01 será apresentado os elementos básicos de uma GUI
from tkinter import *

# ELEMENTOS:
# 1) WINDOW
root = Tk()
root.title('App GUI')
#root.geometry('300x300')

# 2) FRAME
frm1 = Frame(root)

# 3) WIDGET
lb1 = Label(frm1, text='Digite aqui:')
lb2 = Label(frm1)
ent1 = Entry(frm1)
btn1 = Button(frm1, text='Click aqui!')
btn2 = Button(frm1, text='Sair', command=quit)

# 4) LAYOUT
# 4.1) PACK
frm1.pack()

# 4.2) PLACE
lb1.place(x=10, y=10)

# 4.3) GRID

# EXECUTA O WINDOW
root.mainloop()
