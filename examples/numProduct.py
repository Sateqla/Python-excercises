'''Code for an INCORRECT function intended to return
the product of the numbers in a list.'''
def product(nums):
    prod = 1
    for n in nums:
        prod = prod*n
    return prod

print(product([5, 4, 6]))

