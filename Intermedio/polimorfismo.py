



class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")


class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

# Función que usa polimorfismo
def desplazar_vehiculo(vehiculo):
    vehiculo.desplazamiento()

# Ejemplo de uso del polimorfismo
coche = Coche()
moto = Moto()
camion = Camion()

# Llamada a la función desplazar_vehiculo con diferentes tipos de vehículos
desplazar_vehiculo(coche)  # Salida: Me desplazo utilizando cuatro ruedas
desplazar_vehiculo(moto)   # Salida: Me desplazo utilizando dos ruedas
desplazar_vehiculo(camion) # Salida: Me desplazo utilizando seis ruedas


# ejemplo 2

class Perro:
    def hacer_sonido(self):
        return "Guau"

class Gato:
    def hacer_sonido(self):
        return "Miau"

# Función que usa polimorfismo
def hacer_sonido_animal(animal):
    print(animal.hacer_sonido()) # este .hacer_sonido llama al metodo de cada clase arriba

# Crear instancias de las clases
mi_perro = Perro()
mi_gato = Gato()

# Llamar a la función con diferentes objetos
hacer_sonido_animal(mi_perro)  # Imprime "Guau"
hacer_sonido_animal(mi_gato)   # Imprime "Miau"


# ejemplo 3

class Vehiculo:
    def moverse(self):
        pass

class Carro(Vehiculo):
    def moverse(self):
        return "Conducir"

class Bicicleta(Vehiculo):
    def moverse(self):
        return "Pedalear"

def describir_movimiento(vehiculo):
    print(vehiculo.moverse())

# Crear instancias de las clases 
mi_carro = Carro()
mi_bicicleta = Bicicleta()

# Llamar a la función con diferentes objetos
describir_movimiento(mi_carro)      # Imprime "Conducir"
describir_movimiento(mi_bicicleta)  # Imprime "Pedalear"


# ejemplo 4
class ArchivoTexto:
    def leer(self):
        return "Leyendo datos de un archivo de texto"

class ArchivoCSV:
    def leer(self):
        return "Leyendo datos de un archivo CSV"

def procesar_archivo(archivo):
    print(archivo.leer())

# Crear instancias de las clases
archivo_texto = ArchivoTexto()
archivo_csv = ArchivoCSV()

# Llamar a la función con diferentes objetos
procesar_archivo(archivo_texto)  # Imprime "Leyendo datos de un archivo de texto"
procesar_archivo(archivo_csv)    # Imprime "Leyendo datos de un archivo CSV"


# ejemplo 5

class Boton:
    def hacer_click(self):
        return "Botón clickeado"

class CheckBox:
    def hacer_click(self):
        return "Checkbox marcado"

def simular_click(elemento):
    print(elemento.hacer_click())

# Crear instancias de las clases
boton = Boton()
checkbox = CheckBox()

# Llamar a la función con diferentes objetos
simular_click(boton)    # Imprime "Botón clickeado"
simular_click(checkbox) # Imprime "Checkbox marcado"


# ejeplo 6

class PagoTarjeta:
    def procesar_pago(self):
        return "Procesando pago con tarjeta de crédito"

class PagoPayPal:
    def procesar_pago(self):
        return "Procesando pago con PayPal"

def realizar_pago(metodo_pago):
    print(metodo_pago.procesar_pago())

# Crear instancias de las clases
pago_tarjeta = PagoTarjeta()
pago_paypal = PagoPayPal()

# Llamar a la función con diferentes objetos
realizar_pago(pago_tarjeta)  # Imprime "Procesando pago con tarjeta de crédito"
realizar_pago(pago_paypal)   # Imprime "Procesando pago con PayPal"