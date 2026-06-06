n,m1,m2=map(int,input().split())
A=[]
B=[]

for _ in range(0,n):
    B.append([0]*n)
    A.append([0]*n)
for _ in range(m1):
    row,line,num=map(int,input().split())
    A[row][line]+=num
for _ in range(m2):
    row, line, num = map(int, input().split())
    B[row][line] += num
for row in range(0,n):
    for line in range(0,n):
        out = 0
        for k in range(0,n):
            out+=A[row][k]*B[k][line]
        if out!=0:
            print(row,line,out)
