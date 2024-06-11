"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
   1.- Funcion que no recibe parametros y no regresa valor
   2.- Funcion que no recibe parametros y regresa valor
   3.- Funcion que recibe parametros y no regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

#Ejemplo 1 Crear una funcion para imprimir nombres de personas
#    1.- Funcion que no recibe parametros y no regresa valor 
def solicitarNombres():
   nombre=input("Ingresa el nombre completo: ")

solicitarNombres()  

#Ejemplo 2 sumar dos numeros
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

suma()    

#Ejemplo 3 sumar dos numeros 
#2.- Funcion que no recibe parametros y regresa valor
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma

resultado_suma=suma()
print(f"La suma es: {resultado_suma}")

#Ejemplo 4 sumar dos numeros 
# 3.- Funcion que recibe parametros y no regresa valor
def suma(num1,num2):
    suma=num1+num2
    print(f"La suma es: {suma}")

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
suma(n1,n2)

#Ejemplo 5 sumar dos numeros 
# 4.- Funcion que recibe parametros y regresa valor
def suma(num1,num2):
    suma=num1+num2
    return suma

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
resultado_suma=suma(n1,n2)
print(f"La suma es: {resultado_suma}")

#Ejemplo 6 Crear un programa que solicite a traves de una funcion la siguiente informacion: Nombre del Paciente, Edad, Estatura, Tipo de Sangre. Utilizar los 4 tipos de funciones

def consulta_1():
    nombre = input('Escribe el nombre del paciente: ')
    edad = int(input('Digita la edad del paciente: '))
    estatura = float(input('Digita la estatura del paciente: '))
    tipo_sangre = input('Escribe el tipo de sangre del paciente: ')
    
consulta_1()

def consulta_2(nombre, edad, estatura, tipo_sangre):
    print(f'{nombre}\n{edad}\n{estatura}\n{tipo_sangre}')

consulta_2('Diego', 19, 1.73, 'o+')

def consulta_3(nombre, edad, estatura, tipo_sangre):
    paciente = {nombre, edad, estatura, tipo_sangre}
    return paciente

consulta_3('Diego', 19, 1.73, 'o+')

def consulta_4():
    nombre = input('Escribe el nombre del paciente: ')
    edad = int(input('Digita la edad del paciente: '))
    estatura = float(input('Digita la estatura del paciente: '))
    tipo_sangre = input('Escribe el tipo de sangre del paciente: ')
    print(f'{nombre}\n{edad}\n{estatura}\n{tipo_sangre}')
    
consulta_4()