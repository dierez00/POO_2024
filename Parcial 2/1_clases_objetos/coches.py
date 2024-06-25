#Clases: es como un molde a traves del cual se puede instanciar un objeto. Dentro de las clases se 
#definen atributos (propiedades/características) y los métodos (funciones o acciones)
#Objetos o instancias: son parte de una clase, los objetos o instancias pertenecen a una clase
#es decir interactuan con la clase o clases y hacer uso de los atributos y métodos es necesario
#crear un objeto u objetos

class Coches:
    
    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #Valores iniciales es posible declarar al principio de una clase
    marca = 'Ferrari'
    color = 'rojo'
    model = '2010'
    velocidad = 300
    caballaje = 500
    plazas = 2
    
    #Metodos o acciones o funciones que hace el objeto
    
    def acelerar(self):
        self.velocidad+=1
    
    def frenar(self):
        self.velocidad-=1

#Fin definir clase

#Crear un objeto o instanciar la clase

coche1= Coches()

#Mostrar los valores iniciales del objeto o instancia de la clase

print(f'Marca: {coche1.marca} {coche1.color}, numeros de plazas: {coche1.plazas} \nModelo: {coche1.modelo} con una velocidad de {coche1.velocidad} Km/h y un potencia de {coche1.caballaje} hp')

#Acelerar la velocidad del coche de 300 a 301
coche1.acelerar()
print(f"La nueva velocidad es: {coche1.velocidad}")

#Disminuir la velocidad del coche de 301 a 100

for i in range(1,202):
   coche1.frenar()

print(f"La nueva velocidad del coche es: {coche1.velocidad}")

coche2=Coches()
coche2.marca='Porsche'
coche2.color='Amarillo'
coche2.model='2024'
coche2.velocidad = 700
coche2.caballaje = 1000
coche2.plazas = 1

print(f'Marca: {coche2.marca} {coche2.color}, numeros de plazas: {coche2.plazas} \nModelo: {coche2.modelo} con una velocidad de {coche2.velocidad} Km/h y un potencia de {coche2.caballaje} hp')
