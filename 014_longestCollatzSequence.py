'''The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.'''

def getCollatzSeq(startNum):
    # startNum is an integer, the function gives the length of the sequence
    latestNum = startNum
    count = 1
    if startNum == 0:
        return 0
    while latestNum != 1 or count == 1:
        count += 1
        if latestNum % 2 == 0:
            latestNum = latestNum//2
        else:
            latestNum = latestNum*3 + 1
    return count
def getLongestSeq(startCap):
    # startCap gives an integer which is the highest number which the program test the length of the Collatz seq
    #aDict = {}
    seqLen = 0
    startNum = 0
    for n in range(1, startCap + 1):
        seqLenNext = getCollatzSeq(n)
        startNumNext = n
        if seqLen < seqLenNext:
            seqLen = seqLenNext
            startNum = startNumNext
    return startNum, seqLen
        #aDict[getCollatzSeq(n)] = n
        #if  len(list(aDict.keys())) > 1:
           # maxKey = max(list(aDict.keys()))
            #maxVal = aDict[maxKey]
            #aDict = {maxKey:maxVal}
    #return aDict
print(getCollatzSeq(13))
print(getLongestSeq(1000000))