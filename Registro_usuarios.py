import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as mbox
from Clases import Cliente
from Clases import Usuario
from user_view import vista_usuario
import sqlite3 as sql

class Registrar_usuario:
    def __init__(self, root):
        #setting title
        root.title("Supermark-UserReg")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_825=tk.Label(root)
        ft = tkFont.Font(family='Times',size=38)
        GLabel_825["font"] = ft
        GLabel_825["fg"] = "#333333"
        GLabel_825["justify"] = "center"
        GLabel_825["text"] = "Registro de usuario"
        GLabel_825.place(x=80,y=20,width=432,height=93)

        GLabel_97=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_97["font"] = ft
        GLabel_97["fg"] = "#333333"
        GLabel_97["justify"] = "center"
        GLabel_97["text"] = "Nombre"
        GLabel_97.place(x=80,y=110,width=110,height=50)

        GLabel_201=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_201["font"] = ft
        GLabel_201["fg"] = "#333333"
        GLabel_201["justify"] = "center"
        GLabel_201["text"] = "Apellido"
        GLabel_201.place(x=70,y=160,width=120,height=50)

        GLabel_993=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_993["font"] = ft
        GLabel_993["fg"] = "#333333"
        GLabel_993["justify"] = "center"
        GLabel_993["text"] = "Domicilio"
        GLabel_993.place(x=70,y=210,width=120,height=50)

        botonreg=tk.Button(root)
        botonreg["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        botonreg["font"] = ft
        botonreg["fg"] = "#000000"
        botonreg["justify"] = "center"
        botonreg["text"] = "Registrarse"
        botonreg.place(x=250,y=440,width=100,height=42)
        botonreg["command"] = self.agregar_datos

        GLabel_297=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_297["font"] = ft
        GLabel_297["fg"] = "#333333"
        GLabel_297["justify"] = "center"
        GLabel_297["text"] = "Correo"
        GLabel_297.place(x=80,y=260,width=100,height=50)

        GLabel_784=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_784["font"] = ft
        GLabel_784["fg"] = "#333333"
        GLabel_784["justify"] = "center"
        GLabel_784["text"] = "Dni"
        GLabel_784.place(x=80,y=310,width=100,height=50)

        GLabel_856=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_856["font"] = ft
        GLabel_856["fg"] = "#333333"
        GLabel_856["justify"] = "center"
        GLabel_856["text"] = "Clave"
        GLabel_856.place(x=80,y=360,width=100,height=50)

        self.nombre=tk.Entry(root)
        self.nombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.nombre["font"] = ft
        self.nombre["fg"] = "#333333"
        self.nombre["justify"] = "center"
        self.nombre["text"] = "Nombre"
        self.nombre.place(x=200,y=120,width=240,height=30)

        self.apellido=tk.Entry(root)
        self.apellido["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.apellido["font"] = ft
        self.apellido["fg"] = "#333333"
        self.apellido["justify"] = "center"
        self.apellido["text"] = "Apellido"
        self.apellido.place(x=200,y=170,width=240,height=30)

        self.domicilio=tk.Entry(root)
        self.domicilio["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.domicilio["font"] = ft
        self.domicilio["fg"] = "#333333"
        self.domicilio["justify"] = "center"
        self.domicilio["text"] = "Domicilio"
        self.domicilio.place(x=200,y=220,width=240,height=30)

        self.correo=tk.Entry(root)
        self.correo["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.correo["font"] = ft
        self.correo["fg"] = "#333333"
        self.correo["justify"] = "center"
        self.correo["text"] = "Correo"
        self.correo.place(x=200,y=270,width=240,height=30)

        self.dni=tk.Entry(root)
        self.dni["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.dni["font"] = ft
        self.dni["fg"] = "#333333"
        self.dni["justify"] = "center"
        self.dni["text"] = "Dni"
        self.dni.place(x=200,y=320,width=240,height=30)

        self.clave=tk.Entry(root)
        self.clave["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.clave["font"] = ft
        self.clave["fg"] = "#333333"
        self.clave["justify"] = "center"
        self.clave["text"] = "Clave"
        self.clave.place(x=200,y=370,width=240,height=30)

    def agregar_datos(self):
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        domicilio = self.domicilio.get()
        correo = self.correo.get()
        dni = self.dni.get()
        clave = self.clave.get()
        if nombre != "" and apellido != "" and domicilio != "" and correo != "" and dni != "" and clave != "":
            cliente = Cliente(nombre,apellido,domicilio,correo,dni)
            user = Usuario(correo,clave)
            con = sql.connect('Supermark.db',timeout = 10)
            cur = con.cursor()
            cur.execute(f"select * from Clientes where correo = '{correo}' ")
            llave = cur.fetchone()
            con.close()
            if llave != None:
                mbox.showwarning("error","ya existe el usuario")
            else:
                user.registrar_user()
                cliente.registrar_cliente()
                con = sql.connect('Supermark.db',timeout = 10)
                cur = con.cursor()
                cur.execute(f"select * from Clientes where correo = '{correo}' ")
                cliente = cur.fetchone()
                con.close()
                file = open("id_cliente.txt", "w")
                file.write(str(cliente[0]))
                file.close()
                r = tk.Tk()
                user = vista_usuario(r)
        else:
            mbox.showwarning("error","falta completar un campo")


if __name__ == "__main__":
    root = tk.Tk()
    app = Registrar_usuario(root)
    root.mainloop()
