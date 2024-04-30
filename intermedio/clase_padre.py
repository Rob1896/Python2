
'''Herencia con clases o metodos"privados" y heredando la clase padre de otro file'''

#clase padre:


class Avatar:
    def __init__(self, nombre, health, color, level):
        self.nombre = nombre
        self.health  = health
        self.color = color
        self.level = level
        
        
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
        

