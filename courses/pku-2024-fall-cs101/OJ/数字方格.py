n=int(input())
k=n//30
n=n%30
max_=0
for a1 in range(n,-1,-1):
    for a2 in range(n,-1,-1):
        for a3 in range(n,-1,-1):
            if (a1+a2)%2==0 and (a2+a3)%3==0 and (a1+a2+a3)%5==0:
                max_=max(a1+a2+a3+90*k,max_)
                break
print(max_)

