n=int(input())
for i in range(0,n):
    s=int(input())

    a=int(input())
    A=list(map(int,input().split()))

    b=int(input())
    B=list(map(int,input().split()))

    A.sort()#升序
    B.sort(reverse=True)#降序

    A_point=0
    B_point=0

    num=0

    while A_point<a and B_point<b:
        if A[A_point]+B[B_point]==s:
            while True:
                if A_point+1<a and A[A_point+1]==A[A_point]:
                    num+=1
                    A_point+=1
                else:
                    break
            while True:
                if B_point+1<b and B[B_point+1]==B[B_point]:
                    num+=1
                    B_point+=1
                else:
                    break

                num+=1
                A_point+=1
                B_point+=1

        elif A[A_point]+B[B_point]<s:
            A_point+=1

        elif A[A_point]+B[B_point]>s:
            B_point+=1
    print(num)
