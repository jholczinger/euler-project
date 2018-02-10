'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''
# 1. collect multiples in a list, UNDER 1000!!!!
multiples = []
for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        multiples.append(n)
print(multiples)
# 2. get the sum of the list elements and print it
print(sum(multiples))