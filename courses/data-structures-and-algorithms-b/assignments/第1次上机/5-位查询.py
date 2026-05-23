n,m=map(int,input().split())
numbers=list(map(int,input().split()))
for i in range(0,m):
    a,b=input().split()
    b=int(b)
    if a=='Q':
        counter=0
        for num in numbers:
            num=str(bin(num))[2:]
            #print(num)
            l=len(num)
            if b<l and num[-b-1]=='1':
                counter+=1
        print(counter)
    else:
        new_numbers=[]
        for number in numbers:
            number+=b
            if number>65535:
                number-=65535
            new_numbers.append(number)
        numbers=new_numbers