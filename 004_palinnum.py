'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''
# interval is 100*100 - 999*999
def isPalin(n):
    s = str(n)
    if len(s) == 1:
        return True
    elif s[0] == s[-1]:
        if len(s) == 2:
            return True
        else:
            return isPalin(s[1:len(s) - 1])
    else:
        return False

temp = 0
interval = range(999,99,-1)
n = 1000
palind = {}
while n != 99:
    n -= 1
    for i in interval:
        s = n*i
        temp = isPalin(s)
        if temp  == True: # if len(str(i)) == 3 and same for n didn't work...why?range was reversed
            palind[n*i] = (i,n)
        else:
            continue
print(palind)
max_key = max(list(palind.keys()))
print('largest palin:', palind[max_key][0]*palind[max_key][1])