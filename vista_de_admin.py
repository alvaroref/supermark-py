import tkinter as tk
from tkinter import ttk
from cargar_objetos import cargaObjeto
from Clases import producto
from modificar_productos import modificarObjeto
import sqlite3 as sql

class vista_admin_prod:
    def __init__(self, root):
        root.title("Ventana")
        self.root = root
        w = 600
        h = 500
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        al = '%dx%d+%d+%d' % (w,h,(sw-w)/2,(sh-h)/2)
        root.geometry(al)
        root.resizable(width=False,height=False)
        frame = tk.Frame(root,width=600,height=500,background="bisque")
        self.bandera=0
        columns = ('nombre','precio','stock','descripcion')
        self.tree = ttk.Treeview(frame,columns=columns,show='headings')
        self.tree.column("nombre",anchor="center", stretch="NO", width=100)
        self.tree.heading("nombre", text="nombre")
        self.tree.column("precio" ,anchor="center", stretch="NO", width=100)
        self.tree.heading("precio",text="precio")
        self.tree.column("stock" ,anchor="center", stretch="NO", width=100)
        self.tree.heading("stock",text="stock")
        self.tree.column("descripcion" ,anchor="center", stretch="NO", width=300)
        self.tree.heading("descripcion",text="descripcion")
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute(f"select * from productos")
        prod = cur.fetchall()
        con.close()
        for i in prod:
            self.tree.insert('','end',values=(i[4],i[2],i[3],i[1]))

        
        botonagregar = tk.Button(root)
        botonagregar["text"] = "agregar"
        botonagregar.place(x=100,y=450,width=100,height=50)
        botonagregar["command"] = self.agregar_command

        botonmodificar = tk.Button(root)
        botonmodificar["text"] = "modificar"
        botonmodificar.place(x=200,y=450,width=100,height=50)
        botonmodificar["command"] = self.modificar

        botonelim = tk.Button(root)
        botonelim["text"] = "quitar"
        botonelim.place(x=300,y=450,width=100,height=50)
        botonelim["command"] = self.elim_command

        botonrefrescar = tk.Button(root)
        botonrefrescar["text"] = "refrescar lista"
        botonrefrescar.place(x=400,y=450,width=100,height=50)
        botonrefrescar["command"] = self.refresh_window

        frame.pack(fill="both",expand=True)
        self.tree.pack(fill="both",expand=True)
    def agregar_command(self):
            cwindow = tk.Toplevel(self.root)
            reg=cargaObjeto(cwindow,self.root)
    def modificar(self):
            cwindow = tk.Toplevel(self.root)
            reg=modificarObjeto(cwindow,self.root)
    def elim_command(self):
        posicion = self.tree.selection()
        seleccion = self.tree.item(posicion)
        lista = seleccion['values']
        prod = producto(lista[3],lista[1],lista[2],lista[0])
        if posicion:
            prod.quitar_prod(lista[0])
            self.tree.delete(posicion)
    def refresh_window(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.__init__(self.root)
if __name__=='__main__':
        root = tk.Tk()
        app = vista_admin_prod(root)
        root.mainloop()