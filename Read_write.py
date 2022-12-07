import sqlite3

conexion = sqlite3.connect('Supermark.db')
cursor = conexion.cursor()
#cursor.execute("INSERT INTO Clientes(apellido,nombre,dni,correo,domicilio) VALUES (?,?,?,?,?)",("Jacinto","Pablo",4103452, "ab c@hot mail.com ".replace(" ",""),"caseros 349"))

correo = input("ingresar correo ")
cursor.execute(f"select * from Clientes where correo = '{correo}'")

usuario = cursor.fetchone()

if usuario != None:
    print("ya existe el usuario")
else:
    print("no existe este correo")
    '''
usuarios = cursor.fetchall()
c = 0
for usuario in usuarios:
        print("cliente: ", usuario)
        if usuario[4].lower() == "abc@hotmail.com":
            print(usuario[4].lower())
            c += 1
            print(c)

if(c == 1):
    print("fallo")
else:
    print("ya existe ese correo")'''

conexion.close()

