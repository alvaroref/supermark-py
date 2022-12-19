import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import sqlite3 as sql
from Clases import ProductoCarrito
import tkinter.messagebox as mbox
import os

class vista_usuario:
    def __init__(self, root):
        self.root = root
        root.title("Usuario")
        w = 600
        h = 500
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        al = '%dx%d+%d+%d' % (w,h,(sw-w)/2,(sh-h)/2)
        root.geometry(al)
        root.resizable(width=False,height=False)
        columns = ('nombre','precio','stock','descripcion')
        #creo el treeview con sus respectivos ids
        self.tree = ttk.Treeview(root,columns=columns,show='headings')
        self.tree.column("nombre",anchor="center", stretch="NO", width=100)
        self.tree.heading("nombre", text="nombre")
        self.tree.column("precio" ,anchor="center", stretch="NO", width=100)
        self.tree.heading("precio",text="precio")
        self.tree.column("stock" ,anchor="center", stretch="NO", width=100)
        self.tree.heading("stock",text="stock")
        self.tree.column("descripcion" ,anchor="center", stretch="NO", width=300)
        self.tree.heading("descripcion",text="descripcion")
        self.tree.pack(side="top")
        #llamo a la base de datos para cargar el treeview
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute(f"select * from productos where stock > 0")
        self.prod = cur.fetchall()
        con.close()
        for i in self.prod:
            self.tree.insert('','end',values=(i[4],i[2],i[3],i[1]))
        #defino la clase carrito con variables genericas para usar posteriormente
        self.producto = ProductoCarrito("producto","cantidad","precio")
        #defino mi listbox para el carrito
        self.listbox = tk.Listbox(root)
        self.listbox["justify"] = "left"
        self.listbox.place(x=0,y=245,width=600,height=200)
        self.listbox["selectmode"] = "single"
        self.listbox.insert(0,"producto"+"                    "+"cantidad"+"                    "+"precio")
        #self.listbox["setgrid"] = "True"

        #Creo el resto de widgets (botones,entrys,labels etc) para poder interactuar
        boton = tk.Button(root)
        boton["text"] = "agregar"
        boton.place(x=60,y=450,width=100,height=50)
        boton["command"] = self.boton_command

        botonelim = tk.Button(root)
        botonelim["text"] = "quitar"
        botonelim.place(x=160,y=450,width=100,height=50)
        botonelim["command"] = self.elim_command

        cantidadL = tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        cantidadL["font"] = ft
        cantidadL["fg"] = "#333333"
        cantidadL["justify"] = "center"
        cantidadL["text"] = "Cantidad a cargar"
        cantidadL.place(x=260,y=420,width=190,height=20)

        self.cantidad = tk.Entry(root)
        ft = tkFont.Font(family='Times',size=23)
        self.cantidad["font"] = ft
        self.cantidad["fg"] = "#333333"
        self.cantidad["justify"] = "center"
        self.cantidad["text"] = "Iniciar sesion"
        self.cantidad.place(x=300,y=450,width=100,height=30)

        botonefin = tk.Button(root)
        botonefin["text"] = "Finalizar compra"
        botonefin.place(x=460,y=450,width=120,height=50)
        botonefin["command"] = self.finalizar_compra
    def boton_command(self): # con esta funcion agrego los productos que se tienen en stock al carrito
            posicion = self.tree.selection()
            item = self.tree.item(posicion)
            cantidad = self.cantidad.get()
            if cantidad == "":
                cantidad = 1
            con = sql.connect('Supermark.db')
            cur = con.cursor()
            cur.execute(f"select * from productos where nombre = '{item['values'][0]}'")
            stock_prod = cur.fetchone()
            con.close()
            if int(cantidad) <= stock_prod[3]:
                bandera = self.producto.agregar(item['values'][0],cantidad,item['values'][1])
                tam_carrito = self.producto.tamlista()
                if tam_carrito <= 6:
                    valor = int(cantidad)*float(item['values'][1])
                    self.listbox.delete(bandera)
                    self.listbox.insert(bandera,item['values'][0]+"                    "+str(cantidad)+"                    "+str(valor))
                else:
                    self.producto.quitar_carrito(5)
                    mbox.showwarning("error","esta por superar el limite de productos en el carrito")
            else:
                mbox.showwarning("error","no hay sucificiente stock")
    def elim_command(self): # con esta funcion elimino productos del carrito
        posicion = self.listbox.curselection()
        plista = posicion[0]
        print(plista)
        if posicion:
            self.listbox.delete(posicion)
            self.producto.quitar_carrito(plista)

    def finalizar_compra(self):
        pagado = self.producto.total()
        mbox.showinfo("Se realizo la compra","total gastado: $"+str(pagado))
        os.remove("id_cliente.txt")
        self.root.destroy()
if __name__=='__main__':
        root = tk.Tk()
        app = vista_usuario(root)
        root.mainloop()
