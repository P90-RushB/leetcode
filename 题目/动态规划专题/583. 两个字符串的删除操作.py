class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 看博客才明白，还要复习 
        # 这道题给了我们两个单词，问我们最少需要多少步可以让两个单词相等，每一步我们可以在任意一个单词中删掉一个字符。那么我们分析怎么能让步数最少呢，是不是知道两个单词最长的相同子序列的长度，并乘以2，被两个单词的长度之和减，就是最少步数了。其实这道题就转换成求Longest Common Subsequence最长相同子序列的问题，
        # 定义一个二维的dp数组，其中dp[i][j]表示word1的前i个字符和word2的前j个字符组成的两个         #  单词的最长公共子序列的长度
        # dp[i][j] = dp[i][j-1]
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return n1 + n2 - 2 * dp[n1][n2]
    
s = Solution()
res = s.minDistance('sea', 'eta')
print(res)