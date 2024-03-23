# siempre que hay un try tiene que haber un except

try:
    print(10 + '5')
except:
    print('Something went wrong')



n1 = 3
n2 = 4
n3= '4'

try: 
    print(n1+n3)
except: # este except se ejecuta cuando el try da error
    print('hubo un error')
    
    
try:
    print(n1+n2)
except: # este except NO se ejecuta y salta al else 
    print('hubo un error')
else: #este else es opcional
    print('aqui sigue el programa')
    
# si queremos saber la razon del error 

try:
    multiplication = 10-'3'
    print(multiplication)
except:
    print('fatal error')


try:
    multiplication = 10-'3'
    print(multiplication)
except TypeError as e:
    print('the error is: ', e)
    

try:
    resultado = 10/0
except ZeroDivisionError as e:
    print('error: ', e)



   