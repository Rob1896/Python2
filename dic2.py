




for x in "banana":
  print(x)
  
txt = "The best things in life are free!"
print("free" in txt) # true


txt = "The best things in life are free!"
print("expensive" not in txt) # true porque NO esta 

a = "Hello, World!"
print(a.replace("H", "J"))


def is_even (n):
    if n * 2 == 20:
        print('Congrats!')
        return True
    else:
        print('Sorry')
    return False

print(is_even(8)) 



def check_even_list(num_list):
    
    even_numbers = []
    
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we append the even number
        if number % 2 == 0:
            even_numbers.append(number)
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return even_numbers



print(check_even_list(range(20,45)))


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


edad = int(input('introduce tu edad: '))
while edad < 5:  # este while se va a ejecutar siempre que la condicion no se cumpla
     print('no cumples los requisitos')
     edad = int(input('introduce nuevamente: ')) # este input se va a ejecutar hasta que se ingrese la condicion correctamente
    
print('gracias puedes pasar!') # si el while se cumple se sale del while y se ejecuta este print, o sea el resto del programa sigue su curso
print('la edad de la persona es: '+ str(edad))