import mysql.connector

try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = ''
    )

        
except:
    print(f"Ocurrio un error con el sistema, verifique")
    
else:
    #Crear un objeto de tipo cursor que permita ejecutar instrucciones sql
    micursor = conexion.cursor()

    sql = "create database bd_python"
    #Ejecutar la consulta
    micursor.execute(sql)

    print('Se creo la base de datoss')
        
    #Mostrar las BD que existen en el SGBD MySQL

    micursor.execute("show databases")

    for x in micursor:
        print(x)