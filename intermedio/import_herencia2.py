
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
        

       

    
    
        
   
        
    def describe(self):
        print("Name: ", self.nombre, "\nHealth: ", self.health, "\nColor: ", self.color, "\nLevel: ", self.level, "\nFire Level: ",self.fire)
       
        
        
   
        
       
pokemon2 = Charmander('charmander', 80,'Orange', 690, 10)

pokemon2.level = 40
print(pokemon2.health) # la propiedad esta en la clase padre por eso ya no necesito crearla en esta clase 









        
        
