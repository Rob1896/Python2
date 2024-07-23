import re





text3 = 'the first phone is correct, the second phone is correct, the third phone is wronng, the fourth is correct'
# palabras a buscar:
pattern = 'phone'
word1 = 'is'

print(len(text3)) # output: 105 es solo para saber el len del texto


 

for match in re.finditer(pattern, text3):
    print(match) # output  re.Match object; span=(39, 44), match='phone'>

for match in re.finditer(pattern, text3):
    print(match.span()) # va a imprmir donde comienza y donde termina el match

for match in re.finditer(word1, text3):
    print(match.span()) # output (2, 3), (18, 19), (37, 38)

for match in re.finditer(word1, text3):
    print(match) # output <re.Match object; span=(16, 18), match='is'>


