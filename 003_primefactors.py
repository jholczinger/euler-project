'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''
#1. find prime numbers
d = 600851475143

def largestPrimeFactor(n):
    while True:
        for l in range(2,n+1):
            #if n == l:
                #return n
            if n % l == 0:
                if n/l == 1.0:
                    return n
                else:
                    n = n/l
                print(n)
            #largestPrimeFactor(int(n/l)
print(largestPrimeFactor(d))