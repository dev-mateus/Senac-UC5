# editor de texto simples
from tkinter import *
from tkinter.filedialog import *


# back-end
def salvar():
    arquivo = asksaveasfilename(
        defaultextension='.txt',
        filetypes=[('Arquivos de texto', '*.txt'), ('Todos Arquivos', '*.*')]
    )
    with open(arquivo, "w") as output_file:
        text = txt.get(1.0, END)
        output_file.write(text)


def abrir():
    arquivo = askopenfilename(
        filetypes=[('Arquivos de texto', '*.txt'), ('Todos Arquivos', '*.*')]
    )
    with open(arquivo, 'r') as input_file:
        text = input_file.read()
        txt.insert(END, text)


# front-end
root = Tk()
root.geometry('600x600')
root.minsize(width=300, height=300)
root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)


fr1 = Frame(root)
bt1 = Button(fr1, text='Salvar', command=salvar)
bt2 = Button(fr1, text='Abrir', command=abrir)
bt3 = Button(fr1, text='Sair', command=quit)
txt = Text(root)

bt1.grid(row=0, column=0, sticky=EW)
bt2.grid(row=1, column=0, sticky=EW)
bt3.grid(row=2, column=0, sticky=EW)
fr1.grid(row=0, column=0, sticky=NS)
txt.grid(row=0, column=1, sticky=NSEW)


root.mainloop()
