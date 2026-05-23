def qianxvzhouyou(dic,root):
    if root in dic:
        (left,right)=dic[root]
        return [root]+qianxvzhouyou(dic,left)+qianxvzhouyou(dic,right)
    else:
        return []
def tianjia(dic,root,x):
    if x in dic:
        return
    if x>=root:
        if root not in dic or dic[root][1]==-1:
            dic[root][1]=x
            dic[x]=[-1,-1]
            return
        else:
            tianjia(dic,dic[root][1],x)
            return
    else:
        if root not in dic or dic[root][0]==-1:
            dic[root][0]=x
            dic[x]=[-1,-1]
            return
        else:
            tianjia(dic,dic[root][0],x)
            return
nums=list(map(int,input().split()))
root=nums[0]
dic={}
root=nums[0]
dic[root]=[-1,-1]
for i in range(1,len(nums)):
    tianjia(dic, root, nums[i])
print(*qianxvzhouyou(dic,root))