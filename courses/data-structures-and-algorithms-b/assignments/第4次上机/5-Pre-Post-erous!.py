import math
#组合数计算
def C(m,n):
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))
#递归函数
def f(m,pre,post):
    l=len(pre)
    root_node=pre[0]
    #递归终点
    if l==1:
        return 1
    #进行递归
    ans=1
    child_tree=[]

    child_tree_pre_start_index=1
    child_tree_post_start_index=0
    while child_tree_pre_start_index<l:
        root=pre[child_tree_pre_start_index]
        chile_tree_root_post_index=post.index(root)
        len_child_tree=chile_tree_root_post_index-child_tree_post_start_index+1
        child_tree_pre=pre[child_tree_pre_start_index:child_tree_pre_start_index+len_child_tree]
        child_tree_post=post[child_tree_post_start_index:child_tree_post_start_index+len_child_tree]
        child_tree.append(f(m,child_tree_pre,child_tree_post))
        child_tree_pre_start_index+=len_child_tree
        child_tree_post_start_index=chile_tree_root_post_index+1


    #答案
    for chile in child_tree:
        ans*=chile
    ans*=math.comb(m, len(child_tree))
    return ans

#主程序
while True:
    x=input()
    if x[0]=='0':
        break
    else:
        m,pre,post=x.split()
        m=int(m)
        print(f(m,pre,post))
