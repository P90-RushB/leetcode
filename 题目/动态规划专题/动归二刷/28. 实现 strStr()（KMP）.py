class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 竟然标了个简单，果然暴力搜索也过了…… 但这算啥，肯定要用kmp啊

        # # 方法1 暴力搜索
        # m = len(haystack)
        # n = len(needle)
        # if n == 0:
        #     return 0
        # if m < n:
        #     return -1


        # for i in range(m-n+1):
        #     for j in range(n):
        #         if haystack[i + j] != needle[j]:
        #             break
        #         if j == n-1:
        #             return i
        # return -1

        # 方法二 kmp（用动态规划的思想）
        # 我懒得看kmp的常见理解，labuladong的kmp一节写的很好，把kmp当成
        # 动态规划来做。
        # 先根据模式串，计算出dp数组，然后根据dp数组来匹配就行。
        m = len(haystack)
        n = len(needle)

        if n == 0:
            return 0
        if m < n:
            return -1
            
        # dp数组只用到模式串needle
        # dp[i][j] 表示当处于模式串的第i个状态，并且下一个来的字符是0-256 ascii
        # 码的第j个字符，应该转到哪个状态
        dp = [[0] * 256 for _ in range(n)]
        
        def compute_dp():
            dp[0][ord(needle[0])] = 1
            x = 0
            for i in range(1, n):
                for c in range(256):
                    if c == ord(needle[i]):
                        dp[i][c] = i + 1
                    else:
                        dp[i][c] = dp[x][c]
                x = dp[x][ord(needle[i])]
        
        compute_dp()

        j = 0
        for i in range(m):
            j = dp[j][ord(haystack[i])]
            if (j == n):
                return i - n + 1
        return -1

s = Solution()
res = s.strStr('hello', 'll')
print(res)
