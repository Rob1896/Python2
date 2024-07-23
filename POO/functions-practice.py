# simple
def function():
    print("This is a function")
function()

# con return
def function2():
    return 'this is a function'
print(function2())

# con argumento 

def functions(name):
    print(f'welcome, {name}')

functions('Roberto')
functions('Maggie')

# con  2 arguementos
def args(name, lastname):
    print(f'name:{name}')
    print(f'lastname: {lastname}')

args('Alyssa', 'Miranda')

def args1(name, lastname2):
    print(f'Name:{name}\nLastname:{lastname2}')

args1('Peggy', 'Miranda')

# con argumento predeterminado 
def my_func(language="PythonLanguage"):
    print(f'Lnaguage selected: {language}')

my_func('Java')
my_func()

# retorno de varios valores 

def multiple_return_greet():
    return "Hola", "Python"


greet, name = multiple_return_greet()
print(greet) #hola
print(name) #Python

print(multiple_return_greet()) #outputs  ('Hola', 'Python')

# con args
def variable_arg_names(*args):
    print(f'hola {args}')


variable_arg_names('laptop','desktop','mobile','game')


def variable_arg_greet1(*names):
    # Unir todos los nombres en una sola cadena separada por comas y espacios
    nombres_unidos = ", ".join(names)
    print(f"Hola, {nombres_unidos}!")

variable_arg_greet1("Python", "Brais", "MoureDev", "comunidad")



def variable_arg_greet(*names):
    for names in names:
        print(f"Hola, {names}!")


variable_arg_greet("Python", "Brais", "MoureDev", "comunidad")

# funciones con *kwargs

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")


variable_key_arg_greet(
    language="Python",
    name="Brais",
    alias="MoureDev",
    age=36
)



def update_DB(name,**kwargs):
    print(f'Updating profile: {name}') # este print solo es para imprimir el parametro 'name
    for key, value in kwargs.items():
        print(f'Updating {key} to {value}')

update_DB('Juan', age=30, city='Madrid')
update_DB('Rob', age=27, city='Grecia', IP= '10.2.2.34', DB_Name = 'SQLLITE')


def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)

print(lesser_of_two_evens(9,12))


def larger_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return max(a,b)
    else:
        return min(a,b)

print(larger_of_two_evens(100,12))


def email_validation(email):
    if '@' in email and '.' in email:
        return 'email is correct'
    else:
        return 'email is not correct'

print(email_validation('a@b.c'))
print(email_validation('1232.com'))

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animals_crackers(word1,word2):
    if word1[0] == word2[0]:
        return True
    else:
        return False

print(animals_crackers('cog','cat'))


#makes thirty

def makes_thirty(n1,n2):
    if n1 + n2 == 30:
        return True
    elif n1 == 30:
        return True
    elif n2 == 30:
        return True
    else:
        return False
    
print(makes_thirty(20,450))


#Write a function that capitalizes the first and fourth letters of a name

def old_mcdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short'
    
print(old_mcdonald('mcdonald'))


# Given a sentence, return a sentence with the words reversed
def master_yoda(word):
    return word[::-1]

print(master_yoda('I am home'))
print(master_yoda('testing'))

# Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    if n >= 10 or n >= 100 and n <= 200:
        return True
    else: return False

print(almost_there(90))
print(almost_there(3))




    


   

   
