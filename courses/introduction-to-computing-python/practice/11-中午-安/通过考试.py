#pass
name=input()
a=int(input())
b=int(input())
c=int(input())
if a+b+c>=85*3:
    print(f'{name},congratulations!You performed well in the exam')
elif 60*3<=a+b+c<85*3:
    print(f'{name},you passed the exam')
else:
    print(f'{name}, sorry to inform you that you failed to pass the exam')