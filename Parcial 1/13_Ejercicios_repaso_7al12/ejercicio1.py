#Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

 #a.- Recorrer la lista y mostrarla
 #b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 #c.- ordenarla y mostrarla
 #d.- mostrar su longitud
 #e.- buscar algun elemento que el usuario pida por teclado
 

numeros = [5,7,8,9,4,5,6,1]

def recorrer():
        print(str(numeros))
        
sorted(numeros)

print(len(numeros))

buscar = int(input('Digita el numero a buscar: '))

for i in numeros:
    if i == buscar:
        print('Si esta.')
        break