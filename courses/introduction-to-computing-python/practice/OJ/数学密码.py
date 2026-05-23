a=int(input())
for i in range(int(a/6),0,-1):
    if a%i==0 and a//i>5:
        print(i)
        break