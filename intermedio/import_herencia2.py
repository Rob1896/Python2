
from clase_padre import Avatar

class Charmander(Avatar):
    
    def __init__(self, nombre, health, color, level, fire):
        super().__init__(nombre, health, color, level)
        self._fire = fire
       
    @property
    def fire(self):
        return f'Fire:  {self._fire}'
    
    @fire.setter
    def fire(self, fire):
        if 0 <= fire <= 300:
            self._fire = fire
        else:
            print("Fire cannot be higher than 300 or negative")
        
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
       

    
    
        
   
        
    def describe(self):
        print("Name: ", self.nombre, "\nHealth: ", self.health, "\nColor: ", self.color, "\nLevel: ", self.level, "\nFire Level: ",self.fire)
       
        
        
   
        
       
pokemon2 = Charmander('charmander', 80,'Orange', 690, 10)


pokemon2.describe()
pokemon2.health = 90
pokemon2.describe()









        
        
