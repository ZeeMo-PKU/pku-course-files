n=int(input())
students=input()
students=numbers = [int(i) for i in students.split()]
out=[]
a=0
for j in range(0,n):
    out.append(students.index(min(students))+1)
    a+=(n-j-1)*students[students.index(min(students))]
    students[students.index(min(students))]=99999
print(*out)
out = f"{a / n:.2f}"
print(out)

