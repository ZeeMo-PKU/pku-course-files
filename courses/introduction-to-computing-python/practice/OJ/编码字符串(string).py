a=list(input())
a.append('ooooo')
n=1
for i in range(0,len(a)-1):
    if a[i].lower()==a[i+1].lower():
        n+=1
    else:
        print(f'({a[i].lower()},{n})',end='')
        n=1