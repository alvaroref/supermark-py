import tkinter as tk
import tkinter.font as tkFont

from Inicio_sesion import Inicio_sesion


class vista_principal:
    def __init__(self, root):
        #setting title
        root.title("Inicio")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Usuario_boton=tk.Button(root)
        Usuario_boton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Usuario_boton["font"] = ft
        Usuario_boton["fg"] = "#000000"
        Usuario_boton["justify"] = "center"
        Usuario_boton["text"] = "Usuario"
        Usuario_boton.place(x=110,y=50,width=400,height=150)
        Usuario_boton["command"] = self.usuario_command

        Administrador_boton=tk.Button(root)
        Administrador_boton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Administrador_boton["font"] = ft
        Administrador_boton["fg"] = "#000000"
        Administrador_boton["justify"] = "center"
        Administrador_boton["text"] = "Administrador"
        Administrador_boton.place(x=110,y=300,width=400,height=150)
        Administrador_boton["command"] = self.administrador_command

    def usuario_command(self):
        print("Usuario")
        app = Inicio_sesion(tk.Tk()) 
        return "Usuario"


    def administrador_command(self):
        print("admin")
        return "Admin"

if __name__ == "__main__":
    root = tk.Tk()
    app = vista_principal(root)
    root.mainloop()

