#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?

x = float(input('Cual es el numero del que deseas sacar x porcentaje?'))
porcentaje = float(input('Cual es el porcentaje que deseas saber?'))

total = (x/100)*porcentaje

print(f'El {porcentaje} por ciento de {x} es: {total}')