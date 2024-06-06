'''Herencia con clases o metodos"privados" y heredando la clase padre de otro file'''


from clase_padre import Avatar  # se importa la clase padre desde el otro file

class Pikachu(Avatar): #el nombre de la clase padre se coloca en la clase hija entre () para que herede la clase
    
    tipo = 'electric'
    
   
   
   # nombre, health, color, level
    def __init__(self, name, health, color, level, amperaje):
        super().__init__(nombre = name, health = health, color = color, level = level)
       
        self.__amperaje = amperaje
      
     
    @property
    def amperaje(self):
       return f"Amperaje:  {self.__amperaje}"
        
        
    @property
    def level(self):
        return f'level: {self._Avatar_level}'
    
    @level.setter
    def level(self, level):
        if 0 <= level <= 700:
            self._Avatar_level = level
        else:
            print("Level cannot be higher than 700 or negative")
            
    @property
    def health(self):
        return f'Health: {self._Avatar_health}'

    @health.setter
    def health(self, health):
        if health < 0:
            print("Health cannot be negative")
            return 
        elif health > 100:
            print("Health cannot be higher than 100")
            return
        else:
            self._Avatar_health = health
            

            
            
            

pikachu1 = Pikachu('pikachu', 90, 'Amarillo', 400, 250)

print(pikachu1.nombre)
print(pikachu1.color)
print(pikachu1.level)
print(pikachu1.health)
print(pikachu1.amperaje)

    
    
        
        
        
        
    







        
    