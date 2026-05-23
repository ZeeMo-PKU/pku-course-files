# def f(k):
#     for i in range(1,9999999):
#         l_i=len(str(i))
#         qujianchangdu=0
#         for changdu in range(1,l_i):
#             qujianchangdu+=changdu*int('9'+'0'*(changdu-1))
#         qujianchangdu+=l_i*(i+1-int('1'+'0'*(l_i-1)))
#         kk=k-qujianchangdu
#         if kk<=0:
#             for l_n in range(0,999):
#                 kk=k-l_n*(int('9'+'0'*(l_n-1)))
#                 if kk<=0:
#                     shumu=k//l_n
#                     weizhi=k%l_n
#
#                     num=int('1'+'0'*(l_n-1))-1+shumu
#
#                     if weizhi==0:
#                         return str(num)[-1]
#                     else:
#                         return str(num+1)[weizhi-1]
#                 else:
#                     k=kk
#                     continue
#         else:
#             k=kk
#             continue
#
#
#
#
# t=int(input())
# for u in range(0,t):
#     k=int(input())
#     if k==1:
#         print(1)
#         continue
#     else:
#         print(f(k))
#

def f(k):
    l=0
    substring=""
    l_now=0
    for i in range(1,9999999999999):
        substring += str(i)
        l_now=len(str(substring))
        if l+l_now>=k:
            return substring[k-l-1]
        else:
            l+=l_now

t=int(input())
for u in range(0,t):
    k=int(input())
    if k==1:
        print(1)
        continue
    else:
        print(f(k))