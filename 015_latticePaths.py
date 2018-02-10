# 20x20 matrix ==> 20 list in a list with each having 20 elements
def NxNmatrix(n):
    #n x n size 'matrix' (20 lists in a list) is generated with 1 as element
    matrixrow = [1]*(n)
    matrix = []
    for row in  range(0,n):
        matrix.append(matrixrow)
    return matrix
def latticePaths(n):
    # n is the number of squares in the lattice !!!! for lattice paths the matrix should be (n+1)x(n+1) size
    lattice = NxNmatrix(n+1)
    for i in range(1,n+1):
        for ii in range(1,n+1):
            lattice[i][ii] = lattice[i-1][ii] + lattice[i][ii-1]
    return lattice[i][ii]

print(latticePaths(10000))