size = 6
identity = [ [0]*i + [1] + [0]*(size-1-i)  for i in range(0,size)]

def square(n):
    return [[i*j for j in range (0,n)] for i in range(0,n)]

def traspose(matrix):
    trasposedMatrix = []
    for i in range(0,len(matrix[0])):
        newRow = []
        for j in range(0,len(matrix)):
            newRow.append(matrix[j][i])
        trasposedMatrix.append(newRow)
    return trasposedMatrix

def multiply(m1,m2):
    resultMatrix = []

matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
matrixT = traspose(matrix)
print(matrixT)