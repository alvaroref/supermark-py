import tkinter as tk
from tkinter import ttk
from cargar_objetos import cargaObjeto
from Clases import producto
import sqlite3 as sql
def lista_productos(texto):
    id_productos = []
    a = ""
    for i in str(texto):
        if i != " ":
            a += str(i)
        else:
            id_productos.append(a)
            a = ""
    if type(texto) == int:
        a = str(texto)
        return a
    return id_productos
def cantidad_de_productos(lista):
    id_productos = []
    a = ""
    for i in str(lista):
        if i != " ":
            a += str(i)
        else:
            id_productos.append(a)
            a = ""
    if type(lista) == int:
        a = str(lista)
        return a
    return id_productos
def productos_funcion(lista_ids,lista_cantidad):
    productos = []
    produs = "|"
    indice = 0
    for i in lista_ids:
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute(f"select * from productos where id_producto = {int(i)}")
        pr = cur.fetchone()
        con.close()
        try:
            productos.append(pr[4])
        except:
            pass
    for i in productos:
        produs += i +"-" +str(lista_cantidad[indice]) +"|"
        indice +=1
    return produs
class vista_admin_user:
    def __init__(self, root):
        self.root = root
        root.title("Ventana")
        w = 600
        h = 500
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        al = '%dx%d+%d+%d' % (w,h,(sw-w)/2,(sh-h)/2)
        root.geometry(al)
        root.resizable(width=False,height=False)
        self.bandera=0
        frame = tk.Frame(self.root)
        columns = ('id_venta','id_user','correo','productos')
        self.tree = ttk.Treeview(frame,columns=columns,show='headings')
        self.tree.column("id_venta",anchor="center", stretch="NO", width=100)
        self.tree.heading("id_venta", text="id_venta")
        self.tree.column("id_user" ,anchor="center", stretch="NO", width=100)
        self.tree.heading("id_user",text="id_user")
        self.tree.column("correo" ,anchor="center", stretch="NO", width=100)
        self.tree.heading("correo",text="correo")
        self.tree.column("productos" ,anchor="center", stretch="NO", width=300)
        self.tree.heading("productos",text="productos")
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute(f"select * from venta")
        ventas = cur.fetchall()
        con.close()
        id_cliente = []
        let = ""
        productos = []
        for venta in ventas:
            id_cliente.append(venta[1])
        for cliente in id_cliente:
            Lid_cliente = [*set(id_cliente)]
        for i in Lid_cliente:
            con = sql.connect('Supermark.db')
            cur = con.cursor()
            cur.execute(f"select * from venta where id_cliente = '{i}'")
            ventas = cur.fetchall()
            con.close()
            for venta in ventas:
                con = sql.connect('Supermark.db')
                cur = con.cursor()
                cur.execute(f"select * from detalle_venta where id_venta = '{venta[0]}'")
                pr = cur.fetchone()
                cur.execute(f"select * from Clientes where id_cliente = '{i}'")
                correo = cur.fetchone()
                con.close()
                try:
                    prd = lista_productos(pr[1])
                    can = cantidad_de_productos(pr[2])
                except:
                    prd = ""
                    pass
                if prd != []:
                    p = productos_funcion(prd,can)
                    if p != "|":
                        self.tree.insert('','end',values=(venta[0],str(i),correo[4],p))
        frame.grid(column = 0,row = 0,sticky="nsew")
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)
        self.tree.pack(side="left",fill="both",expand="TRUE")

if __name__=='__main__':
        root = tk.Tk()
        app = vista_admin_user(root)
        root.mainloop()