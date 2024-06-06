
#Solicitar monto consumido


monto = float(input("Ingrese monto consumido: "))
if monto > 50 and monto <= 100:
    descuento = monto * 0.10
    total = monto - descuento
    print(f'Su descuento es de:{descuento:.2f}')
    print(f"El total a pagar es:  {total}")

elif monto > 100 and monto <= 200:
    descuento = monto * 0.15
    total = monto - descuento
    print(f'Su descuento es de:{descuento:.2f}')
    print(f"El total a pagar es:  {total}")

elif monto > 200:
    descuento = monto * 0.20
    total = monto - descuento
    print(f'Su descuento es de:{descuento:.2f}')
    print(f"El total a pagar es:  {total}")
else:
    print(f"No tiene descuento \nEl total a pagar es:  {monto}")

# forma 2

monto1 = float(input('Ingrese monto consumudo: '))

if monto1 > 50 and monto1 <= 100:
    descuento1 = 0.1
elif monto1 > 100 and monto1 <=200:
    descuento1 = 0.2
elif monto1 > 200 and monto1 <=300:
    descuento1 = 0.3
else:
    descuento1 = 0

total1 = monto1 - (monto1 * descuento1)

print(f'Su descuento es de:{descuento1*100:.2f}%')






         
       
    


        

