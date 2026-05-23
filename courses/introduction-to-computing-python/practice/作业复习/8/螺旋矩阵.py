#n*m的矩阵
def g(matrix):
    n=len(matrix)

    out=[]
    if n==1:
        return matrix[0]
    m = len(matrix[0])
    if m==1:
        return [i[0] for i in matrix]
    if n==2:
        return [i for i in matrix[0]]+list(reversed(matrix[1]))
    if m==2:
        return [matrix[0][0]]+[matrix[i][1] for i in range(0,n)]+[matrix[j][0] for j in range(n-1,0,-1)]
    next1=[]
    for i in range(1,n-1):
        next1.append([*matrix[i][1:-1]])
    print(next1)
    return matrix[0]+[matrix[i][-1] for i in range(1,n-1)]+list(reversed(matrix[-1]))+[matrix[j][0] for j in range(n-2,0,-1)]+g(next1)

print(g([[2,5],[8,4],[0,-1]]))
