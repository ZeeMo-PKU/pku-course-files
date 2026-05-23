#转化为整数，不可以用字典序
# （为什么呢？）
#python中的list.sort（）很稳定
#归并排序和插入排序都很稳定
#Merge sort（归并排序）是什么？
#elderly.sort(key=lambda x: -x[1])
n=int(input())
laoren=[]
nianqingren=[]
for _ in range(0,n):
    id,year=map(str,input().split())
    year=int(year)
    if year>=60:
        laoren.append((id,year))
    else:
        nianqingren.append((id,year))
#laoren.sort(key=lambda y:y[0],reverse=True)
#这样是不可以的，因为有年龄一样的难搞
#所以我们应该是
laoren.sort(key=lambda x:-x[1])
for a1 in laoren:
    print(a1[0])
for a2 in nianqingren:
    print(a2[0])