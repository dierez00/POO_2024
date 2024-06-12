#Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

lista = []
cadena = 'd'
entero = int(3)
logico = True

def tipo_de_dato(variable):
    if type(variable) == list:
       print('El tipo de variable es lista')
    elif  type(variable) == str:
        print('El tipo de variable es una cadena')
    elif  type(variable) == int:
        print('El tipo de variable es entero')
    elif  type(variable) == bool:
        print('El tipo de variable es logico')
        
tipo_de_dato(lista)