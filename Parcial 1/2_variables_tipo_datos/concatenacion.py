#Formas de concatenacion en python

nombre = "Diego Antunez"
especialidad = "Area de software multiplataforma"
carrera = "Ingenieria en Gestion y Desarrollo de Software"

#1er forma
print("Mi nombre es "+nombre+ " estoy en la especialidad de "+especialidad+ " en la carrera de  "+carrera)

print("\n")

#2da forma
print("Mi nombre es ",nombre, " estoy en la especialidad de ",especialidad, " en la carrera de  ",carrera)

print("\n")

#3er forma
print(f"Mi nombre es ,{nombre},  estoy en la especialidad de ,{especialidad},  en la carrera de  ,{carrera}")

print("\n")

#4ta forma
print("Mi nombre es ,{},  estoy en la especialidad de ,{},  en la carrera de  ,{}" .format(nombre, especialidad, carrera))

print("\n")

#5ta forma
print('Mi nombre es '+nombre+ ' estoy en la especialidad de '+especialidad+ ' en la carrera de  '+carrera)

