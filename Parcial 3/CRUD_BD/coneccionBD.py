import mysql.connector

#conectar con la BD en la MySQL
try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'bd_python'
    )
except:
    print(f'Ocurrio un error, verifique')

#verificar si la conexion fue exitosa
#if conexion.is_connected():
 #   print("Se creo la conexion con la base de datos exitosamente")
    
#else: 
#    print("No fue posible conectar con la base de datos, verifique")