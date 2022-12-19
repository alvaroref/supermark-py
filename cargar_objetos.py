import tkinter as tk
import tkinter.font as tkFont
from Clases import producto
import tkinter.messagebox as mbox


class cargaObjeto:
    def __init__(self, root,mroot):
        #setting title
        self.root = root
        self.master = mroot
        root.title("objetos")
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
        self.nombre.place(x=160,y=60,width=260,height=30)

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

        GLabel_403=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_403["font"] = ft
        GLabel_403["fg"] = "#333333"
        GLabel_403["justify"] = "center"
        GLabel_403["text"] = "Nombre del producto"
        GLabel_403.place(x=150,y=20,width=136,height=30)

        GLabel_235=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_235["font"] = ft
        GLabel_235["fg"] = "#333333"
        GLabel_235["justify"] = "center"
        GLabel_235["text"] = "Descripción"
        GLabel_235.place(x=160,y=100,width=70,height=25)

        GLabel_531=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_531["font"] = ft
        GLabel_531["fg"] = "#333333"
        GLabel_531["justify"] = "center"
        GLabel_531["text"] = "Precio"
        GLabel_531.place(x=140,y=250,width=70,height=25)

        GLabel_260=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_260["font"] = ft
        GLabel_260["fg"] = "#333333"
        GLabel_260["justify"] = "center"
        GLabel_260["text"] = "Stock"
        GLabel_260.place(x=140,y=300,width=70,height=25)

        self.boton = tk.Button(root)
        self.boton["font"] = ft
        self.boton["fg"] = "#333333"
        self.boton["justify"] = "center"
        self.boton["text"] = "Agregar"
        self.boton.place(x=200,y=350,width=100,height=50)
        self.boton["command"]=self.agregarProd

    def agregarProd(self):
        nombre = self.nombre.get()
        descripcion = self.descrip.get()
        precio = self.precio.get()
        stock = self.stock.get()
        if nombre != "" and descripcion != "" and precio != "" and stock != "":
            prod = producto(descripcion,precio,stock,nombre)
            print(prod)
            prod.cargar_producto()
            self.master.update()
            self.root.destroy()
        else:
            mbox.showwarning("error","falto completar algun campo")

if __name__ == "__main__":
    root = tk.Tk()
    app = cargaObjeto(root)
    root.mainloop()
