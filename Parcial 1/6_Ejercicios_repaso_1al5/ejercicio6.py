#Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10

i=0
o=0

for i in range(0,11,1):
    print(f'====Tabla del {i}====')
    for o in range(0,11,1):
        print(f'{i}x{o}={i*o}')