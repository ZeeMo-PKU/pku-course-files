input()

pingfangshu=tuple([i**2 for i in range(1,32)])
nums=list(map(int,input().split()))
ans=[]
for num in nums:
    for k in pingfangshu:
        if k>=num:
            break

        if num-k in pingfangshu:
            ans.append(num)
            break

for a in ans:
    print(f"{bin(a)} {oct(a)} {hex(a)}")