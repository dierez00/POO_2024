""" 
    Existe una estructura de condicion llamada "if" la cual evalua una condicion para encontrar el valor "True" o se cumple la 
    condicion se ejecuta la linea o lineas codigo 
    
    Tenemos 4 variantes del if
    1.- if simple
    2.- if compuesto
    3.- if anidado
    4.- if y el elif
"""

#Ejemplo 1 - if simple

color="rojo"

if color=="rojo":
    print("El color es rojo")

#Ejemplo 2 - if compuesto

color="rojo"

if color=="rojo":
    print("El color es rojo")

else:
    print("El color no es rojo")
    
#Ejemplo 3 - if anidado

color="rojo"

if color=="rojo":
    print("El color es rojo")
    if color!="rojo":
        print("Es un color diferente al rojo")
        
#Ejemplo 4 - if y elif

color="rojo"

if color=="rojo":
    print("El color es rojo")

elif color=="negro":
    print("El color es negro")