num=int(input())
num=num%26
a=input()
for i in range(0,len(a)):
    q=ord(a[i])
    if 65<=q<=90:
        p=q-num
        if 65<=p<=90:
            print(chr(p),end='')
        else:
            o=90-65+p+1
            print(chr(o),end='')
    else:
        p = q - num
        if 97 <= p <= 122:
            print(chr(p),end='')
        else:
            o=122-97+p+1
            print(chr(o),end='')