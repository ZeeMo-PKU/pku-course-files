from functools import lru_cache

n=int(input())
cishu=0
@lru_cache
def move_way(n,start,way,end):
    global cishu
    if n==1:
        print(f'{start}->{end}')
        cishu+=1
    else:
        move_way(n-1,start,end,way)
        print(f'{start}->{end}')
        cishu+=1
        move_way(n-1,way,start,end)

move_way(n,'A','B','C')
print(cishu)