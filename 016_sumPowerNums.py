'''2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?'''
def sumPowerDigits(n):
    # returning the sum of the digits of an integer
    string = str(n)
    summa = 0
    for s in string:
        summa += int(s)
        print(summa)
    return summa

n = 2**1000
print(sumPowerDigits(n))