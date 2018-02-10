'''he sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.'''
sieve = [True]*2000000

def dafaq(aList, x):
    for i in range(x+x,len(aList),x):
        aList[i] = False

for k in range(2, int(len(sieve)**0.5)+1):
    if sieve[k]:
        dafaq(sieve, k)

print(sum(i for i in range(2,len(sieve)) if sieve[i]))