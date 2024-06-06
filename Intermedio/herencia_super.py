'''Se utiliza para llamar métodos de una clase base (superclase) desde una clase derivada (subclase).'''
'''¿Qué hace super()?

	1.	Acceso a Métodos y Propiedades de la Superclase: Permite acceder a métodos y propiedades de la superclase desde la subclase.
	2.	Evita la Duplicación de Código: Permite reutilizar el código de la superclase, evitando la duplicación.
	3.	Soporta Múltiple Herencia: Gestiona correctamente la herencia múltiple, lo cual puede ser complicado de manejar manualmente.'''




class Persona(): #clase padre
    def __init__(self, nombre, apellido, edad, locacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.locacion = locacion

    def description(self):
        print('Nombre:', self.nombre, '\nApellido:', self.apellido, '\nEdad:', self.edad, '\nLocacion:', self.locacion)


class Employee(Persona):
    def __init__(self, nombre, apellido, edad, locacion, salario=0, antiguedad=0):
        super().__init__(nombre, apellido, edad, locacion) # con esto heredo de la clase padre "Persona"
        self.salario = salario
        self.antiguedad = antiguedad
    
    def description(self):
        super().description() # se ejecuta el drescription de la clase padre
        print('Salario:', self.salario, '\nAntiguedad:', self.antiguedad) # despues se ejecuta el print
        


Peggy=Employee('peggy','miranda',4,'grecia',1500,3)

Peggy.description()



#ejemplo2

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        return "Algun sonido"

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llamada al constructor de la superclase
        self.raza = raza

    def hacer_sonido(self):
        return "Guau"

# Crear una instancia de Perro
mi_perro = Perro("Fido", "Labrador")

# Acceder a atributos y métodos
print(mi_perro.nombre)    # Imprime "Fido"
print(mi_perro.raza)      # Imprime "Labrador"
print(mi_perro.hacer_sonido())  # Imprime "Guau"


#ejemplo 3 herencia multiple 

class A:
    def __init__(self):
        print("Inicializando A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Inicializando B")

class C(A):
    def __init__(self):
        super().__init__()
        print("Inicializando C")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("Inicializando D")

# Crear una instancia de D
d = D()



#ejemplo4

'''En este ejemplo, Gerente extiende la funcionalidad del método mostrar_informacion de Empleado utilizando super() 
para obtener la información básica y agregar información adicional específica del Gerente.'''

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_informacion(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_informacion(self):
        info_basica = super().mostrar_informacion()
        return f"{info_basica}, Departamento: {self.departamento}"

# Crear una instancia de Gerente
mi_gerente = Gerente("Alice", 75000, "Ventas")

# Mostrar información del gerente
print(mi_gerente.mostrar_informacion())
# Imprime "Empleado: Alice, Salario: 75000, Departamento: Ventas"

