#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

a = int(input('Digita el primer numero: '))
b = int(input('Digita el segundo numero: '))

i=0

for i in range(a , b , 2):
    print(i)
    i+=1