
#write a for loop thar prints the integers from the list but only if they are even numbers

integers = [1,2,3,4,5,6,7,8,9]

for i  in integers:
    if  i % 2 == 0:
        print(i)


# write a while loop that has the same functionality as the following for loop

furniture = ['table','chairs', 'desktop','lamp','tv']

for i in furniture:
    print(f'YOU WILL NOT BE ABLE TO FIND A {i.upper()} CHEAPER THAN OUR PRICES')

# while 
i = 0

while i < len(furniture):
    print(f'YOU WILL NOT BE ABLE TO FIND A {furniture[i].upper()} CHEAPER THAN OUR PRICES')
    i += 1




string = 'memomamimumn'

count = 0
for i in string:
    if i != 'm':
        continue
    else:
        count = count + 1

print('Total number of m is:', count)


#Print First 10 natural numbers using while loop

number = 1

while number <= 10:
    print(number)
    number += 1


rows = 6

for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')


rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')




