def quotientProblem(x, y):
    quotient = x//y
    remainder = x%y
    print(quotientString(x, y, quotient, remainder))

def quotientString(x, y, quotient, remainder):
    printString = 'The quotient of {x} and {y} is {quotient} with a remainder of {remainder}.'
    formattedString = printString.format(**locals())
    return formattedString

def main():
    value1 = 300
    value2 = 115

    x = int(input('Enter an integer: '))
    y = int(input('Enter an another integer: '))
    quotientProblem(x, y)

    quotientProblem(value1, value2)

main()
