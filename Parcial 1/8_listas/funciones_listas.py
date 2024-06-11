
paises=['Mexico', 'USA', 'Brasil', 'Japon']
numeros=[23,34,12.56,0.100]
texto=['HOLA', True, 23, 3.141516]

#Ordenar una lista

print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

#Añadir elementos
print(texto)
texto.insert(len(texto), 'True')
print(texto)
texto.insert(len(texto), True)
print(texto)
texto.append(False)
print(texto)

#Eliminar elementos 
print(numeros)
numeros.remove(23)
print(numeros)
numeros.pop(0)
print(numeros)

#Dar la vuelta a una lista
print(numeros)
numeros.reverse()
print(numeros)

#Buscar un dato dentro de una lista
print('Brasil' in paises)


numeros=[23,34,12.56,0.100,23]
#Cuantas veces aparece un valor dentro de una lista
print(numeros)
numeros.append(23)
cuantos = numeros.count(23)
print(f'En la variable numeros se encontro el numero 23 {cuantos} veces')

#Unir listas
print(paises)
paises.extend(numeros)
print(paises)
