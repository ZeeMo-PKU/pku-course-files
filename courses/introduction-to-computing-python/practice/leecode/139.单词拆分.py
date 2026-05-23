class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False] * (l + 1)
        dp[0] = True  # 空字符串可以被“拆分”为零个单词

        for i in range(1, l + 1):  # 遍历到 l，包括 l
            for j in range(i):  # j 从 0 到 i-1
                if dp[j] and (s[j:i] in wordDict):  # 检查 s[j:i] 是否在字典中
                    dp[i] = True
                    break  # 如果找到一个合适的分割，则停止内层循环

        return dp[l]  # 返回整个字符串是否可以被拆分