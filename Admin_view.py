import tkinter as tk
import tkinter.font as tkFont

class Admin_view:
    def __init__(self, root):
        #setting title
        root.title("Admin")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Productos_boton=tk.Button(root)
        Productos_boton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Productos_boton["font"] = ft
        Productos_boton["fg"] = "#000000"
        Productos_boton["justify"] = "center"
        Productos_boton["text"] = "Productos"
        Productos_boton.place(x=320,y=50,width=200,height=100)
        Productos_boton["command"] = self.GButton_444_command

        Usuarios_boton=tk.Button(root)
        Usuarios_boton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Usuarios_boton["font"] = ft
        Usuarios_boton["fg"] = "#000000"
        Usuarios_boton["justify"] = "center"
        Usuarios_boton["text"] = "Usuarios"
        Usuarios_boton.place(x=320,y=300,width=200,height=100)
        Usuarios_boton["command"] = self.GButton_341_command

        Tag_usuarios=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        Tag_usuarios["font"] = ft
        Tag_usuarios["fg"] = "#333333"
        Tag_usuarios["justify"] = "center"
        Tag_usuarios["text"] = "Usuarios"
        Tag_usuarios.place(x=60,y=300,width=220,height=100)

        Tag_productos=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        Tag_productos["font"] = ft
        Tag_productos["fg"] = "#333333"
        Tag_productos["justify"] = "center"
        Tag_productos["text"] = "Lista de productos"
        Tag_productos.place(x=60,y=50,width=220,height=100)

    def GButton_444_command(self):
        print("command")


    def GButton_341_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = Admin_view(root)
    root.mainloop()
