print("=====Captura de calificaciones=====")

nombres = []
carreras = []
calificaciones_parciales = []
calificaciones_proyectos = []
promedios_finales = []

while True:
    suma = 0.0
    nombre_alumno = input('Dime el nombre del alumno: ')
    nombres.append(nombre_alumno)
    
    carrera = input('¿A qué carrera pertenece? ')
    carreras.append(carrera)
    
    parciales = []
    for i in range(1, 4):
        calificacion = float(input(f'Dime la {i}ª calificación: '))
        parciales.append(calificacion)
        suma += calificacion
    
    promedio_parciales = suma / 3
    calificaciones_parciales.append(promedio_parciales)
    
    calificacion_proyecto_final = float(input('Digita la calificación final del proyecto: '))
    calificaciones_proyectos.append(calificacion_proyecto_final)
    
    promedio_final = (promedio_parciales + calificacion_proyecto_final) / 2
    promedios_finales.append(promedio_final)
    
    captura = input('¿Deseas realizar otra captura? (SI/NO): ')
    if captura.upper() == 'NO':
        suma_promedios_finales = 0.0
        for idx in range(len(nombres)):
            print('\t======Alumnos=====')
            print(f'Alumno: {nombres[idx]}\nCarrera: {carreras[idx]}\nPromedio Parciales: {calificaciones_parciales[idx]:.2f}\n'
                  f'Calificación Final Proyecto: {calificaciones_proyectos[idx]:.2f}\nPromedio Final: {promedios_finales[idx]:.2f}')
            
            if promedios_finales[idx] < 80 or calificaciones_proyectos[idx] > 50:
                print("\t***El alumno presentará examen extraordinario.***")
            
            suma_promedios_finales += promedios_finales[idx]

        promedio_general = suma_promedios_finales / len(nombres)
        print('\t=====PROMEDIO GENERAL=====')
        print(f'Promedio final de todos los alumnos capturados: {promedio_general:.2f}')

        print("Captura finalizada.")
        break


