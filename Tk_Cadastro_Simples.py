from tkinter import *
from tkinter.ttk import Combobox


# ############################ formata_cpf ############################# #
def formata_cpf(event=None):
    entrada = en2_fr1.get()[:14]
    nova_entrada = ''

    # verifica se a entrada é um 'BackSpace'
    if event.keysym == 'BackSpace':
        return

    for i in range(len(entrada)):
        if not entrada[i] in '0123456789':
            continue

        # 'verifica' e formata a entrada nas posições [2,6,10]
        if i in [2, 6]:
            nova_entrada += entrada[i] + '.'
        elif i == 10:
            nova_entrada += entrada[i] + '-'
        else:
            nova_entrada += entrada[i]

    en2_fr1.delete(0, 'end')
    en2_fr1.insert(0, nova_entrada)


# ############################ formata_data ############################# #
def formata_data(event=None):
    # 06/05/1988
    entrada = en4_fr1.get()[:10]
    nova_entrada = ''

    # verifica se a entrada é um 'BackSpace'
    if event.keysym == 'BackSpace':
        return

    for i in range(len(entrada)):
        if not entrada[i] in '0123456789':
            continue

        # 'verifica' e formata a entrada nas posições [2,6,10]
        if i in [1, 4]:
            nova_entrada += entrada[i] + '/'
        else:
            nova_entrada += entrada[i]

    en4_fr1.delete(0, 'end')
    en4_fr1.insert(0, nova_entrada)


# ############################ formata_tel ############################# #
def formata_tel(event=None):
    # (035)9-9213-3545
    entrada = en3_fr1.get()[:16]
    nova_entrada = '('

    # verifica se a entrada é um 'BackSpace'
    if event.keysym == 'BackSpace':
        return

    for i in range(len(entrada)):
        if not entrada[i] in '0123456789':
            continue
        # 'verifica' e formata a entrada nas posições [0,3,5,10]
        if entrada != '0' and i in [0]:
            nova_entrada += '0' + entrada[i]
        elif entrada == '0' and i in [0]:
            nova_entrada += entrada[i]
        elif i in [3]:
            nova_entrada += entrada[i] + ')'
        elif i in [5, 10]:
            nova_entrada += entrada[i] + '-'
        else:
            nova_entrada += entrada[i]

    en3_fr1.delete(0, 'end')
    en3_fr1.insert(0, nova_entrada)


# ############################ grava_dados ############################# #
lista_entrada = []
lista_entrada_1 = []


def gravar():

    global lista_entrada, lista_entrada_1
    lista_entrada_1 += en1_fr1.get()
    lista_entrada += [en2_fr1.get(), en3_fr1.get(), en4_fr1.get()]
    limpar()
    #print(lista_entrada[0][0, 1, 2, 3])


# ############################ limpa_dados ############################# #
def limpar():
    en1_fr1.delete(0, 'end')
    en2_fr1.delete(0, 'end')
    en3_fr1.delete(0, 'end')
    en4_fr1.delete(0, 'end')


# ############################ logout ############################# #
def logout():
    fr0.pack(anchor=CENTER)
    fr1.pack_forget()
    fr2.pack_forget()
    fr3.pack_forget()
    limpar()


# ############################ login ############################# #
def login():
    fr0.pack_forget()
    en1_fr0.delete(0, 'end')
    en2_fr0.delete(0, 'end')
    fr1.pack(fill=BOTH, anchor=W)
    fr2.pack(fill=BOTH, anchor=W)
    fr3.pack(fill=BOTH, anchor=NE)


# ############################ consultar ############################# #
def consultar():
    fr1.pack_forget()
    fr2.pack_forget()
    fr3.pack_forget()
    limpar()
    fr7.pack(fill=BOTH, anchor=NE)
    fr4.pack(fill=BOTH, anchor=W)
    fr5.pack(fill=BOTH, anchor=W)
    fr6.pack(fill=BOTH, anchor=NE)
    mb1_fr7 = Combobox(fr7, values=lista_entrada_2, font='verdana 11')
    mb1_fr7.grid(row=0, column=0)



# ############################ voltar ############################# #
def voltar():
    fr4.pack_forget()
    fr5.pack_forget()
    fr6.pack_forget()
    fr7.pack_forget()
    fr1.pack(fill=BOTH, anchor=W)
    fr2.pack(fill=BOTH, anchor=W)
    fr3.pack(fill=BOTH, anchor=NE)


