def isPalindrome(s, i, j):
    # 递归终止条件：当 i >= j 时，区间内只有一个字符或没有字符，一定是回文的
    if i >= j:
        return True
    # 如果两端的字符相等，继续判断中间部分是否是回文的
    return s[i] == s[j] and isPalindrome(s, i + 1, j - 1)

def main():
    s = input().strip()
    # 调用递归函数判断整个字符串是否是回文的
    if isPalindrome(s, 0, len(s) - 1):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()