import tkinter as tk
import tkinter.font as tkFont
from Clases import producto
import tkinter.messagebox as mbox


class modificarObjeto:
    def __init__(self, root,mroot):
        #setting title
        self.root = root
        self.master = mroot
        root.title("Modificar producto")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.nombre=tk.Entry(root)
        self.nombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.nombre["font"] = ft
        self.nombre["fg"] = "#333333"
        self.nombre["justify"] = "center"
        self.nombre["text"] = "Nombre"
        self.nombre.place(x=160,y=20,width=260,height=30)

        self.descrip=tk.Entry(root)
        self.descrip["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.descrip["font"] = ft
        self.descrip["fg"] = "#333333"
        self.descrip["justify"] = "center"
        self.descrip["text"] = "descripción"
        self.descrip.place(x=160,y=130,width=261,height=98)

        self.precio=tk.Entry(root)
        self.precio["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.precio["font"] = ft
        self.precio["fg"] = "#333333"
        self.precio["justify"] = "center"
        self.precio["text"] = "precio"
        self.precio.place(x=300,y=250,width=122,height=30)

        self.stock=tk.Entry(root)
        self.stock["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.stock["font"] = ft
        self.stock["fg"] = "#333333"
        self.stock["justify"] = "center"
        self.stock["text"] = "stock"
        self.stock.place(x=300,y=300,width=121,height=30)

        nombre_producto=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        nombre_producto["font"] = ft
        nombre_producto["fg"] = "#333333"
        nombre_producto["justify"] = "center"
        nombre_producto["text"] = "Nombre del producto"
        nombre_producto.place(x=150,y=20,width=136,height=30)

        cambiar_descripcion=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        cambiar_descripcion["font"] = ft
        cambiar_descripcion["fg"] = "#333333"
        cambiar_descripcion["justify"] = "center"
        cambiar_descripcion["text"] = "Nueva descripcion"
        cambiar_descripcion.place(x=160,y=100,width=150,height=25)

        nuevo_precio=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        nuevo_precio["font"] = ft
        nuevo_precio["fg"] = "#333333"
        nuevo_precio["justify"] = "center"
        nuevo_precio["text"] = "Precio nuevo"
        nuevo_precio.place(x=160,y=250,width=130,height=25)

        agregarstock=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        agregarstock["font"] = ft
        agregarstock["fg"] = "#333333"
        agregarstock["justify"] = "center"
        agregarstock["text"] = "stock(+/-)"
        agregarstock.place(x=200,y=300,width=70,height=25)

        self.boton2 = tk.Button(root)
        self.boton2["font"] = ft
        self.boton2["fg"] = "#333333"
        self.boton2["justify"] = "center"
        self.boton2["text"] = "modificar"
        self.boton2.place(x=200,y=350,width=100,height=50)
        self.boton2["command"]=self.modificarProd

        aclaracion = tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        aclaracion["font"] = ft
        aclaracion["fg"] = "#FF0000"
        aclaracion["justify"] = "center"
        aclaracion["text"] = "Introducir nombre y solo llenar los campos que se van a modificar"
        aclaracion.place(x=50,y=420,width=510,height=30)
    def modificarProd(self):
        nombre = self.nombre.get()
        descripcion = self.descrip.get()
        precio = self.precio.get()
        stock = self.stock.get()
        if nombre != "":
            prod = producto(descripcion,precio,stock,nombre)
            if descripcion != "":
                prod.modificar_descripcion(descripcion)
            if str(precio) != "":
                prod.cambiar_precio(precio)
            if str(stock) != "" and int(stock) > 0:
                prod.agregar_stock(int(stock))
            if str(stock) != "" and int(stock) < 0:
                prod.quitar_stock(int(0-int(stock)))
            self.master.update()
            self.root.destroy()
        else:
            mbox.showwarning("debe ingresar un nombre")
            self.root.destry()
if __name__ == "__main__":
    root = tk.Tk()
    app = modificarObjeto(root)
    root.mainloop()
