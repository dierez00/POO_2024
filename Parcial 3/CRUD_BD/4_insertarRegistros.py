from coneccionBD import * 

try:
    micursor = conexion.cursor()

    sql = "insert into clientes(id, nombre, direccion, tel) values(null,'Daniel Contreras', 'Col centro', '6181234567');"

    micursor.execute(sql)

    conexion.commit()

except:
    print("Ocurrio un error, verifique")

else:
    print(f"Registro hecho")