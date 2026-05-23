n=int(input())
my_list=[]
for i in range(0,n):
    a,b=input().split()
    b=int(b)
    my_list.append((a,b))
my_list.sort(key=lambda x:(-x[-1],x[0]))
for x in my_list:
    print(*x)