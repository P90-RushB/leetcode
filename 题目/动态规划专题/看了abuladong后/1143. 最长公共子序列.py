# 最长公共子序列
# dp[i][j] 表示str1的前i个字符与str2的前j个字符的最长公共子序列长度。
# 也就是说，每一个ij的组合，就是一个状态。
# 要求的最终状态下的值为dp[len(str1)-1][len(str2)-1]
# 状态转移方程：
# 如果当前遍历到的str1[i] == str2[j], 那么就加1，
# dp[i][j] = dp[i-1][j-1] + 1
# 如果str1[i] != str2[j]
# 要么i往后挪一位继续比，要么j往后挪一位继续比,
# 综上：
# dp[i][j] = dp[i-1][j-1] if str1[i] == str2[j]
# dp[i][j] = max(dp[i-1][j], dp[i][j-1]) if str1[i] != str2[j]

# 边界条件：
str[-1][j] = 0, str[i][-1] = 0  -1表示第0个字符，也就是空串。


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ######################## ver1 暴力递归 ###########################
        # 暴力递归，肯定超时了，但肯定要会。这样可以理解自顶向下。加个备忘录就能通过了。
        # n1 = len(text1)
        # n2 = len(text2)
        # # lcs 代表Longest Common Subsequence
        # # 暴力递归求解法。
        # def lcs(i, j):
        #     if i == -1 or j == -1:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return lcs(i-1, j-1) + 1
        #     else:
        #         return max(lcs(i-1, j), lcs(i, j-1))

        # return lcs(n1-1, n2-1)

        
        ####################### 用字典当备忘录 ###############################
        # n1 = len(text1)
        # n2 = len(text2)
        
        # bei = {}

        # def lcs(i, j):
        #     if i == -1 or j == -1:
        #         return 0
        #     if text1[i] == text2[j]:
        #         if (i-1, j-1) not in bei:
        #             bei[(i-1, j-1)] = lcs(i-1, j-1) 
        #         return bei[(i-1, j-1)] + 1
        #     else:
        #         if (i-1,j) not in bei:
        #             bei[(i-1,j)] = lcs(i-1, j)
        #         if (i,j-1) not in bei:
        #             bei[(i,j-1)] = lcs(i, j-1)
        #         return max(bei[(i-1,j)], bei[(i,j-1)])

        # return lcs(n1-1, n2-1)

############################# 动态规划 #######################
        n1 = len(text1)
        n2 = len(text2)
        # 参照 https://github.com/labuladong/fucking-algorithm/blob/master/动态规划系列/最长公共子序列.md
        # 由于边界条件是空字符串时，所以n1，n2都加了1. 后面的text1和text2的索引也相应减1
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        return dp[n1][n2]