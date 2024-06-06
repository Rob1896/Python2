"""En Python, las herencias se refieren a la capacidad de una clase de heredar atributos y métodos de otra clase. 
Esto permite la reutilización de código y la creación de una jerarquía de clases 
donde las clases hijas pueden extender o modificar el comportamiento de las clases padre."""


class Vehiculos(): # clase padre
    def __init__(self, marca, model):
        self.marca = marca
        self.model = model
        self.enMarcha = False
        self.acelera = False
        self.frenar = False

    # metodos  
    def arrancar(self):
        self.enMarcha = True
        return f'Arrancado: {self.enMarcha}'
        
    def acelerar(self):
        self.acelera = True
        return f'Acelerando: {self.acelera}'
    
    def frenando(self):
        self.frenar = True
        return f'Frenando: {self.frenar}'
        
    def state(self):
        print("Marca: ", self.marca, "\nModelo: ", self.model, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
        
    
    
class Moto(Vehiculos):  # se crea la clase "hija"

    def velocidad(self): #se crea instancia propia de la clase "hija"
        print("La velocidad de la moto es de 150km/h")

    def ruedas(self):
        print("La moto tiene 2 ruedas")

miMoto = Moto('honda', 'CBR') #se le pasan los parametros que pidde la clase padre

miMoto.velocidad() # se prueba el metdo propia de la clase
miMoto.ruedas()

print(miMoto.arrancar()) # se prueban los metodos proprios da la clase padre

print(miMoto.acelerar())# se prueban los metodos proprios da la clase padre

print(miMoto.frenando())# se prueban los metodos proprios da la clase padre


class Camion(Vehiculos):

    def velocidad(self): #se crea instancia propia de la clase "hija"
        print("La velocidad del camion es de 200km/h")

    def ruedas(self):
        print("El camion tiene 6 ruedas")

miCamion = Camion('volvo', 'volo1')

miCamion.velocidad() # se prueba el metdo propia de la clase

print(miCamion.acelerar())

    







    
        
