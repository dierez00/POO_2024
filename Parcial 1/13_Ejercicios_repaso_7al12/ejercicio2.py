#2.- 
#Escribir un programa  que añada valores a una lista mientras que su longitud 
#sea menor a 120, y luego mostrar la lista: Usar un while y for

lista = []

while len(lista)<5:
    valor = input('Coloca el valor a añadir a la lista: ')
    lista.append(valor)

for i in lista:
    print(f'Elementos de la lista: {i}')
        

