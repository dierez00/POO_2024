import math


def solicitarDatos():
   print("\n")
   global n1,n2,ope
   if opcion=='6' or opcion=='5':
      n1=int(input("Numero: "))
      n2=0
   else:
      n1=int(input("Numero #1: "))
      n2=int(input("Numero #2: "))
         
   
  

def getCalculadora(num1,num2,operacion):
    if operacion=="1" or operacion=="+" or operacion=="SUMA":
       return f"{num1}+{num2}={int(num1)+int(num2)}"
    elif operacion=="2" or operacion=="-" or operacion=="RESTA":
       return f"{num1}-{num2}={int(num1)-int(num2)}"  
    elif operacion=="3" or operacion=="*" or operacion=="MULTIPLICACION":
       return f"{num1}*{num2}={int(num1)*int(num2)}"        
    elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
       return f"{num1}/{num2}={int(num1)/int(num2)}"
    elif operacion=="5"or operacion=="^" or operacion=="POTENCIA":
       return f'{num1}x{num1}={int(num1*num1)}'  
    elif operacion=='6' or operacion=='RAIZ':
       return f'{math.sqrt(int(num1))}'
    else:
        return f'Opcion no valida'


opcion = True
while opcion:
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- Potencia \n 6.- Raiz \n 7. Salir")
    opcion=input("\t Elige una opción: ").upper()

    if opcion != '7':
        solicitarDatos()
        print(getCalculadora(n1,n2,opcion))
    else:
        opcion=False
        print('SALIENDO')