row_A,line_A=map(int,input().split())
A=[]
for iA1 in range(0,row_A):
    A.append(list(map(int,input().split())))

row_B,line_B=map(int,input().split())
B=[]
for iB1 in range(0,row_B):
    B.append(list(map(int,input().split())))

row_C,line_C=map(int,input().split())
C=[]
for iC1 in range(0,row_C):
    C.append(list(map(int,input().split())))

if line_A==row_B and row_A==row_C and line_B==line_C:
    AB=[]
    row_AB=row_A
    line_AB=line_B
    for ooo in range(0,row_AB):
        AB.append([0]*line_AB)
    for iABrow in range(0,row_AB):
        for iABline in range(0,line_AB):
            for c in range(0,line_A):
                AB[iABrow][iABline]+=A[iABrow][c]*B[c][iABline]
    for iABrow in range(0,row_AB):
        for iABline in range(0,line_AB):
            AB[iABrow][iABline]+=C[iABrow][iABline]
    for op in AB:
        print(*op)


else:
    print('Error!')