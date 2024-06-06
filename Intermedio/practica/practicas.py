import math
#sumar 2 numeros y mostrar sus resultados
a = 3
b = 4

c = a + b
print(c)

#solucion en funcion
def add(a, b):
    return a + b

print(add(3, 4))


# calcula el area de un circulo con un radio dado

radio = 3
print(math.pi * radio ** 2)

#solucion en funcion
def radio(a):
    return math.pi * a ** 2

print(radio(3))

# concatena 2 cadenas de texto
b = 'hola'
c = 'circ'
r = b + ' '+ c

print(r)

# multiplica 2 numeros y muestra su resultado
num1 = 4
num2 = 4
result = num1 * num2

print('result:',result)

#solucion en funcion

def multiplicacion(a, b):
    r = a * b
    print('resultado: ', r)

multiplicacion(4, 4)

# crea una cade de texto y muestra su longitud

strin1 = 'hello world, i love my wife'
long = len(strin1)

print(long)

#solucion en funcion

def longitud(a):
    print('longitud: ', len(a))

longitud('hello world, i love my wife')

# calcula promedio de una lista de numeros

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
promedio = sum(lista) / len(lista)

print(promedio)


# crea una tupla e imprimela 

my_tuples = tuple([1, 2, 3, 4, 5, 6, 7,])

print(type(my_tuples))

# crea una cadena e imprimela al reves


strin2= 'helow world my name is peggy'

r = strin2[::-1]

print(r)

# calcla el area de un rectangulo 

base = int(input('ingrese la base: '))
altur = int(input('ingrese la altura: '))

area = (base * altur) / 2

print('el area del triangulo es: ', area)

# solucion en funcion

def area(a, b):
    return (a * b) / 2

print('el area del triangulo es: ', area(3, 4))


# conviere un int en una string 
num = 100
print(type(num))

num = str(num)
print(type(num))


# ordenar lista de numeros de menor a mayor
lista2 = [1,4,6,8,9,45,2,67,890]

lista2.sort()

print(lista2)


# cuenta cuantas v

cadena4 = 'take a look around'
concurrencia = cadena4.count('a')
print(concurrencia)

# con bucle for 
cadena3 = 'mamammmmsdadsmamasda'
count = 0
for i in cadena3:
    if i != 'm': # si es diferente a M que pase a la siguiente letra,cadd vez que i encuentre a M se ejecuta el Else
        continue 
    else: # si el IF NO SE CUMPLE que sume 1 al contador, o sea cada que i encuente a M.
        count = count + 1 # basicamente no esta buscando M en la cadena sino que cuenta las veces que el IF no se cumplio

print('Total number of m is:', count) # muestra el resultado de las veces que IF no se cumplio y se cumplio el else sumandole 1 al count 



count = 1

while count <= 5:
    print(count)
    count = count + 1
    












