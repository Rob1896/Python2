import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
sentence = 'Start a sentence and then bring it to an end'


pattern = re.compile(r'abc')
matches = pattern.findall(text_to_search)
matchess = pattern.finditer(text_to_search)
matcches1 = pattern.search(text_to_search) # search no lo puedo poner como iterable por eso no esta en el bucle for.

print(matches)  # output ['abc']
print(matcches1) # output <re.Match object; span=(1, 4), match='abc'>

for match in matches:
    print(match) # output abc

for i in matchess:
    print(i) # output <re.Match object; span=(1, 4), match='abc'>


