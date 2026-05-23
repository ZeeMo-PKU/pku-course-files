def jiafa(f1:list,f2:list):
    dic_ans=dict()

    #求和
    l_f1=len(f1)//2-1
    l_f2 = len(f2) // 2 - 1
    for i in range(0,l_f1):
        xishu=f1[2*i]
        mishu=f1[2*i+1]

        if mishu in dic_ans:
            dic_ans[mishu]+=xishu
        else:
            dic_ans[mishu]=xishu
    for i in range(0,l_f2):
        xishu=f2[2*i]
        mishu=f2[2*i+1]

        if mishu in dic_ans:
            dic_ans[mishu]+=xishu
        else:
            dic_ans[mishu]=xishu



    ans=[]

    items =[]
    for mishu,xishu in dic_ans.items():
        if xishu!=0:
            items.append((mishu,xishu))
    items.sort(reverse=True)


    for mishu,xishu in items:
        if xishu!=0:
            print(f'[ {xishu} {mishu} ]',end=' ')
    print()



n=int(input())
for i in range(0,n):
    f1=list(map(int,input().split()))
    f2=list(map(int,input().split()))
    jiafa(f1,f2)