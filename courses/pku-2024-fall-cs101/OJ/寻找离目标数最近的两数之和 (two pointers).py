T=int(input())
s=list(map(int,input().split()))
s.sort()
n=len(s)
left=0
right=n-1



zuo=float('-inf')
you=float('inf')
while left<right:
    if s[left]+s[right]==T:
        you=T
        zuo=T
        break
    if s[left]+s[right]>T:
        you=min(you,s[left]+s[right])
        right-=1
    elif s[left]+s[right]<T:
        zuo=max(zuo,s[left]+s[right])
        left+=1

if T-zuo>you-T:
    print(you)
else:
    print(zuo)