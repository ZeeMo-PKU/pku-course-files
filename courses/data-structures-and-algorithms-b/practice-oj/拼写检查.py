#判断函数
def yes_or_no(dic_word:str,x:str):
    # 不可能的
    if abs(len(x) - len(dic_word)) > 1:
        return 'No'

    # 替换
    elif len(x) == len(dic_word):
        n = 0
        len_word = len(x)
        for i in range(0, len_word):

            if x[i] == dic_word[i]:
                continue
            else:
                n += 1
                if n > 1:
                    return 'No'
        return 'Yes'

    # 删除&添加
    else:

        # # 删除
        # if len(x) - len(dic_word) == 1:
        #     l = len(dic_word)
        #     more = 0
        #
        #     for j in range(0, l):
        #
        #         if dic_word[j]==x[j+more]:
        #             continue
        #         else:
        #             more+=1
        #             if more > 1:
        #                 return 'No'
        #             if dic_word[j] != x[j + more]:
        #                 return 'No'
        #
        #     return 'Yes'
        #
        #
        # # 添加
        # else:
        #     if len(dic_word) - len(x) == 1:
        #         l = len(x)
        #         more = 0
        #
        #         for j in range(0, l):
        #
        #             if x[j] == dic_word[j + more]:
        #                 continue
        #             else:
        #                 more += 1
        #                 if more > 1:
        #                     return 'No'
        #                 if x[j] != dic_word[j + more]:
        #                     return 'No'
        #
        #         return 'Yes'
dic=[]
while True:
    word=input()
    if word=='#':
        break
    dic.append(word)

while True:
    x=input()
    if x=='#':
        break
    #出现
    if x in dic:
        print(f'{x} is correct')
        continue

    else:
        print(f'{x}:',end=' ')
        seem_word=[]
        for dic_word in dic:
            answer=yes_or_no(dic_word,x)
            if answer=='Yes':
                seem_word.append(dic_word)
        print(*seem_word)
