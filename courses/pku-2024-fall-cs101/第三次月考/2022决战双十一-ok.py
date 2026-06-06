n,m=map(int,input().split())
shangpinjiage=[[0]]
for i in range(0,n):
    shangpinjiage.append(list(input().split()))
jianmian=[[0]]
for i in range(0,m):
    jianmian.append(list(input().split()))
result=float('inf')
meigedian=[0]*(m+1)

def dfs(shangpin_num,zongjia):
    global result


    if shangpin_num==n+1:
        zongjia -=(zongjia//300)*50
        for j in range(1,m+1):#遍历每个店
            youhui=0
            for u in jianmian[j]:#遍历每个券
                huaxiao,zhekou=map(int,u.split('-'))
                if meigedian[j]>=huaxiao:
                    youhui=max(youhui,zhekou)
            zongjia-=youhui
        result=min(zongjia,result)
        return 0
    else:
        for t in shangpinjiage[shangpin_num]:

            #print(t)
            # print(t[2:])
            meigedian[int(t[0])]+=int(t[2:])
            zongjia+=int(t[2:])
            dfs(shangpin_num+1,zongjia)

            meigedian[int(t[0])]-=int(t[2:])
            zongjia -= int(t[2:])
dfs(1,0)
print(result)