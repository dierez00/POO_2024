#Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#el contenido de la lista en mayusculas

lista = []

if len(lista) == 0:
    opcion = True
    while opcion:
        elemento = str(input('Ingrese un valor: '))
        lista.append(elemento.upper())
        respuesta = str(input('Deseas añadir mas valores a la lista(SI/NO): '))
        if respuesta.upper() == "NO":
            opcion = False
            print(lista)   