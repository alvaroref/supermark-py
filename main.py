from Inicio_sesion import Inicio_sesion
from Principal import vista_principal
import tkinter as tk
import tkinter.font as tkFont


if __name__ == "__main__":
    root = tk.Tk()
    app = vista_principal(root)
    
    root.mainloop()
