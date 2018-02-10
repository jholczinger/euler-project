'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''
def primes(n):
    '''collecting prime numbers into a list up to n (integer)'''
    prime = [2,3]
    k = 3
    while True:
        count = 0
        k += 2
        for e in prime:
            if k % e != 0:
                count += 1
                print(count)
        if count == len(prime):
            prime.append(k)
        if k == n:
            return sum(prime)
        #if len(prime) == n:
            #return prime[n-1]
print(primes(2*(10**6)))