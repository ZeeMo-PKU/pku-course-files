def print_story(n):
    if n == 0:
        print("讲你妹的故事啊！快点去睡觉！！！")
    else:
        print("从前有座山，山上有座庙")
        print("庙里有一个老和尚和一个小和尚")
        print("睡前老和尚给小和尚讲故事：")
        print_story(n - 1)  # 递归调用生成子故事
        print("然后老和尚和小和尚就睡觉啦")

# 读取输入
n = int(input())
print_story(n)