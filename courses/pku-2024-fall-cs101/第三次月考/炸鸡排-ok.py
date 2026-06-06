n,guo=map(int,input().split())
list_jipai=list(map(int,input().split()))
list_jipai.sort()

def f(list_jipai,n,guo):
    if guo==1:
        return sum(list_jipai)
    time_max_jipai=list_jipai.pop(-1)

    if time_max_jipai>sum(list_jipai)/(guo-1):
        return f(list_jipai,n-1,guo-1)

    else:
        return (sum(list_jipai)+time_max_jipai)/guo

print(f"{f(list_jipai,n,guo):.3f}")