from coches import *
#Crear un objetos o instanciar la clase

print("Objeto 1")
coche1=Coches("Blanco","VW","2022",220,150,5)
#coche1.getInfo()


#print("Objeto 2")
#coche2=Coches("Azul","Nissan","2020",180,150,5)
#coche2.getInfo()

#print("Objeto 3")
#coche3=Coches("Azul","Audi","2025",240,300,6)
#coche3.getInfo()
#coche3.setColor("Azul Metalico")
#coche3.getInfo()

print(coche1.getPrivateAtribute())
coche1.getMetodoPublico()

camion1=Camiones("Negro","Dina","2020",180,300,12,8,2500)
camion1.getInfo()

camion2=Camiones("Azul","Dina","2020",180,300,12,8,2500)
camion2.getInfo()

camioneta1=Camionetas("Roja","Skibidi","2025",240,250,8,"delantera",True)
camioneta1.getInfo()

camioneta2=Camionetas("Verde","Toilet","2025",240,250,8,"delantera",True)
camioneta2.getInfo()