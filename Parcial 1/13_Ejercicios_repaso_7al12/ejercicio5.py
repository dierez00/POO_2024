#Crear una lista y un diccionario con el contenido de esta tabla: 

#ACCION              TERROR        DEPORTES
#MAXIMA VELOCIDAD    LA MONJA       ESPN
#ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#RAPIDO Y FURIOSO I  LA MALDICION   ACCION


#imprimir la información

def lista():
    tabla_lista = [
    ["ACCION", "TERROR", "DEPORTES"],
    ["MAXIMA VELOCIDAD", "LA MONJA", "ESPN"],
    ["ARMA MORTAL 4", "EL CONJURO", "MAS DEPORTE"],
    ["RAPIDO Y FURIOSO I", "LA MALDICION", "ACCION"]]


    print("Contenido de la lista:")
    for fila in tabla_lista:
        print(fila)


def diccionario():
    tabla_diccionario = {
        "ACCION": ["MAXIMA VELOCIDAD", "ARMA MORTAL 4", "RAPIDO Y FURIOSO I"],
        "TERROR": ["LA MONJA", "EL CONJURO", "LA MALDICION"],
        "DEPORTES": ["ESPN", "MAS DEPORTE", "ACCION"]
    }

    print("Contenido del diccionario:")
    for i, o in tabla_diccionario.items():
        print(f"{i}: {', '.join(o)}")

diccionario()