s=input()
t=input()
n=0
if len(s)!=len(t):
    print('NO')
else:
    for i in range(0,len(s)):
        if s[i]==t[-1-i]:
            n+=1
        else:
            print('NO')
            break
if n==len(s):
    print('YES')