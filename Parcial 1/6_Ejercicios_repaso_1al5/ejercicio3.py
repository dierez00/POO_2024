# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

i=1
o=1

print("For:")

for i in range(0,61,1):
    print(f'{i}^2={i*i}')

print('\n\nWhile:')

while o<=60: 
    print(f'{o}^2={o*o}')
    o+=1