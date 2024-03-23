#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

word = input("escriba una palabra: ")
for i in range(10):
    print(word)


#  Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
age = int(input("¿Cuántos años tienes? "))
for i in range(age):
    print("Has cumplido " + str(i+1) + " años")
    
    
 #Imprimir todos los dígitos decimales, del 0 al 9, utilizando una repetición.   
    
for x in range(10):
    print(x)
    
# Imprimir todos los números entre el 100 y el 199.

for x in range(100, 200):
    print(x)

# Imprimir los números entre el 5 y el 20, saltando de tres en tres.

for x in range(5,20,3):
    print(x)

for x in range(5,25,2):
    print(x)

#Escribir un programa que muestre la sumatoria de todos los números entre el 0 y el 100.


total=0
for i in range(101):
    total=total+i
print("Sumatoria:", total)

# escribir un programa que evalue la edad usando while
edad = int(input('introduce tu edad: '))
while edad < 5:
     print('no cumples los requisitos')
     edad = int(input('introduce nuevamente: '))
     
print('gracias puedes pasar!')
print('la edad de la persona es: '+ str(edad))

