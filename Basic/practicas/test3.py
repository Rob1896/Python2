
#create a list wtih the even number 4 to 30 

l = list(range(4,30))
even_nos = list(filter(lambda x: x % 2 == 0, l))
print("Even numbers are: ", even_nos)



#print first 10 naturals numbers using while loop

i = 1
while i <= 10:
    print(i)
    i += 1


# Write a program to create a function that takes two arguments, name and age, and print their value

def print_name_age(name, edad):
    print('name: ', name, "edad: ", edad)
    

print_name_age('Peter', 25)

def information(name, age):
    print('name: ', name)
    print("age: ", age)


information('Peter', 25)

#Create a function in such a way that we can pass any number of arguments to this function, and the function should process them and display each argument’s value

def print_args(*args):
    for arg in args: # para que se impriman 1 en cada linea
        print(arg)
        
print_args(1,2,3,4)



#Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. 
#Also, it must return both addition and subtraction in a single return call.

def calculation(a, b):
    add = a + b
    sub = a - b
    return add, sub


print(calculation(10, 5))

#solution 2
def calculation1(a, b):
    add = a + b
    sub = a - b
    return add, sub
result = calculation(10, 7)

print(result)


# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# f the salary is missing in the function call then assign default value 9000 to salary
def employees(name, salary=900):
    print('name: ', name)
    print("salary: ", salary)

employees('Peter',5000)
employees('jen')

# solution 2
def employees1(name, salary=900):
    print('name: ', name,  "salary: ", salary)


employees1('Peter',5000)
    


#Create an inner function to calculate the addition in the following way
#Create an outer function that will accept two parameters, a and b
#Create an inner function inside an outer function that will calculate the addition of a and b
#t last, an outer function will add 5 into addition and return it

def outer_function(a, b): # funcion principal 
    def inner_function(a, b): #second function
        return a + b
    
    add = inner_function(a, b)# third function
    return add + 5
        
        
print(outer_function(10, 5))


#Generate a Python list of all the even numbers between 4 to 30

l = list(range(4,30))

def even_number(a):
    return a % 2 == 0

even_nos = list(filter(even_number, l))

print("Even numbers are: ", even_nos)


#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum

def product(a, b):

    if a * b <= 1000:
        return a * b
    else:
        return a + b
    
print(product(10, 5))

# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

i = 1
while i <= 10:
    print(i)
    i += 1






