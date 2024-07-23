class Persona():
    def __init__(self, nombre, apellido, edad, locacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.locacion = locacion

    def description(self):
        print('Nombre:', self.nombre, '\nApellido:', self.apellido, '\nEdad:', self.edad, '\nLocacion:', self.locacion)


class Employee(Persona):
    def __init__(self, nombre, apellido, edad, locacion, salario=0, antiguedad=0):
        super().__init__(nombre, apellido, edad, locacion)
        self.salario = salario
        self.antiguedad = antiguedad
    
    def description(self):
        super().description()
        print('Salario:', self.salario, '\nAntiguedad:', self.antiguedad)
        


Peggy=Employee('peggy','miranda',4,'grecia',1500,3)

Peggy.description()
