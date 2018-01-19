def calculateDiscount(discountPercent, price):
    discount = (1 - discountPercent/100) * price
    formattedDiscount = format(discount, '.2f')
    return formattedDiscount

def main():
    price = float(input('Give original price: '))
    discountPercent = float(input('Give discount percent: '))

    finalPrice = calculateDiscount(discountPercent, price)

    print('Your price with discount is ' + finalPrice)

main()