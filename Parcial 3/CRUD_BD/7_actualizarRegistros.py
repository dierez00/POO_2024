from coneccionBD import * 

try:
    micursor = conexion.cursor()

    sql = "update clientes set direccion='Col. Nueva Vizcaya' where id = 7"

    micursor.execute(sql)
    conexion.commit()
    
except:
    print(f"Ocurrio un error, verifique")

else:
    print("hecho")