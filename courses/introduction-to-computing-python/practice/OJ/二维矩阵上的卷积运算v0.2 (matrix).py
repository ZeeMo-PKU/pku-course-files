m,n,p,q=map(int,input().split())
A=[]
for i in range(0,m):
    A.append(list(map(int,input().split())))
B=[]
for j in range(0,p):
    B.append(list(map(int,input().split())))
for a1 in range(0,m-p+1):
    for a2 in range(0,n-q+1):
        out=0
        for a3 in range(0,p):
            for a4 in range(0,q):
                out+=A[a1+a3][a2+a4]*B[a3][a4]
        print(out,end=' ')
    print()
