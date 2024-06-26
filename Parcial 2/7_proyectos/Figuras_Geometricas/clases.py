import math

class Figuras:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible
        
    def estaVisible(self, visible):
        return self.visible
    
    def mostrar(self,visible):
        self.visible = True
        
    def ocultar(self,visible):
        self.visible = False
        
    def mover(self, x, y):
        self.x = int(input("Digita x:"))
        self.y = int(input("Digita y:"))
        return self.x and self.y
    
    def calcularArea(self):
        return self
        
    def getX(self):
        return self.x
    def setX(self,x):
        self.x = x
        
    def getY(self):
        return self.y
    def sety(self,y):
        self.y = y
    
    def getVisible(self):
        return self.visible
    def setVisible(self,visible):
        self.visible = visible
        
class Rectangulos(Figuras):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.alto = alto
        self.ancho = ancho
        
    def getLargo(self):
        return self.largo
    
    def setLargo(self,largo):
        self.largo=largo
        
    def getAncho(self):
        return self.ancho
    
    def setAncho(self,ancho):
        self.ancho=ancho    
        
    def ocultar(self, visible):
        return super().ocultar(visible)
    
    def mostrar(self, visible):
        return super().mostrar(visible)
    
    def calcularArea(self, alto, ancho):
        global area 
        area = self.alto * self.ancho
    
    def getInfo(self):
        print(f"X={self.getX()}\nY={self.getY()}\nVisible = {self.getVisible()}\nAlto = {self.getAlto()}\nAncho = {self.getAncho()}")
    
class Circulos(Figuras):
    def __init__(self, x, y, visible, radio):
        super().__init__( x, y, visible)
        self.radio = radio
        
    def mostrar(self, visible):
        return super().mostrar(visible)
    
    def ocultar(self, visible):
        return super().ocultar(visible)
    
    def calcularArea(self, radio):
        return (self.radio**2)*math.pi
    
    def getRadio(self):
        return self.radio
    
    def setRadio(self,radio):
        self.radio=radio
        
    def getInfo(self):
        print(f"X={self.getX()}\nY={self.getY()}\nVisible = {self.getVisible()}\nRadio = {self.getRadio()}")
    