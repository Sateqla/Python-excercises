def quotientProblem(x, y):
    quotient = x//y
    remainder = x%y
    printString = 'The quotient of {} and {} is {} with a remainder of {}.'
    formattedString = printString.format(x, y, quotient, remainder)
    print(formattedString)

def main():
    value1 = 300
    value2 = 115

    x = int(input('Enter an integer: '))
    y = int(input('Enter an another integer: '))
    quotientProblem(x, y)

    quotientProblem(value1, value2)

main()
