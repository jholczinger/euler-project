'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''
def factor(m):
    num = 1
    for i in range(1,m+1):
        num *= i
    return num
##########################
def isDivisible(n, m):
    count = 0
    for i in range(1, m+1):
        if n % i == 0:
            count += 1
    if count == m:
        return True
    else:
        return False
##########################
def minNumDivBy(m):
    divisible = False
    min_num = 9699680
    while not divisible:
        min_num += 20
        divisible = isDivisible(min_num, m)
    return min_num
##########################
print(factor(4)) # factor works
print(isDivisible(12,4)) # isDivisible works
print(minNumDivBy(20))
