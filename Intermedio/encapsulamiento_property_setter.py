'''El encapsulamiento en Python es un principio fundamental de la programación orientada a objetos (OOP) 
que se utiliza para restringir el acceso directo a algunos de los componentes de un objeto 
puede prevenir la modificación accidental de datos. Se implementa principalmente utilizando atributos y métodos privados.'''


#En Python, los atributos y métodos se pueden hacer privados utilizando un guion bajo () o doble guion bajo (_) al principio de sus nombres:

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
        
    
persona = Persona('Peggy', 'Miranda',5) #estos valores si pueden ser cambiados

print(persona.nombre) 
persona.apellido = 'Mercado' # aqui modifique el valor inicial que era Miranda a Mercado
print(persona.apellido)




'''En Python, los atributos y métodos se pueden hacer privados utilizando un guion bajo () o doble guion bajo (_) al principio de sus nombres:
como evitar que suceda:
los _ solo sirven como generalidad, no quiere decir que NO se puede modificar, si se puede  pero NO DEBERIA modificarse 
Atributos protegidos (Protected): Se utiliza un solo guion bajo (_). 
Esto indica que el atributo o método no debe ser accedido directamente fuera de la clase, aunque todavía es accesible.'''

class Personas:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    '''aqui creo una forma de acceder a los atributos privados desde fuera de la funcion
    creando un metodo publico'''   
    def get_apellido(self):
        return self.__apellido
    def get_edad(self):
        return self.__edad

  

persona1 = Personas('Peggy', 'Miranda',5) 

print(persona1._nombre) # Output Peggy, por que solo lleva 1 _ en vez de 2
print(persona1.get_apellido())
#print(persona1.__edad)  si acceso de esta forma va a dar error porque el doble _ lo hace privado


persona1.__apellido = 'test' # test para cambiar el atributo privado
persona1.__edad= 56 # test para cambiar el atributo privado
print(persona1.__edad) # Output 56 pero no modifica el original 

print(persona1.get_apellido()) # output Miranda, el atributo inicial  no se modifica 
print(persona1.get_edad()) # Output 5, el atributo inicial  no se modifica




# los dobles guion bajo se llaman name mangling o atributos privados 
# no se puede acceder desde fuera de la funcion porque da error

class Personas:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        
        
    
persona = Personas('Maggie', 'Miranda',5) # estos son los valores que NO pueden ser cambiados 

#print(persona.__nombre) ## esto va a dar error porque lleva doble __ por eso no se puede acceder 

'''forma correcta de acceder'''
print(persona._Personas__nombre) 
print(persona._Personas__apellido)
print(persona._Personas__edad) 






# los atributos que tienen __ no se pueden acceder desde afuera de la clase como normalmente se hace
# tampoco se pueden modificar esos atributos como normalmente se hace
# la idea de usar los __ es que hace los atributos "privados" y no se acceden desde fuera de la clase y tampoco los pueden modificar 
class Personas:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
 # el  getter se usa para acceder desde afuera de la clase:      
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
        
    def get_edad(self):
        return self.__edad
# el setter se usa para modificar los atributos   
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_apellido(self,apellido):
        self.__apellido = apellido
    
    def set_edad(self,edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print('La edad no puede ser negativa')
    

    
persona = Personas('Maggie', 'Miranda',5)



#con el getter se accede asi:
print(persona.get_apellido())
print(persona.get_nombre())
print(persona.get_edad())

#si quiero modificar algo se hace asi:
'''persona.__apellido = 'Garcia'  pero esta da error porque el atributo es "privado"'''
#modifico los atributos 
persona.set_apellido('Garcia')
persona.set_nombre('Luna')
persona.set_edad(10)
#nuevos atributos:
print(persona.get_apellido())
print(persona.get_nombre())
print(persona.get_edad())


# segunda forma de hacerlo  y es la mas comun en python usando @property que viene siendo como un decorador

class Personas:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
    
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @property
    def edad(self):
        return self.__edad
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido
    
    @edad.setter
    def edad(self,edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print('La edad no puede ser negativa')
    
    

persona = Personas('Maggie', 'Miranda',5)


print(persona.nombre)
print(persona.apellido)
print(persona.edad)



#mismo ejemplo pero con getter y setters

class Personas:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    def get_nombre(self):
        print(f'Nombre: {self.__nombre}.')
        return self.__nombre

    def get_apellido(self):
        print(f'Apellido: {self.__apellido}.')
        return self.__apellido

    def get_edad(self):
        print(f'Edad: {self.__edad}.')
        return self.__edad
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_apellido(self,apellido):
        self.__apellido = apellido
    
    def set_edad(self,edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print('La edad no puede ser negativa')

persona1 = Personas('Peggy', 'Miranda',5) 

persona1.get_apellido()
persona1.get_nombre()
persona1.get_edad()


persona1.set_apellido('Smith')
persona1.set_nombre('Petunia')
persona1.set_edad(2)

persona1.get_apellido()
persona1.get_nombre()
persona1.get_edad()


################3

class Pokemon:
   
    def __init__(self, name, level, health, color, fuerza):
        self.name = name
        self.__level = level # el doble guion bajo va a impedir que acceda desde afuera de la clase 
        self.__health = health
        self.color = color 
        self.__fuerza = fuerza
        
 
    
    @property
    def level(self):
        return f'Level: {self.__level}'
    
    @property
    def health(self):
        return f'Health:  {self.__health}'
    
    
    @property
    def fuerza(self):
        return f'Fuerza: {self.__fuerza}'
    
# los setter van a proporcionar un mecanismo controlado para modificar los valores iniciales de los atributos privados
# si los puedo modificar pero se deben cumplir esa condiciones que estableci
    
    @level.setter
    def level(self, level):
        if level > 0 and level < 5000:
            self.__level = level
        else:
            print("Level cannot be higher than 5000 or negative")


    
    @health.setter
    def health(self, health):
        if health > 0 and health <400:
            self.__health = health
        else:
            print("Health cannot be higher than 400 or negative")
    
    @fuerza.setter
    def fuerza(self, fuerza):
        if fuerza > 0 and fuerza < 500:
            self.__fuerza = fuerza
        else:
            print("Fuerza cannot be higher than 500 or negative")
        
    def rango(self):
        if self.__fuerza >= 500:
            return 'Rango 1'
        elif self.__fuerza >= 400:
            return 'Rango 2'
        elif self.__fuerza >= 300:
            return 'Rango 3'
        else:
            return 'Rango 0'
    
    
    
pokemon1= Pokemon('Pikachu', 300, 250, 'Amarillo', 525)
pokemon2= Pokemon('Charmander', 300, 250, 'Rojo', 325)


pokemon1.__health = 56788 # esto no modifica el metodo privado sino que esta creando uno nuevo
print(pokemon1.__health)
print(pokemon1.health)# aqui se puede comprobar de que el valor original se mantiene a pesar de modificarlo arriba

# como modificar los atributos iniciales cuando son privados?

pokemon1.health = 456 # aca se hace la prueba de modificar con el setter 
print(pokemon1.health) # y aca se ve el resultado
pokemon1.health = 45
print(pokemon1.health)

''' como acceder a los atributos cuando son privados?
igual como si no llevasen doble _ al inicio, esto por el @property que se establecio'''
print(pokemon1.level)
print(pokemon1.health)
print(pokemon1.fuerza) 

print(pokemon1.color)
print(pokemon2.color)





        
    




    
        
        
    
 
 
 


