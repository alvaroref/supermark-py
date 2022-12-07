import sqlite3

#Alumnos: Perez Natael, Gomez Alvaro, Tolaba Damian

con = sqlite3.connect("supermark.db")

cur = con.cursor()

cur.execute("CREATE TABLE productos(id_producto INTEGER PRIMARY KEY AUTOINCREMENT,descripcion TEXT(255) NOT NULL, precio NUMERIC NOT NULL, stock INTEGER NOT NULL, nombre TEXT(25) NOT NULL)")

cur.execute("CREATE TABLE Clientes (id_cliente INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,apellido TEXT(25) NOT NULL,nombre TEXT(25) NOT NULL,dni INTEGER NOT NULL,correo TEXT(50) NOT NULL,domicilio TEXT(50) NOT NULL)")

cur.execute("CREATE TABLE usuarios(nombreusuario TEXT(50) NOT NULL,clave TEXT(18) NOT NULL)")

cur.execute("CREATE TABLE venta(id_venta INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,id_cliente INTEGER NOT NULL,fecha NUMERIC NOT NULL,FOREIGN KEY(id_cliente) REFERENCES Clientes(id_cliente))")

cur.execute("CREATE TABLE detalle_venta(id_venta TEXT(25) PRIMARY KEY NOT NULL,id_producto INTEGER NOT NULL,cantidad NUMERIC NOT NULL,FOREIGN KEY(id_venta) REFERENCES venta(id_venta),FOREIGN KEY(id_producto) REFERENCES producots(id_producto))")

con.close()

