from http import client
import sqlite3 as sql

class Usuario():
    def __init__(self,nombreUser,clave,tipo = None):
        self.__nombreUser = nombreUser
        self.__clave = clave
        self.__tipo = tipo
    def registrar_user(self):
        while True:
            con = sql.connect('Supermark.db',timeout = 10)
            cur = con.cursor()
            cur.execute(f"select * from Clientes where correo = '{self.__correo}' ")
            usuario = cur.fetchone()
            if usuario != None:
                    print("ya existe el usuario")
                    self.__correo = input("ingrese correo: ").replace(" ","")
            else:
                    break
            con.close()
        cur.execute("INSERT INTO usuarios VALUES (?,?)",(self.__nombreUser,self.__clave))
        con.commit()
        con.close()

class Cliente():
    def __init__(self,nombre ,apellido ,domicilio ,correo ,dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__domicilio = domicilio
        self.__correo = correo
        self.__dni = dni

    def __str__(self):
        return self.__nombre+ "\n" + self.__apellido +"\n"+ self.__domicilio+"\n" + self.__correo+"\n" + str(self.__dni)
    def registrar_cliente(self):
        while(True):
            con = sql.connect('Supermark.db')
            cur = con.cursor()
            cur.execute(f"select * from Clientes where correo = '{self.__correo}' ")
            usuario = cur.fetchone()
            if usuario != None:
                print("ya existe el usuario")
                self.__correo = input("ingrese correo: ").replace(" ","")
            else:
                break
            con.close()
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute("INSERT INTO Clientes(apellido,nombre,dni,correo,domicilio) VALUES (?,?,?,?,?)",(self.__apellido,self.__nombre,self.__domicilio, self.__correo,self.__dni))
        con.commit()
        con.close()
    def mostrar_productos(self):
        con = sql.connect('supermark.db')
        cur = con.cursor()
        cur.execute("select * from productos")
        productos = cur.fetchall()
        for produc in productos:
            print(produc)
        con.close()
    #para recuperar cur.lastidrow

class producto():
    def __init__(self,descripcion,precio,stock,nombre):
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock
        self.__nombre = nombre
    def __str__(self):
        return self.__descripcion+ "\n" + str(self.__precio)+"\n" + str(self.__stock) +"\n"+self.__nombre

    def cargar_producto(self):
        while(True):
            con = sql.connect('Supermark.db')
            cur = con.cursor()
            cur.execute(f"select * from productos where nombre = '{self.__nombre}' ")
            prod = cur.fetchone()
            con.close()
            if prod != None:
                print("ya existe el producto")
                self.__nombre = input("ingrese otro producto: ").replace(" ","")
                self.__descripcion = input("ingrese una nueva descripcion ")
            else:
                break
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute("INSERT INTO productos(descripcion,precio,stock,nombre) VALUES (?,?,?,?)",(self.__descripcion,self.__precio,self.__stock,self.__nombre))
        con.commit()
        con.close()
    
    def quitar_stock(self, cantidad):
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute(f"select * from productos where nombre = '{self.__nombre}' ")
        prod = cur.fetchone()
        self.__stock = prod[3] - cantidad
        cur.execute(f"UPDATE productos SET stock = {self.__stock} where nombre = '{self.__nombre}'")
        con.commit()
        con.close()

    def agregar_stock(self, cantidad):
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute(f"select * from productos where nombre = '{self.__nombre}' ")
        prod = cur.fetchone()
        self.__stock = prod[3] + cantidad
        cur.execute(f"UPDATE productos SET stock = {self.__stock} where nombre = '{self.__nombre}'")
        con.commit()
        con.close()

    def modificar_descripcion(self,descripcion):
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute(f"select * from productos where nombre = '{self.__descripcion}' ")
        prod = cur.fetchone()
        self.__descripcion = descripcion
        cur.execute(f"UPDATE productos SET stock = {self.__descripcion} where nombre = '{self.__nombre}'")
        con.commit()
        con.close()

    def cambiar_nombre(self,nombre):
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute(f"UPDATE productos SET stock = {nombre} where nombre = '{self.__nombre}'")
        con.commit()
        con.close()
class ProductoCarrito():
    def __init__(self, Producto, cantidad):
        self.__Producto = Producto
        self.__cantidad = cantidad

class Carrito():
    def __init__(self,ProductoCarrito):
        self.__ProductosCarrito = ProductoCarrito

class RegistroDatos():
    def RegistrarCliente(self):
        nombre = input("ingrese nombre")
        apellido = input("ingrese apellido")
        dom = input("ingrese domicilio")
        correo = input("ingrese correo").replace(" ","")
        dni = int(input("ingrese DNI"))
        Datos = Cliente(apellido,nombre,dni,correo,dom)
        return Datos
    def RegistrarUsuario(self):
        correo = input("ingrese correo")
        clave = input("Ingrese Clave")
        User = Usuario(correo,clave)
        return User

if __name__ == "__main__":
    '''reg = RegistroDatos()
    cliente1 = reg.RegistrarCliente()
    user1 = reg.RegistrarUsuario()
    cliente1.registrar_cliente()
    user1.registrar_user()
    print(cliente1)
    print(user1)'''
    pr = producto("galletas",100 , 150 ,"q")
    cl.mostrar_productos()
    print(pr)
