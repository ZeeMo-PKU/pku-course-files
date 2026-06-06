n=int(input())
list_=list(map(int,input().split()))
for j in range(0,n):
    for i in range(0,n-1-j):#此处改进
        if list_[i]>list_[i+1]:
            list_[i+1],list_[i]=list_[i],list_[i+1]
print(*list_)
