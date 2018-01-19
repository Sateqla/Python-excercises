def underscore(inputString):
    splitString = inputString.split()
    underscoreString = '_'.join(splitString)
    return underscoreString

def main():
    inputString = input('Give a string with spaces: ')
    finalString = underscore(inputString)
    print(finalString)

main()