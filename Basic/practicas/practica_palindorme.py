
#verificar si palabra es palindrome 
#funcion:
def palindrome():
    word = input('Ingrese una palabra: ')
    word = word.lower()
    if word == word[::-1]:
        print('La palabra es palindrome')
    else:
        print('La palabra no es palindrome')

palindrome()



word1 = input('ingrese una palabra: ')

word1 = word1.lower()
word1 = word1.replace(' ', '')

if word1 == word1[::-1]:
    print('La palabra ingresada es palindrome')
else:
    print('La palabraingresada no es palindrome')



        