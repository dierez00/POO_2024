from coneccionBD import * 

try:
    micursor = conexion.cursor()

    sql = "delete from clientes where id=6"

    micursor.execute(sql)
    conexion.commit()
    
except:
    print(f"Ocurrio un error, verifique")

else:
    print("hecho")
