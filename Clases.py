from http import client
import sqlite3 as sql
import tkinter.messagebox as mbox
from datetime import date
import os

class Usuario():
    def __init__(self,nombreUser,clave,tipo = None):
        self.__nombreUser = nombreUser
        self.__clave = clave
        self.__tipo = tipo
    def registrar_user(self):
            con = sql.connect('Supermark.db',timeout = 10)
            cur = con.cursor()
            cur.execute(f"select * from Clientes where correo = '{self.__nombreUser}' ")
            usuario = cur.fetchone()
            con.close()
            if usuario != None:
                print("ya existe el usuario")
            else:
                con = sql.connect('Supermark.db',timeout = 10)
                cur = con.cursor()
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
            con = sql.connect('Supermark.db')
            cur = con.cursor()
            cur.execute(f"select * from Clientes where correo = '{self.__correo}' ")
            usuario = cur.fetchone()
            con.close()
            if usuario != None:
                mbox.showwarning("error","ya existe el usuario")
            else:
                con = sql.connect('Supermark.db',timeout = 10)
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
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute(f"select * from productos where nombre = '{self.__nombre}' ")
        prod = cur.fetchone()
        con.close()
        if prod != None:
            mbox.showwarning("error","ya existe el producto que se desea cargar")
        else:
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
        cur.execute(f"UPDATE productos SET descripcion = '{descripcion}' where nombre = '{self.__nombre}'")
        con.commit()
        con.close()
    def cambiar_nombre(self,nombre):
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute(f"UPDATE productos SET nombre = '{nombre}' where nombre = '{self.__nombre}'")
        con.commit()
        con.close()
    def cambiar_precio(self,precio):
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute(f"UPDATE productos SET precio = {precio} where nombre = '{self.__nombre}'")
        con.commit()
        con.close()
    def quitar_prod(self,nombre):
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute(f"delete from productos where nombre = '{nombre}'")
        con.commit()
        con.close()
class ProductoCarrito():
    def __init__(self, Producto, cantidad,precio):
        self.__Producto = Producto
        self.__cantidad = cantidad
        self.__precio = precio
        self.__carrito = [[self.__Producto,self.__precio,self.__cantidad]]
    def agregar(self,prod,cantidad,precio):
            a = 0
            for i in self.__carrito:
                if i[0] == prod:
                    print("entro")
                    print(a)
                    self.__carrito[a]=([prod,precio,cantidad])
                    return a
                a+=1
            self.__carrito.append([prod,precio,cantidad])
            return len(self.__carrito)+1
    def tamlista(self):
        return len(self.__carrito)
    def lista(self):
        return self.__carrito
    def quitar_carrito(self,posicion):
        self.__carrito.pop(posicion)
    def total(self):
        total = 0
        archivo = open("id_cliente.txt","r")
        id_cliente = archivo.readlines()
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute("INSERT INTO venta(id_cliente,fecha) VALUES (?,?)",(id_cliente[0],date.today()))
        con.commit()
        cur.execute(f"select * from venta where id_cliente = '{id_cliente[0]}' ")
        id_venta = cur.lastrowid
        print(id_venta)
        con.close()
        prod_id = ""
        cantidad = ""
        for i in self.__carrito:
            if i[0] != "producto":
                print(i[0])
                print(i[2])
                con = sql.connect('Supermark.db')
                cur = con.cursor()
                cur.execute(f"select * from productos where nombre = '{i[0]}' ")
                prod = cur.fetchone()
                resto = int(prod[3]) - int(i[2])
                cur.execute(f"UPDATE productos SET stock = {resto} where nombre = '{i[0]}'")
                con.commit()
                con.close()
                prod_id += str(prod[0]) + " "
                cantidad += str(i[2]) + " "
                total += float(i[1])*float(i[2])
        con = sql.connect('Supermark.db')
        cur = con.cursor()
        cur.execute("INSERT OR REPLACE INTO detalle_venta VALUES (?,?,?)",(id_venta,prod_id,cantidad))
        con.commit()
        con.close()
        return total
if __name__ == "__main__":
    '''reg = RegistroDatos()
    cliente1 = reg.RegistrarCliente()
    user1 = reg.RegistrarUsuario()
    cliente1.registrar_cliente()
    user1.registrar_user()
    print(cliente1)
    print(user1)'''
    cl.mostrar_productos()
    print(pr)

