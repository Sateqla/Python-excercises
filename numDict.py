def createDictionary():
    numbers = dict()
    numbers['one'] = 1
    numbers['two'] = 2
    numbers['three'] = 3
    numbers['four'] = 4

    return numbers

def main():
    dictionary = createDictionary()
    print(dictionary['two'])
    print(dictionary['four'])

    testValue = dictionary['three']*dictionary['four']
    testValue2 = dictionary['three']+dictionary['four']+dictionary['two']+dictionary['one']

    print(testValue)
    print(testValue2)

main()