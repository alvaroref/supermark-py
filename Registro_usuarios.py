import tkinter as tk
import tkinter.font as tkFont

class App:
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

        GButton_712=tk.Button(root)
        GButton_712["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_712["font"] = ft
        GButton_712["fg"] = "#000000"
        GButton_712["justify"] = "center"
        GButton_712["text"] = "Registrarse"
        GButton_712.place(x=250,y=440,width=100,height=42)
        GButton_712["command"] = self.GButton_712_command

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

        GLineEdit_937=tk.Entry(root)
        GLineEdit_937["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_937["font"] = ft
        GLineEdit_937["fg"] = "#333333"
        GLineEdit_937["justify"] = "center"
        GLineEdit_937["text"] = "Nombre"
        GLineEdit_937.place(x=200,y=120,width=240,height=30)

        GLineEdit_1=tk.Entry(root)
        GLineEdit_1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_1["font"] = ft
        GLineEdit_1["fg"] = "#333333"
        GLineEdit_1["justify"] = "center"
        GLineEdit_1["text"] = "Apellido"
        GLineEdit_1.place(x=200,y=170,width=240,height=30)

        GLineEdit_241=tk.Entry(root)
        GLineEdit_241["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_241["font"] = ft
        GLineEdit_241["fg"] = "#333333"
        GLineEdit_241["justify"] = "center"
        GLineEdit_241["text"] = "Domicilio"
        GLineEdit_241.place(x=200,y=220,width=240,height=30)

        GLineEdit_153=tk.Entry(root)
        GLineEdit_153["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_153["font"] = ft
        GLineEdit_153["fg"] = "#333333"
        GLineEdit_153["justify"] = "center"
        GLineEdit_153["text"] = "Correo"
        GLineEdit_153.place(x=200,y=270,width=240,height=30)

        GLineEdit_713=tk.Entry(root)
        GLineEdit_713["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_713["font"] = ft
        GLineEdit_713["fg"] = "#333333"
        GLineEdit_713["justify"] = "center"
        GLineEdit_713["text"] = "Dni"
        GLineEdit_713.place(x=200,y=320,width=240,height=30)

        GLineEdit_745=tk.Entry(root)
        GLineEdit_745["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_745["font"] = ft
        GLineEdit_745["fg"] = "#333333"
        GLineEdit_745["justify"] = "center"
        GLineEdit_745["text"] = "Clave"
        GLineEdit_745.place(x=200,y=370,width=240,height=30)

    def GButton_712_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
