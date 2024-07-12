from coneccionBD import * 

try:
    micursor = conexion.cursor()

    sql = "select * from clientes"

    micursor.execute(sql)

    #Crear un objeto para enviar el resultado de la ejecucion del execute para posteriormente mostrar con ciclo
    resultado = micursor.fetchall()
    
except:
    print(f"Ocurrio un error, verifique")

else:
    for x  in resultado:
        print(x)