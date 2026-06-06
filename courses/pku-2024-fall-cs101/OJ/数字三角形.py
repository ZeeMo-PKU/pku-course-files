#dp
N=int(input())
shuzisanjiaoxing=[[0]]
for i in range(0,N):
    shuzisanjiaoxing.append([0]+list(map(int,input().split()))+[0])
out=[]
for i in range(2,N+1):
    for j in range(1,i+1):
        shuzisanjiaoxing[i][j]=shuzisanjiaoxing[i][j]+max(shuzisanjiaoxing[i-1][j],shuzisanjiaoxing[i-1][j-1])
print(max(shuzisanjiaoxing[-1]))
