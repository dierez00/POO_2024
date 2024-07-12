import mysql.connector

try:
    #conectar con la BD en la MySQL
    conexion = mysql.connector.connect(
        host = 'localhot',
        user = 'root',
        password = '',
        database = 'bd_python'
    )
    
    #verificar si la conexion fue exitosa
    if conexion.is_connected():
        print("Se creo la conexion con la base de datos exitosamente")
        
    else: 
        print("No fue posible conectar con la base de datos, verifique")

except Exception as e:
    print(f'Error :{type(e)}')
    print(f'Tipo de exepcion: {type(e).__name__}')
    print(f"Ocurrio un error con el servidor, verifique")

