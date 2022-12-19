import tkinter as tk
import tkinter.font as tkFont
from Registro_usuarios import Registrar_usuario
from user_view import vista_usuario
import sqlite3 as sql
import tkinter.messagebox as mbox
from Admin_view import Admin_view

class Inicio_sesion:
    def __init__(self, root):
        self.root = root
        #setting title
        root.title("Iniciar sesion")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_944=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_944["font"] = ft
        GLabel_944["fg"] = "#333333"
        GLabel_944["justify"] = "center"
        GLabel_944["text"] = "Correo"
        GLabel_944.place(x=50,y=80,width=150,height=50)

        GLabel_904=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_904["font"] = ft
        GLabel_904["fg"] = "#333333"
        GLabel_904["justify"] = "center"
        GLabel_904["text"] = "Contraseña"
        GLabel_904.place(x=50,y=170,width=150,height=50)

        self.correo=tk.Entry(root)
        self.correo["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.correo["font"] = ft
        self.correo["fg"] = "#333333"
        self.correo["justify"] = "center"
        self.correo["text"] = "Correo"
        self.correo.place(x=220,y=90,width=300,height=30)

        self.contraseña=tk.Entry(root)
        self.contraseña["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.contraseña["font"] = ft
        self.contraseña["fg"] = "#333333"
        self.contraseña["justify"] = "center"
        self.contraseña["text"] = "Contraseña"
        self.contraseña.place(x=220,y=190,width=300,height=30)

        inicion_sesion=tk.Button(root)
        inicion_sesion["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        inicion_sesion["font"] = ft
        inicion_sesion["fg"] = "#000000"
        inicion_sesion["justify"] = "center"
        inicion_sesion["text"] = "Ingresar"
        inicion_sesion.place(x=230,y=270,width=150,height=40)
        inicion_sesion["command"] = self.iniciar_sesion

        boton_registro=tk.Button(root)
        boton_registro["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        boton_registro["font"] = ft
        boton_registro["fg"] = "#000000"
        boton_registro["justify"] = "center"
        boton_registro["text"] = "Registrarse"
        boton_registro.place(x=230,y=410,width=150,height=40)
        boton_registro["command"] = self.b_registro

        inicio_sesion=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        inicio_sesion["font"] = ft
        inicio_sesion["fg"] = "#333333"
        inicio_sesion["justify"] = "center"
        inicio_sesion["text"] = "Iniciar sesion"
        inicio_sesion.place(x=120,y=20,width=400,height=40)

        GLabel_768=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_768["font"] = ft
        GLabel_768["fg"] = "#333333"
        GLabel_768["justify"] = "center"
        GLabel_768["text"] = "Crear usuario"
        GLabel_768.place(x=110,y=340,width=400,height=40)

        self.administrador = "2"

    def iniciar_sesion(self):
        #obtengo los datos de los campos de entrada
        correo = self.correo.get().replace(" ","")
        cont = self.contraseña.get().replace(" ","")
        print("correo: "+correo+"   contraseña: "+cont)
        #conexion base de datos
        con = sql.connect('Supermark.db',timeout = 10)
        cur = con.cursor()
        cur.execute(f"select * from usuarios where nombreusuario = '{correo}' ")
        usuario = cur.fetchone()
        cur.execute(f"select * from Clientes where correo = '{correo}' ")
        cliente = cur.fetchone()
        con.close()
        admin = False

        if usuario != None and usuario[0] == correo and usuario[1] == cont and correo == self.administrador:
            print("ya existe el usuario")
            admin = True
        if correo == "" or cont == "" or usuario == None or usuario[0] != correo or usuario[1] != cont:
            mbox.showwarning(title="error",message="el usuario no existe o la contraseña es incorrecta")
        if admin:
            r = tk.Toplevel(self.root)
            adm = Admin_view(r)
        if correo != "" and correo != self.administrador and correo == usuario[0] and cont == usuario[1]:
            file = open("id_cliente.txt", "w")
            file.write(str(cliente[0]))
            file.close()
            r = tk.Toplevel(self.root)
            user = vista_usuario(r)

    def b_registro(self):
        r = tk.Toplevel(self.root)
        reg = Registrar_usuario(r)

if __name__ == "__main__":
    root = tk.Tk()
    app = Inicio_sesion(root)
    root.mainloop()
