def main(a,b):
    point_a=0
    point_b=0
    l_a=len(a)
    l_b=len(b)

    while point_a<l_a and point_b < l_b:
        if a[point_a]==b[point_b]:
            point_a+=1
            point_b+=1
        else:
            point_b+=1
    if point_a==l_a:
        return 'Yes'
    else:
        return 'No'
while True:
    try:
        a,b=input().split()
        print(main(a,b))
    except EOFError:
        break