x = int(input('Enter an integer: '))
y = int(input('Enter an another integer: '))
z = int(input('Enter the last integer: '))
intSum = x+y+z
formatString = 'You gave integers {}, {} and {}. Sum of them is {}.'
finalString = formatString.format(x, y, z, intSum)
print(finalString)