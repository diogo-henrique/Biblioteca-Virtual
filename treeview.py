from tkinter import *
from tkinter import ttk

my_tree = ttk.Treeview(window)
my_tree['columns'] =("name,ID,Favorite pizza")
my_tree.column('#0',width=120,minwidth=25)
my_tree.column('name',anchor=W,width=120,minwidth=25)
my_tree.column('ID',anchor=CENTER,width=80,minwidth=25)
my_tree.column('Favorite pizza',anchor=W,width=120,minwidth=25)

my_tree.heading('#0',text= 'label',anchor=W)
my_tree.heading('name',text='name',anchor=W)
my_tree.heading('ID',text='Id',anchor=CENTER)
my_tree.heading('Favorite pizza',text='favorite pizza',anchor=W)

