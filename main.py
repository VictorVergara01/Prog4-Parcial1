import mysql.connector

conexion = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="", 
    database="inventario"
    )

def crear_tablas():
    cursor = conexion.cursor()
    return cursor.execute("CREATE TABLE IF NOT EXISTS articulos (codigo INT AUTO_INCREMENT PRIMARY KEY, articulo VARCHAR(50), precio FLOAT )")

def principal():
    
    crear_tablas()
    
    menu="""
    == Menu Principal ==\n
    a) Registrar
    b) Buscar
    c) Editar
    d) Eliminar
    e) Lista de articulos
    f) salir
    Elige: """
    eleccion = ""
    
    while eleccion != "f":
        
        eleccion = input(menu)
        
        if eleccion == "a":
            articulo = input("Ingrese nombre del articulo: ")
            posible_articulo = buscar_articulo(articulo)
            if posible_articulo:
                print(f"El articulo '{articulo}' ya existe")
            else:
                precio = input("Ingresa el precio: ")
                agregar_articulo(articulo, precio)
                print("Articulo agregado")
        
        if eleccion == "b":
            articulo = input("Ingrese el nombre del articulo que quiere buscar: ")
            busqueda_registro = buscar_articulo(articulo)
            if busqueda_registro:
                print(f"El articulo '{articulo}' \n precio: {precio[0]}")
            else:
                print(f"Articulo '{articulo}' no encontrado")
        
        if eleccion == "c":
            articulo = input("Ingresa el nombre del articulo que quieres editar: ")
            nuevo_precio = input("Ingrese nuevo precio del articulo: ")
            editar_articulo(articulo, nuevo_precio)
            print("Articulo actualizado")
     
        if eleccion == "d":
            articulo = input("Ingrese articulo a eliminar: ")
            eliminar_articulo(articulo)

        if eleccion == "e":
            articulos = obtener_articulos()
            print("=== Lista de articulos ===")
            for x in articulos:
                print(x)

#--------------------------------------------------------------------------------------------#

def buscar_articulo(articulo):
    cursor = conexion.cursor()
    consulta = "SELECT precio FROM articulos WHERE articulo = %s"
    cursor.execute(consulta, [articulo])
    return cursor.fetchone()

#---------------------------------------------------------------------------------------------#

def agregar_articulo(articulo, precio):
    cursor = conexion.cursor()
    sentencia = "INSERT INTO articulos (articulo, precio) VALUES (%s, %s)"
    cursor.execute(sentencia, [articulo, precio])
    conexion.commit()

#---------------------------------------------------------------------------------------------#
     
def editar_articulo(articulo, nuevo_precio):
    cursor = conexion.cursor()
    sentencia = "UPDATE articulos SET precio = %s WHERE articulo = %s"
    cursor.execute(sentencia, [nuevo_precio, articulo])
    conexion.commit()

#---------------------------------------------------------------------------------------------#

def eliminar_articulo(articulo):
    cursor = conexion.cursor()
    sentencia = "DELETE FROM articulos WHERE articulo = %s"
    cursor.execute(sentencia, [articulo])
    conexion.commit()  

#---------------------------------------------------------------------------------------------#

def obtener_articulos():
    cursor = conexion.cursor()
    consulta = "SELECT codigo, articulo, precio FROM articulos"
    cursor.execute(consulta)
    return cursor.fetchall()

 
#---------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    principal()