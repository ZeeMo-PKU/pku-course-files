import sys
sys.setrecursionlimit(200000)  # 设置递归限制为10000
def strCmp(a,b) :
    if a == "" and b != "":
        return True
    elif a != "" and b == "":
        return False

    elif a == "" and b == "" :
        return False
    else:
        if abs(ord(a[0]) - ord('k')) < abs(ord(b[0]) - ord('k')):
            return True
        elif abs(ord(a[0]) - ord('k')) > abs(ord(b[0]) - ord('k')):
            return False
        else:
            return strCmp(a[1:], b[1:])
= int(input())
for _ in range(n):
    s1,s2 = input().split()
    if strCmp(s1,s2):
        print("YES")
    else:
        print("NO")