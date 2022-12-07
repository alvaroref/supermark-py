import tkinter as tk
import tkinter.font as tkFont

class Inicio_sesion:
    def __init__(self, root):
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

        GLineEdit_344=tk.Entry(root)
        GLineEdit_344["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_344["font"] = ft
        GLineEdit_344["fg"] = "#333333"
        GLineEdit_344["justify"] = "center"
        GLineEdit_344["text"] = "Correo"
        GLineEdit_344.place(x=220,y=90,width=300,height=30)

        GLineEdit_184=tk.Entry(root)
        GLineEdit_184["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_184["font"] = ft
        GLineEdit_184["fg"] = "#333333"
        GLineEdit_184["justify"] = "center"
        GLineEdit_184["text"] = "Contraseña"
        GLineEdit_184.place(x=220,y=190,width=300,height=30)

        GButton_655=tk.Button(root)
        GButton_655["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_655["font"] = ft
        GButton_655["fg"] = "#000000"
        GButton_655["justify"] = "center"
        GButton_655["text"] = "Ingresar"
        GButton_655.place(x=230,y=270,width=150,height=40)
        GButton_655["command"] = self.GButton_655_command

        GButton_703=tk.Button(root)
        GButton_703["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_703["font"] = ft
        GButton_703["fg"] = "#000000"
        GButton_703["justify"] = "center"
        GButton_703["text"] = "Registrarse"
        GButton_703.place(x=230,y=410,width=150,height=40)
        GButton_703["command"] = self.GButton_703_command

        GLabel_176=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_176["font"] = ft
        GLabel_176["fg"] = "#333333"
        GLabel_176["justify"] = "center"
        GLabel_176["text"] = "Iniciar sesion"
        GLabel_176.place(x=120,y=20,width=400,height=40)

        GLabel_768=tk.Label(root)
        ft = tkFont.Font(family='Times',size=23)
        GLabel_768["font"] = ft
        GLabel_768["fg"] = "#333333"
        GLabel_768["justify"] = "center"
        GLabel_768["text"] = "Crear usuario"
        GLabel_768.place(x=110,y=340,width=400,height=40)

    def GButton_655_command(self):
        print("command")


    def GButton_703_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = Inicio_sesion(root)
    root.mainloop()
