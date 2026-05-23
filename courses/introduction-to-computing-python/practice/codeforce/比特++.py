a1=eval(input())
a2=0
for i in range(0,a1):
    b=input()
    if b=='++X' or b=='X++':
        a2+=1
    elif b=='X--' or '--X':
        a2-=1
print(a2)