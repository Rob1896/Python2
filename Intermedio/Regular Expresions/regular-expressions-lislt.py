
import re

# metacartecteres

names = ['Roberto Mercado',
        'Marimar Gonzalez', 
        'Petunia Gonzalez',
        'Pedro Martinez',
        'Marta Martinez',
        'Pedro Lopez',
        'Alejandro Lopez',
        'Maria Lopez',
        'Carlos Lopez',
        'Maria Lopez',
        'Juan Lopez',]

# comienza con: 
for name in names:
    if re.findall('^Pedro', name): #el ^ busca los elementos que comienzan con x o y parametro
        print(name)

for name in names:
    if re.findall('Lopez$', name): #el $ busca los elementos que terminan con x o y parametro
        print(name)


# buscar elementos que esten en un rango

import re

things = ['carro',
         'manzana',
         'barco',
         'oro',
         'orco',
         'ana',
         'alla',
         'abeja',
         'amigo',
         'huevo',
         'cafe',
         ]

for thing in things:
    if re.findall('[o-t]', thing): # busca elementos entre la O y la T
        print(thing) 

for thing in things:
    if re.findall('^[o-t]' , thing): # busca elementos que comienzan entre la O y la T
        print(thing)  

for thing in things:
    if re.findall('[a-f]$' , thing): # busca elementos que terminan entre la O y la T
        print(thing)




