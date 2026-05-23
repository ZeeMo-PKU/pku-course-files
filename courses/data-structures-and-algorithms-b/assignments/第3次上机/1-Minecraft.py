def f(n:int):
    a=0
    b=0
    c=0
    #a>=b>=c
    ans=[]
    for a in range(1,int(n**1/3)+1):
        if n%a==0:
            for b in range(1,int((n/a)**0.5)+1):
                if (n//a)%b==0:
                    c=(n//a)//b
                    ans.append(a*b+b*c+a*c)
    return min(ans)*2




n=int(input())
print(f(n))