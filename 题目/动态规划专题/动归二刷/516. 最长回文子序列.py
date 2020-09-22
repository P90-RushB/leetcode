class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 求最值，考虑用动态规划。
        # 首先，如果不用动态规划，暴力递归，会怎么做？ 每个字符都可以要也可以不要，
        # 总共有2的n次方个组合，对每个组合判断是否是回文，当然，这计算量简直开玩笑。
        # 从递归思路可以看出，有很多重复计算（很多子回文序列的判断）。
        # 实际上，对于这种回文问题，一般用双指针，dp定义为一个二维数组。
        # dp[i][j]表示i到j索引的子串包含的最长回文子序列的长度。

        # if (s[i] == s[j])
        #     // 它俩一定在最长回文子序列中
        #     dp[i][j] = dp[i + 1][j - 1] + 2;
        # else
        #     // s[i+1..j] 和 s[i..j-1] 谁的回文子序列更长？
        #     dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]);

        # 边界：对角线，长度1. 
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        for j in range(n):
            right = -1
            for i in range(n-j):
                right += 1
                if i == j + right:
                    continue
                if s[i] == s[j+right]:
                    dp[i][j+right] = dp[i+1][j+right-1] + 2
                else:
                    dp[i][j+right] = max(dp[i+1][j+right], dp[i][j+right-1])

        return dp[0][n-1]

# 二刷，不是斜着遍历的那种：
        if not s:
            return 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # 只有一个字符，回文长度为1， 这是边界之一。
        # 另一个边界是： i 小于 j， 不合法，最大长度为0。
        for i in range(n):
            dp[i][i] = 1

        for i in reversed(range(n-1)):
            for j in range( i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]