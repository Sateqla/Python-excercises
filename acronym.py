def main():

    splittedString = input('Give the string for acronym generation: ').upper().split()

    # inputString = input('Give the string for acronym generation: ')
    # capString = inputString.upper()
    # splittedString = capString.split()

    letters = []

    for i in splittedString:
        letters.append(i[0])

    acronym = ''.join(letters)

    print(acronym)

main()