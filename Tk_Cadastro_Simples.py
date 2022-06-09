from tkinter import *


def valida_cpf(event=None):
    entrada = en2_fr1.get().replace('.', '').replace('-', '')[:11]
    nova_entrada = ''

    if event.keysym.lower() == "backspace":
        return

    for i in range(len(entrada)):

        if not entrada[i] in '0123456789':
            continue
        if i in [2, 5]:
            nova_entrada += entrada[i] + '.'
        elif i == 8:
            nova_entrada += entrada[i] + '-'
        else:
            nova_entrada += entrada[i]

    en2_fr1.delete(0, 'end')
    en2_fr1.insert(0, nova_entrada)


def valida_tel(entrada):
    if len(entrada) == 0 or len(entrada) <= 11 and entrada.isdigit():
        return True
    else:
        return False


# ############################## window ############################### #
root = Tk()
root.title('cadastro')
root.config(bg='#8c8a89')
root.config(pady=10, padx=10)
root.geometry('730x300')
root.resizable(width=False, height=False)
# ############################## frames ############################### #
fr0 = LabelFrame(root, padx=10, pady=10, bg='#8c8a89')
fr1 = LabelFrame(root, padx=10, pady=10, bg='#8c8a89', fg='#660000', text='Dados Pessoais', font='Verdana 14 italic')
fr2 = LabelFrame(root, padx=10, pady=10, bg='#8c8a89', fg='#660000', text='Endereço', font='Verdana 14 italic')
fr3 = Frame(root, padx=10, pady=10, bg='#8c8a89')
# ########################## widgets frame 0 ########################## #
lb1_fr0 = Label(fr0, text='Login:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb2_fr0 = Label(fr0, text='Senha:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
en1_fr0 = Entry(fr0, font='Verdana 12')
en2_fr0 = Entry(fr0, font='Verdana 12', show='*')
bt1_fr0 = Button(fr0, text='Entrar', font='Verdana 11', command=lambda: [fr0.pack_forget(), fr1.pack(fill=BOTH, anchor=W), fr2.pack(fill=BOTH, anchor=W), fr3.pack(fill=BOTH, anchor=NE)])
# ########################## widgets frame 1 ########################## #
lb1_fr1 = Label(fr1, text='Nome:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb2_fr1 = Label(fr1, text='CPF:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb3_fr1 = Label(fr1, text='Telefone:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb4_fr1 = Label(fr1, text='Data Nasc:', font='Verdana 12',  anchor=E, pady=3, bg='#8c8a89')
lb_5fr2 = Label(fr1, text='Sexo:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
en1_fr1 = Entry(fr1, font='Verdana 11')
en2_fr1 = Entry(fr1, font='Verdana 11', width=15)
en3_fr1 = Entry(fr1, font='Verdana 11', width=15, validate='key', validatecommand=(fr1.register(valida_tel), '%P'))
en4_fr1 = Entry(fr1, font='Verdana 11', width=13)
rb1_fr1 = Checkbutton(fr1, text='Masculino', font='Verdana 12', anchor=W, pady=3, bg='#8c8a89', highlightbackground='#8c8a89', activebackground='#8c8a89')
rb2_fr1 = Checkbutton(fr1, text='Feminino', font='Verdana 12', anchor=W, pady=3, bg='#8c8a89', highlightbackground='#8c8a89', activebackground='#8c8a89')
# ########################## widgets frame 2 ########################## #
lb1_fr2 = Label(fr2, text='Rua:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb2_fr2 = Label(fr2, text='N°:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb3_fr2 = Label(fr2, text='Bairro:', font='Verdana 12', anchor=E, pady=3, bg='#8c8a89')
lb4_fr2 = Label(fr2, text='Cidade:', font='Verdana 12',  anchor=E, pady=3, bg='#8c8a89')
lb5_fr2 = Label(fr2, text='UF:', font='Verdana 12',  anchor=E, pady=3, bg='#8c8a89')
en1_fr2 = Entry(fr2, font='Verdana 12 bold')
en2_fr2 = Entry(fr2, font='Verdana 12 bold', width=6)
en3_fr2 = Entry(fr2, font='Verdana 12 bold')
en4_fr2 = Entry(fr2, font='Verdana 12 bold')
en5_fr2 = Entry(fr2, font='Verdana 12 bold', width=6)
# ########################## widgets frame 3 ########################## #
bt1_fr3 = Button(fr3, text='Gravar Dados', font='Verdana 11')
bt2_fr3 = Button(fr3, text='Sair', font='Verdana 11', command=lambda: [fr0.pack(anchor=CENTER), fr1.pack_forget(), fr2.pack_forget(), fr3.pack_forget()])
# ########################### layout frames ########################### #
fr0.pack(anchor=CENTER)
# ####################### layout widgets frame 0 ####################### #
lb1_fr0.grid(row=0, column=0, sticky=EW)
lb2_fr0.grid(row=1, column=0, sticky=EW)
en1_fr0.grid(row=0, column=1, sticky=EW)
en2_fr0.grid(row=1, column=1, sticky=EW)
bt1_fr0.grid(row=2, column=1)
# ####################### layout widgets frame 1 ####################### #
lb1_fr1.grid(row=1, column=0, sticky=EW) # nome
lb2_fr1.grid(row=2, column=0, sticky=EW) # cpf
lb3_fr1.grid(row=2, column=2, sticky=EW) # telefone
lb4_fr1.grid(row=2, column=4, sticky=EW)  # data nasc
lb_5fr2.grid(row=3, column=0)
en1_fr1.grid(row=1, column=1, columnspan=5, sticky=EW) # nome
en2_fr1.grid(row=2, column=1) # cpf
en3_fr1.grid(row=2, column=3) # telefone
en4_fr1.grid(row=2, column=5) # data nasc.
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
# ####################### bind ######################### #
en2_fr1.bind("<KeyRelease>", valida_cpf)
root.mainloop()
