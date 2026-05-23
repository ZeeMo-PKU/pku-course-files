# Assign #3: Oct Mock Exam暨选做题目满百

Updated 1537 GMT+8 Oct 10, 2024

2024 fall, Complied by Hongfei Yan==（请改为同学的姓名、院系）==



**说明：**

1）Oct⽉考： AC6==（请改为同学的通过数）== 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/



思路：按照阿斯克码进行转换，如果超过范围，就减回去




代码
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
```python


```



代码运行截图 ==（至少包含有"Accepted"）==
"C:\Users\贾镕旭\Desktop\python1\作业图片库\1728736812132.jpg"




### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/



思路：切片，然后转化为整数型，比较简单的题



代码
a=input()
aa=int(a[0:2])
bb=int(a[4:6])
print(aa+bb)
```python


```



代码运行截图 ==（至少包含有"Accepted"）==
"C:\Users\贾镕旭\Desktop\python1\作业图片库\1728736919129.jpg"




### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/



思路：慢慢算，然后一个一个去判断



代码

```python
a=int(input())
for i in range(0,a):
    b=input()
    sum_=int(b[0])*7+int(b[1])*9+int(b[2])*10+int(b[3])*5+int(b[4])*8+int(b[5])*4+int(b[6])*2+int(b[7])*1+int(b[8])*6+int(b[9])*3+int(b[10])*7+int(b[11])*9+int(b[12])*10+int(b[13])*5+int(b[14])*8+int(b[15])*4+int(b[16])*2
    k=sum_%11
    if k==0 and b[-1]=='1':
        print('YES')
    elif k==1 and b[-1]=='0':
        print('YES')
    elif k==2 and b[-1]=='X':
        print('YES')
    elif k==3 and b[-1]=='9':
        print('YES')
    elif k == 4 and b[-1] == '8':
        print('YES')
    elif k==5 and b[-1]=='7':
        print('YES')
    elif k==6 and b[-1]=='6':
        print('YES')
    elif k==7 and b[-1]=='5':
        print('YES')
    elif k==8 and b[-1]=='4':
        print('YES')
    elif k==9 and b[-1]=='3':
        print('YES')
    elif k==10 and b[-1]=='2':
        print('YES')
    else:
        print('NO')


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

"C:\Users\贾镕旭\Desktop\python1\作业图片库\1728736997070.jpg"



### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/



思路：之前做过这个，所以考试的时候没用多长时间



代码

```python
a=int(input())
while True:
    if a==1:
        print('End')
        break
    elif a%2==1 and a>1:
        print(f'{a}*3+1={a*3+1}')
        a = a * 3 + 1
    else:
        print(f'{a}/2={int(a/2)}')
        a=int(a/2)

```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image.png)



### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/



思路：第一问简单，就是慢慢搞，第二问还是想了好久，然后转换思路



##### 代码

```python
# 
a=input()
if ord(a[0])<60:
    a=int(a)
    a1=a//1000
    print('M'*a1,end='')
    a2=(a//100)%10
    if a2==4:
        print('CD',end='')
    elif a2==9:
        print('CM',end='')
    elif a2<=3:
        print('C'*a2,end='')
    elif 4<a2<9:
        print('D', end='')
        print('C'*(a2-5),end='')
    a3=(a//10)%10
    if a3 == 4:
        print('XL', end='')
    elif a3 == 9:
        print('XC', end='')
    elif a3 <= 3:
        print('X' * a3,end='')
    elif 4 < a3 < 9:
        print('L', end='')
        print('X' * (a3- 5), end='')
    a4=a%10
    if a4== 4:
        print('IV', end='')
    elif a4== 9:
        print('IX', end='')
    elif a4<= 3:
        print('I' * a4, end='')
    elif 4 < a4< 9:
        print('V', end='')
        print('I' * (a4- 5), end='')
else:
    year=0
    k=list(a)
    for i in k:
        if i=='I':
            year+=1
        if i == 'V':
            year +=5
        if i == 'X':
            year +=10
        if i == 'L':
            year +=50
        if i == 'C':
            year +=100
        if i == 'D':
            year +=500
        if i == 'M':
            year +=1000
    if 'IV'in a:
        year-=2
    if 'IX' in a:
        year -=2
    if 'XL'in a:
        year-=20
    if 'XC'in a:
        year-=20
    if 'CD'in a:
        year-=200
    if 'CM'in a:
        year-=200
    print(year)
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==
"C:\Users\贾镕旭\Desktop\python1\作业图片库\1728737144465.jpg"




### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/



思路：太难了，要一个一个送到相应的位置，最后看的学长的代码



代码
N, D = map(int, input().split())
height = [0]*N
check = [False]*N
for i in range(N):
    height[i] = int(input())

height_new = []
while False in check:
    i, l = 0, len(height)
    buffer = []
    while i < l:
        if check[i]:
            i += 1
            continue
        if len(buffer) == 0:
            buffer.append(height[i])
            maxh = height[i]
            minh = height[i]
            check[i] = True
            continue

        maxh = max(height[i], maxh)
        minh = min(height[i], minh)
        if maxh-height[i] <= D and height[i]-minh <= D:
            buffer.append(height[i])
            check[i] = True
        i += 1
    buffer.sort()
    height_new.extend(buffer)

print(*height_new, sep='\n')
```python


```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![1728737275809.jpg](..%2F..%2F%E4%BD%9C%E4%B8%9A%E5%9B%BE%E7%89%87%E5%BA%93%2F1728737275809.jpg)"C:\Users\贾镕旭\Desktop\python1\作业图片库\1728737275809.jpg"



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

参加月考，做出来前四道题，第五题第二问陷进错误的思路费了我一个小时，希望之后考试的时候能避免这种一题两问的
最后就是排队这个题还是很难的，目前看语法已经差不多可以了，但是很多算法还是不会哎









