import os

peliculas=["Sirenita","Rey leon","Titanic","Matrix","Spiderman"]

def esperaTecla():
        print("Presione cualquier tecla para continuar")
        input()
        os.system("cls")

def insertarPelicula():
    pelicula=input("Ingrese el nombre de la pelicula a agregar: ")
    peliculas.append(pelicula)
    print(f"La pelicula {pelicula} ha sido ingresada en el sistema")
    esperaTecla()

def removerPelicula():
    bucle=True
    while bucle:
        pelicula=input("Ingrese el nombre de la pelicula a eliminar: ")
        if pelicula in peliculas:
            peliculas.remove(pelicula)
            print(f"La pelicula {pelicula} ha sido eliminada correctamente")
            esperaTecla()
            bucle=False
        else:
            print(f"La pelicula {pelicula} no se encuentra en el sistema")
            esperaTecla()
            continuar = input("Desea intentar de nuevo? SI/NO ").upper()
            if continuar in ["SI", "S"]:
                bucle=True
            else:
                bucle=False
                os.system("cls")


def actualizarLista():
    print("Las peliculas en stock son: ")
    print(peliculas)
    esperaTecla()
    
def consultarPelicula():
    pelicula = input("Dame la película a buscar: ")
    noencontre = True  # Inicializar como True

    for i in range(len(peliculas)):
        if pelicula == peliculas[i]:
            print(f"La película '{peliculas[i]}' sí está disponible")
            continuar = input("Desea eliminar esta pelicula? SI/NO ").upper()
            if continuar in ["SI", "S"]:
                peliculas.remove(pelicula)
                esperaTecla()
            noencontre = False
            break  # Terminar el bucle cuando se encuentra la película

    if noencontre:
        print(f"No se encuentra la película {pelicula}")
    esperaTecla()
    
def buscarLista():
    pelicula = input("Ingresa el nombre de la pelicula a buscar: ")
    if pelicula in peliculas:
        print('La pelicula no se encuentra.')
    esperaTecla()

def vaciarLista():
    peliculas.clear()
    
def menu():
     print("\n1.- Agregar pelicula\n2.- Eliminar pelicula\n3.- Actualizar\n4.- Consultar\n5.- Buscar\n6.- Vaciar\n7.- SALIR ")
     opcion = int(input("\tIngresa una opcion: "))
     return opcion

opcion = menu()

while opcion != 7:
    if opcion == 1:
        pelicula = input("\nIngresa el nombre de la pelicula: \n")
        insertarPelicula()
    elif opcion == 2:
        pelicula = input("\nIngresa el nombre de la pelicula: \n")
        removerPelicula()
    elif opcion == 3:
        pelicula = input("\nIngresa el nombre de la pelicula: \n")
        actualizarLista()
    elif opcion == 4:
        pelicula = input("\nIngresa el nombre de la pelicula: \n")
        consultarPelicula()
    elif opcion == 5:
        pelicula = input("\nIngresa el nombre de la pelicula: \n")
        buscarLista()
    elif opcion == 6:
        pelicula = input("\nIngresa el nombre de la pelicula: \n")
        vaciarLista()
    opcion = menu()
