#Imprime «Hola Mundo» si a es mayor a b

a = 10
b = 5

if a > b:
    print("Hola Mundo")




#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.


age = int(input("What is your age:"))
if age >= 18:
        print('you are older')
else:
    print('you are not older')
    

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

age = int(input("edad: "))
ingreso = int(input("escriba su ingreso mensual: "))
if age >= 16 and ingreso >= 1000:
    print('debe pagar impuesto')
else:
    print('no debe pagar impuesto')
    
    

name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)

# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad = int(input("Cual es tu edad: "))
if age <= 4:
    print("Su entrada es gratis")
elif age <= 18:
    print("Costo de la entrad 5")
else:
    print("Costo de la entrada 10")
    
# otra forma de hacerlo

edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "€.")



# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
#Renta	Tipo impositivo
#Menos de 10000€	5%
#Entre 10000€ y 20000€	15%
#Entre 20000€ y 35000€	20%
#Entre 35000€ y 60000€	30%
#Más de 60000€	45%


renta = int(input("Cual es su renta Anual: "))
if renta < 10000:
    impuesto = '5%'
elif renta > 10000  and renta < 20000:
    impuesto = '15%'
elif renta > 20000 and renta < 35000:
    impuesto = '20%'
elif renta > 35000 and renta < 65000:
    impuesto = '30%'
elif renta >  65000:
    impuesto = '45%'
print('Su impuesto es de:', impuesto, 'pelucholares')



# Imprime «Hola Mundo» si a es mayor a b.

a = 10
b = 5

if a > b:
    print("Hola Mundo")

# Escribí un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla al mayor de los dos.

numero1=int(input("Un número:"))
numero2=int(input("Otro número distinto:"))
if numero1>numero2:
    print(numero1, "es mayor")
else:
    print(numero2, "es mayor")
    
# Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”.
# Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.

letra=input("Letra:")
if len(letra)!=1:
    print("Debe ser sólo una letra")
else:
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        print("Es vocal")
    else:
        print("No es vocal")
        

# Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.

n1=int(input("Primer numero:"))
n2=int(input("Segundo número:"))
n3=int(input("Tercer número:"))
if n1<n2:
    if n1<n3:
        print("Menor:", n1)
    else:
        print("Menor:", n3)
else:
    if n2<n3:
        print("Menor:", n2)
    else:
        print("Menor:", n3)


# Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. 
# Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos
# . Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.
    


username = input("Username: ")
password = input('type your password: ')

if password == "Maggie20" and username == "Rob456":
    print("Access granted!")
else:
    print("Access denied!")




frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")



