p=int(input())
wuqi=list(map(int,input().split()))
# print(wuqi)
wuqi.sort()
if p<wuqi[0]:
    print(0)
else:
    zuo=0
    you=len(wuqi)-1

    ans=0

    while zuo<you:
        if p>=wuqi[zuo]:
            ans+=1
            p-=wuqi[zuo]
            zuo+=1

        else:
            if ans>0:
                ans-=1
                p+=wuqi[you]
                you-=1
            else:
                break
    if zuo==you and p>=wuqi[zuo]:
        ans+=1
    print(ans)
