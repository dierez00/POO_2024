#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

aprobaron = 0
reprobaron = 0
i = 1

for i in range(1,16,1):
    calificacion=float(input(f'Dime la calificacion del {i} alumno: '))
    if calificacion >= 80:
        aprobaron+=1
    else:
        reprobaron+=1
        
print(f'{aprobaron} Alumnos pasaron y {reprobaron} Alumnos reprobaron')