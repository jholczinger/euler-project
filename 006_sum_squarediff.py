'''The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''
def sumOfSq(n):
    s = 0
    for k in range(1,n+1):
        s += k**2
    return s

def sqOfSum(n):
    s = 0
    for k in range(1,n+1):
        s += k
    return s**2
print(sqOfSum(100)-sumOfSq(100))