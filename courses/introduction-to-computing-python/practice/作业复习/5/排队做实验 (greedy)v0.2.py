n=int(input())
T=list(map(int,input().split()))
students=[]
for i in range(0,n):
    students.append((i+1,T[i]))
students.sort(key=lambda x:x[1])
time_sum=0
for i in range(0,n-1):
    time_sum+=students[i][1]*(n-i-1)
    print(students[i][0],end=' ')

print(students[-1][0])
print("{:.2f}".format(time_sum/n))