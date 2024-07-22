'''Las expresiones regulares (regular expressions, regex o regexp)
en Python son una herramienta poderosa utilizada para buscar y manipular cadenas de texto basándose en patrones específicos. 
Permiten realizar tareas como la búsqueda de coincidencias, la sustitución de texto y la extracción de datos dentro de una cadena.

Python proporciona el módulo re para trabajar con expresiones regulares. A continuación, se muestran algunos conceptos y ejemplos básicos:'''



import re

text = 'this is a text example, this text is going to help you understand the text in the system'


# este ejemplo es basico y solo va a encontrar la primera palabara de la cadena y omite las demas

# formas de buscar palabra en una cadena
#guardando la palabra en una variable
pattern = 'text'
print(re.search(pattern, text)) #output:   span=(10, 14), match='text'> span es el index de donde se encontro la palbra que busco.
pattern2 = 'example'
print(re.search(pattern2, text))

# usando print
print(re.search('text', text))
print(re.search('help', text))

# guardando la funcion en una variable

result = re.search(pattern, text) # palabra a buscar "text" guardado en pattern 
print(result)

# algunos metodos de RE
print(result.span()) # output (10,14) exact index
print(result.start())# output 10 start index
print(result.end()) #output 14 end index


'''para contar TODAS las veces que aparece una palabra en un text'''

text1 = 'the first phone is correct, the second phone is correct, the third phone is wronng'

pattern = 'phone'
print(re.findall(pattern, text1)) # output: ['phone', 'phone', 'phone']
print(len(re.findall(pattern, text1))) # output 3

# second way
matches = re.findall(pattern, text1)
print(matches)
print(len(matches)) # output: 3, cuenta las veces que aparece una palabra en un texto

# ejemplo 2
word1 = 'is'
find_word = re.findall(word1, text1)
print(find_word) # output: ['is', 'is', 'is']
print(len(find_word)) # output: 3


# ejemplo con bucle for 

text3 = 'the first phone is correct, the second phone is correct, the third phone is wronng, the fourth is correct'
# palabras a buscar:
pattern = 'phone'
word1 = 'is'

print(len(text3)) # output: 105 es solo para saber el len del texto


# ejemplo con bucle for 

for match in re.finditer(pattern, text3):
    print(match.span()) # output (10, 11), (23, 24), (43, 44)

for match in re.finditer(word1, text3):
    print(match.span()) # output (2, 3), (18, 19), (37, 38)







