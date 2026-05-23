a=int(input())
b=input()
op=[int(x) for x in b.split()]
sum_b=sum(op)
op.sort()
me=0
ok=0
while me<=sum_b/2:
    me+=op.pop(-1)
    ok+=1
print(ok)