# ############################## window ############################### #
root = Tk()
root.title('cadastro')
root.config(bg='#8c8a89')
root.config(pady=10, padx=10)
#root.geometry('730x300')
root.resizable(width=False, height=False)
# ############################ variáveis ############################# #
var_mb1_fr7 = StringVar()
# ############################## frames ############################### #
fr0 = LabelFrame(root, padx=10, pady=10, bg='#8c8a89')
fr1 = LabelFrame(root, padx=10, pady=10, bg='#8c8a89', fg='#660000', text='Dados Pessoais', font='Verdana 14 italic')
fr2 = LabelFrame(root, padx=10, pady=10, bg='#8c8a89', fg='#660000', text='Endereço', font='Verdana 14 italic')
fr3 = Frame(root, padx=10, pady=10, bg='#8c8a89')
fr4 = LabelFrame(root, padx=10, pady=10, bg='#8c8a89', fg='#660000', text='Dados Pessoais', font='Verdana 14 italic')
fr5 = LabelFrame(root, padx=10, pady=10, bg='#8c8a89', fg='#660000', text='Endereço', font='Verdana 14 italic')
fr6 = Frame(root, padx=10, pady=10, bg='#8c8a89')
fr7 = Frame(root, padx=10, pady=10, bg='#8c8a89')
# ########################## widgets frame 0 ########################## #
lb1_fr0 = Label(fr0, text='Login:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb2_fr0 = Label(fr0, text='Senha:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
en1_fr0 = Entry(fr0, font='Verdana 12')
en2_fr0 = Entry(fr0, font='Verdana 12', show='*')
bt1_fr0 = Button(fr0, text='Entrar', font='Verdana 11', command=login)
# ########################## widgets frame 1 ########################## #
lb1_fr1 = Label(fr1, text='Nome:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb2_fr1 = Label(fr1, text='CPF:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb3_fr1 = Label(fr1, text='Telefone:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb4_fr1 = Label(fr1, text='Data Nasc:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb_5fr2 = Label(fr1, text='Sexo:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
en1_fr1 = Entry(fr1, font='Verdana 11')
en2_fr1 = Entry(fr1, font='Verdana 11', width=15)
en3_fr1 = Entry(fr1, font='Verdana 11', width=15)
en4_fr1 = Entry(fr1, font='Verdana 11', width=13)
rb1_fr1 = Checkbutton(fr1, text='Masculino', font='Verdana 12', anchor=W, pady=3, bg='#8c8a89',
                      highlightbackground='#8c8a89', activebackground='#8c8a89')
rb2_fr1 = Checkbutton(fr1, text='Feminino', font='Verdana 12', anchor=W, pady=3, bg='#8c8a89',
                      highlightbackground='#8c8a89', activebackground='#8c8a89')
# ########################## widgets frame 2 ########################## #
lb1_fr2 = Label(fr2, text='Rua:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb2_fr2 = Label(fr2, text='N°:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb3_fr2 = Label(fr2, text='Bairro:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb4_fr2 = Label(fr2, text='Cidade:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb5_fr2 = Label(fr2, text='UF:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
en1_fr2 = Entry(fr2, font='Verdana 12 bold')
en2_fr2 = Entry(fr2, font='Verdana 12 bold', width=6)
en3_fr2 = Entry(fr2, font='Verdana 12 bold')
en4_fr2 = Entry(fr2, font='Verdana 12 bold')
en5_fr2 = Entry(fr2, font='Verdana 12 bold', width=6)
# ########################## widgets frame 3 ########################## #
bt1_fr3 = Button(fr3, text='Gravar Dados', font='Verdana 11', command=gravar)
bt2_fr3 = Button(fr3, text='Consultar', font='Verdana 11', command=consultar)
bt3_fr3 = Button(fr3, text='Sair', font='Verdana 11', command=logout)
# ########################## widgets frame 4 ########################## #
lb1_fr4 = Label(fr4, text='Nome:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb2_fr4 = Label(fr4, text='CPF:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb3_fr4 = Label(fr4, text='Telefone:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb4_fr4 = Label(fr4, text='Data Nasc:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb_5fr4 = Label(fr4, text='Sexo:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
en1_fr4 = Entry(fr4, font='Verdana 11', state=DISABLED)
en2_fr4 = Entry(fr4, font='Verdana 11', width=15, state=DISABLED)
en3_fr4 = Entry(fr4, font='Verdana 11', width=15, state=DISABLED)
en4_fr4 = Entry(fr4, font='Verdana 11', width=13, state=DISABLED)
rb1_fr4 = Checkbutton(fr4, text='Masculino', font='Verdana 12', anchor=W, pady=3, bg='#8c8a89',
                      highlightbackground='#8c8a89', activebackground='#8c8a89')
rb2_fr4 = Checkbutton(fr4, text='Feminino', font='Verdana 12', anchor=W, pady=3, bg='#8c8a89',
                      highlightbackground='#8c8a89', activebackground='#8c8a89')
# ########################## widgets frame 5 ########################## #
lb1_fr5 = Label(fr5, text='Rua:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb2_fr5 = Label(fr5, text='N°:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb3_fr5 = Label(fr5, text='Bairro:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb4_fr5 = Label(fr5, text='Cidade:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb5_fr5 = Label(fr5, text='UF:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
en1_fr5 = Entry(fr5, font='Verdana 12 bold', state=DISABLED)
en2_fr5 = Entry(fr5, font='Verdana 12 bold', width=6, state=DISABLED)
en3_fr5 = Entry(fr5, font='Verdana 12 bold', state=DISABLED)
en4_fr5 = Entry(fr5, font='Verdana 12 bold', state=DISABLED)
en5_fr5 = Entry(fr5, font='Verdana 12 bold', width=6, state=DISABLED)
# ########################## widgets frame 6 ########################## #
bt1_fr6 = Button(fr6, text='Voltar', font='Verdana 11', command=voltar)
# ########################## widgets frame 7 ########################## #
lista_entrada_2 = lista_entrada_1
print(lista_entrada_2)

#mb1_fr7.menu = Menu(mb1_fr7)
#mb1_fr7["menu"] = mb1_fr7.menu
#mb1_fr7.menu.add_checkbutton(label='Hindi', variable=IntVar())
# ########################### layout frames ########################### #
fr0.pack(anchor=CENTER)
# ####################### layout widgets frame 0 ####################### #
lb1_fr0.grid(row=0, column=0, sticky=EW)
lb2_fr0.grid(row=1, column=0, sticky=EW)
en1_fr0.grid(row=0, column=1, sticky=EW)
en2_fr0.grid(row=1, column=1, sticky=EW)
bt1_fr0.grid(row=2, column=1)
# ####################### layout widgets frame 1 ####################### #
lb1_fr1.grid(row=1, column=0, sticky=EW)  # nome
lb2_fr1.grid(row=2, column=0, sticky=EW)  # cpf
lb3_fr1.grid(row=2, column=2, sticky=EW)  # telefone
lb4_fr1.grid(row=2, column=4, sticky=EW)  # data nasc
lb_5fr2.grid(row=3, column=0)
en1_fr1.grid(row=1, column=1, columnspan=5, sticky=EW)  # nome
en2_fr1.grid(row=2, column=1)  # cpf
en3_fr1.grid(row=2, column=3)  # telefone
en4_fr1.grid(row=2, column=5)  # data nasc.
rb1_fr1.grid(row=3, column=1, sticky=EW)
rb2_fr1.grid(row=3, column=2, sticky=EW)
# ####################### layout widgets frame 2 ####################### #
lb1_fr2.grid(row=1, column=0, sticky=EW)
lb2_fr2.grid(row=1, column=4, sticky=EW)
lb3_fr2.grid(row=2, column=0, sticky=EW)
lb4_fr2.grid(row=2, column=2, sticky=EW)
lb5_fr2.grid(row=2, column=4, sticky=EW)
en1_fr2.grid(row=1, column=1, columnspan=3, sticky=EW)
en2_fr2.grid(row=1, column=5)
en3_fr2.grid(row=2, column=1)
en4_fr2.grid(row=2, column=3)
en5_fr2.grid(row=2, column=5)
# ####################### layout widgets frame 3 ####################### #
bt1_fr3.grid(row=0, column=0)
bt2_fr3.grid(row=0, column=1, padx=3)
bt3_fr3.grid(row=0, column=2, padx=3)
# ####################### layout widgets frame 4 ####################### #
lb1_fr4.grid(row=1, column=0, sticky=EW)  # nome
lb2_fr4.grid(row=2, column=0, sticky=EW)  # cpf
lb3_fr4.grid(row=2, column=2, sticky=EW)  # telefone
lb4_fr4.grid(row=2, column=4, sticky=EW)  # data nasc
lb_5fr4.grid(row=3, column=0)
en1_fr4.grid(row=1, column=1, columnspan=5, sticky=EW)  # nome
en2_fr4.grid(row=2, column=1)  # cpf
en3_fr4.grid(row=2, column=3)  # telefone
en4_fr4.grid(row=2, column=5)  # data nasc.
rb1_fr4.grid(row=3, column=1, sticky=EW)
rb2_fr4.grid(row=3, column=2, sticky=EW)
# ####################### layout widgets frame 5 ####################### #
lb1_fr5.grid(row=1, column=0, sticky=EW)
lb2_fr5.grid(row=1, column=4, sticky=EW)
lb3_fr5.grid(row=2, column=0, sticky=EW)
lb4_fr5.grid(row=2, column=2, sticky=EW)
lb5_fr5.grid(row=2, column=4, sticky=EW)
en1_fr5.grid(row=1, column=1, columnspan=3, sticky=EW)
en2_fr5.grid(row=1, column=5)
en3_fr5.grid(row=2, column=1)
en4_fr5.grid(row=2, column=3)
en5_fr5.grid(row=2, column=5)
# ####################### layout widgets frame 6 ####################### #
bt1_fr6.grid(row=0, column=0)
# ####################### layout widgets frame 7 ####################### #

# ####################### bind ######################### #
en2_fr1.bind("<KeyRelease>", formata_cpf)
en3_fr1.bind("<KeyRelease>", formata_tel)
en4_fr1.bind("<KeyRelease>", formata_data)
root.mainloop()
