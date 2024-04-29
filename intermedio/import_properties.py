
#IMPORTACION DE LOS PROPERTIES 

from clase_padre import Avatar

class Maggie(Avatar):
    
    def __init__(self, nombre, health, color, level, waterlevel):
        super().__init__(nombre, health, color, level)
        self.__waterlevel = waterlevel

       #ya no tengo que definir los properties porque los estoy jalando de la clase padre
       # solo defino la propiedad de waterlevel que es unica para esta clase 
       
    @property
    def waterlevel(self):
       return f"Waterlevel :  {self.__waterlevel}"
    
    @waterlevel.setter
    def water_level(self, water_level):
        if 0 <= water_level <= 300:
            self.__waterlevel = water_level
        else:
            print("Water level cannot be higher than 700 or negative")
    
    
    
        
pokemon3 = Maggie('Maggie', 980,'orange', 450, 50) # salud fuera de rango para probar el metodo
# se imprime el "error" del setter healt
print(pokemon3.nombre)
pokemon3.health = 34 #se pasa una nuevo valor dentro del rango 
print(pokemon3.health) # se imprime correctamente

print(pokemon3.water_level) # se imprime correctamente
pokemon3.water_level = 45
print(pokemon3.waterlevel) # se imprime correctamente con el nuevo valor



























        
        
