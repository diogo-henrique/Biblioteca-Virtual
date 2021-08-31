from export import sql_to_table
from sqlite3.dbapi2 import connect
from tkinter import *
import backend


#funções dos botões

def ver_todos():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)   
    
def pesquisar():
    a = titulo_text.get()
    b = autor_text.get()
    c = estilo_text.get()
    d = entregue_text.get()
    e = dedicatoria_text.get()

    if a == "":
        a = " "
    if b == "":
        b = " "
    if c == "":
        c = " "
    if d == "":
        d = " "
    if e == "":
        e = " "

    list1.delete(0,END)
    for row in backend.search(a,b,c,d,e):
        list1.insert(END,row)

def inserir():
    list1.delete(0,END)

    backend.insert(titulo_text.get(),autor_text.get(),estilo_text.get(),entregue_text.get(),dedicatoria_text.get())

    list1.insert(END,(titulo_text.get(),autor_text.get(),estilo_text.get(),entregue_text.get()))

def get_selected_row(event):
    try:
        global selected_touple
        index =list1.curselection()[0]
        selected_touple = list1.get(index)
        
        titulo.delete(0,END)
        titulo.insert(END,list1.get(index)[1])
        autor.delete(0,END)
        autor.insert(END,list1.get(index)[2])
        estilo.delete(0,END)
        estilo.insert(END,list1.get(index)[3])
        entregue.delete(0,END)
        entregue.insert(END,list1.get(index)[4])
        dedicatoria.delete(0,END)
        dedicatoria.insert(END,list1.get(index)[5])

    except:
        pass

def deletar():
    backend.delete(selected_touple[0])
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def editar():
    try:
        a = titulo_text.get()
        b = autor_text.get()
        c = estilo_text.get()
        d = entregue_text.get()
        e = dedicatoria_text.get()

        if a == "":
            a = " "
        if b == "":
            b = " "
        if c == "":
            c = " "
        if d == "":
            d = " "
        if e == "":
            e = " "

        index =list1.curselection()[0]
        selected_touple = list1.get(index)
        backend.update(selected_touple[0],a,b,c,d,e)
        list1.delete(0,END)
        for row in backend.view():
            list1.insert(END,row)
    except:
        pass

def exportar():
    sql_to_table(backend.view(),entry_value.get())

#janela secundária


def abrir():
    p = Toplevel()
    p.geometry('180x100')

    fontP = ("Helvetica",11)
    p.title("Exportar")
    p.iconbitmap("book_icon_v11_64.ico")

    rotulo1 = Label(p, text="Deseja exportar o arquivo?",font=fontP)
    rotulo1.grid(row=0,column=0,columnspan=2)

    rotulo2 = Label(p,text='Nome:',font=fontP)
    rotulo2.grid(row=1,column=0)
    global entry_value
    entry_value = StringVar()
    entry = Entry(p,width=15,textvariable=entry_value)
    entry.grid(row=1,column=1)

    salvar = Button(p,text="Salvar",font=fontP,pady=10,command=exportar,height=1,width=5)
    salvar.grid(row=2,column=0)
    

    cancelar = Button(p,text="Fechar",font=fontP,pady=10,command=p.destroy)
    cancelar.grid(row=2,column=1)

    
    p.mainloop()

#criação da janela principal
window = Tk()
cor1 = "#b0b3a6"
cor2 = '#efeee8'
cor3 = '#b0b3a6'
col4 = '#06160f'
window.configure(bg= cor1)
window.resizable(0, 0)

#criação do ícone e título da janela
window.iconbitmap("book_icon_v11_64.ico")
window.title('Biblioteca Dinâmica')

#criação dos rótulos
myFont = font=("Helvetica",16)

l1 = Label(window,text='Livro',font=myFont,bg=cor1,fg=col4)
l1.grid(row=0,column=0,pady=10)

l2 = Label(window,text='Autor',font=myFont,bg=cor1,fg=col4)
l2.grid(row=1,column=0,pady=10)

l3 = Label(window,text='Estilo',font=myFont,bg=cor1,fg=col4)
l3.grid(row=0,column=2)

l4 = Label(window,text='Dado a',font=myFont,bg=cor1,fg=col4)
l4.grid(row=1,column=2)

l5 = Label(window,text='Dedicado',font=myFont,bg=cor1,fg=col4)
l5.grid(row=1,column=4)

#Criação das caixas de entrada
titulo_text = StringVar()
titulo = Entry(window, textvariable=titulo_text,font=myFont,bg=cor2)
titulo.grid(row=0,column=1,padx=5 )

autor_text = StringVar()
autor = Entry(window,textvariable=autor_text,font=myFont,bg=cor2)
autor.grid(row=1,column=1,padx=5 )

estilo_text = StringVar()
estilo = Entry(window,textvariable=estilo_text,font=myFont,bg=cor2)
estilo.grid(row=0,column=3,padx=5 )

entregue_text = StringVar()
entregue = Entry(window,textvariable=entregue_text,font=myFont,bg=cor2)
entregue.grid(row=1,column=3,padx=5 )

dedicatoria_text = StringVar()
dedicatoria = Entry(window,textvariable=dedicatoria_text,font=myFont,bg=cor2,width=2)
dedicatoria.grid(row=1,column=5)

#criação dos botões
buttonFont = ("Helvetica",18)

b1 = Button(window, text="Ver todos",width=12,command=ver_todos,font=buttonFont,bg=cor3)
b1.grid(row=2,column=4,columnspan=2,padx=(0,5))

b2 = Button(window, text="Pesquisar",width=12,command=pesquisar,font=buttonFont,bg=cor3)
b2.grid(row=3,column=4,columnspan=2,padx=(0,5))

b3 = Button(window, text="Inserir",width=12,command=inserir,font=buttonFont,bg=cor3)
b3.grid(row=4,column=4,columnspan=2,padx=(0,5))

b4 = Button(window, text="Deletar",width=12,command=deletar,font=buttonFont,bg=cor3)
b4.grid(row=5,column=4,columnspan=2,padx=(0,5))

b5 = Button(window, text="Editar",width=12,command=editar,font=buttonFont,bg=cor3)
b5.grid(row=6,column=4,columnspan=2,padx=(0,5))

b6 = Button(window, text="Exportar",width=12,command=abrir,font=buttonFont,bg=cor3)
b6.grid(row=7,column=4,pady=(0,5),padx=(0,5),columnspan=2)


#Criação da barra de rolagem

scroll= Scrollbar(window)
scroll.grid(column=0,row=2,rowspan=6,sticky='ns',pady=5)

#criação da Listbox que vai servir de display da base de dados

list1 = Listbox(window,font=("Helvetica"),bg=cor2)
list1.grid(row=2,column=1,columnspan=3,rowspan=6,padx=10,pady=(0,5),sticky='nsew')
list1.bind('<<ListboxSelect>>',get_selected_row)

list1.configure(yscrollcommand=scroll.set)
scroll.configure(command=list1.yview)

window.mainloop()
