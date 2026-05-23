a=bin(int(input()))
b=list(a)
b=b[2:]

c=b[::-1]
# print(b,c)
if c==b:
    print('Yes')
else:
    print('No')
