a=int(input())
q=[]
p=0
for i in range(0,a):
    b_out,b_in=map(int,input().split())
    q.append(p+b_in-b_out)
    p=p+b_in-b_out
print(max(q))
