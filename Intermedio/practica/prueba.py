cadena4 = 'take a look around'

concurrencia = cadena4.count('a')


print(concurrencia)


cadena3 = 'mamammmmsdadsmamasda'
count = 0
for i in cadena3:
    if i != 'm': # si es diferente a M que pase a la siguiente letra,cadd vez que i encuentre a M se ejecuta el Else
        continue 
    else: # si el IF NO SE CUMPLE que sume 1 al contador, o sea cada que i encuente a M.
        count = count + 1 # basicamente no esta buscando M en la cadena sino que cuenta las veces que el IF no se cumplio

print('Total number of m is:', count) # muestra el resultado de las veces que IF no se cumplio y se cumplio el else sumandole 1 al count 


