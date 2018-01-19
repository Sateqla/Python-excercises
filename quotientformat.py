x = int(input('Enter an integer: '))
y = int(input('Enter an another integer: '))
quotient = x//y
remainder = x%y
printString = 'The quotient of {} and {} is {} with a remainder of {}.'
formattedString = printString.format(x, y, quotient, remainder)
print(formattedString)