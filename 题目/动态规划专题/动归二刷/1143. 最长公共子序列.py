class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 方法一， 暴力递归(超时)
        # dp 两个参数表示两个字符串的end索引。
        # def dp(i, j):
        #     if i == -1 or j == -1:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return dp(i-1, j-1) + 1
        #     else:
        #         return max(dp(i-1, j), dp(i, j-1))

        # return dp(len(text1)-1, len(text2)-1)

        # 方法二 递归加备忘录
        # memo = {}
        # def dp(i, j):
        #     if i == -1 or j == -1:
        #         return 0
        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     if text1[i] == text2[j]:
        #         memo[(i, j)] = dp(i-1, j-1) + 1
        #     else:
        #         memo[(i, j)] = max(dp(i-1, j), dp(i, j-1))
        #     return memo[(i, j)]

        # return dp(len(text1)-1, len(text2)-1)

        # 方法三 动态规划 
        # 可以从递归式看出，当前dp[i][j]下的结果，只和dp[i-1][j], dp[i][j-1],
        # dp[(i-1, j-1)]有关。
        m = len(text1)
        n = len(text2)

        if m == 0 or n == 0:
            return 0

        array_last = [0] * (m + 1)
        array_now = [0] * (m + 1)

        # 对于这个二维dp矩阵，我的遍历方式是一行一行遍历，只保存相邻两行的结果。
        # 我的这个写法里，text1是行，text1有m个字符，则就有m列。
        for i in range(1, n+1):
            for j in range(1, m+1):
                # 注意，这里的i-1， j-1 只是因为i，j是属于dp矩阵，dp矩阵左边和上边
                # 是多加了一列和一行0的，所以要-1才是text的真实索引。
                if text2[i-1] == text1[j-1]:
                    array_now[j] = array_last[j-1] + 1
                else:
                    array_now[j] = max(array_now[j-1], array_last[j])
            
            # 这里其实并不需要copy，可以直接赋值。直接赋值后两者引用了同一数组，
            # 但在下一句array_now 引用到了一个新建的数组，就和array_last不同了。
            # python的这个特性要牢记。
            # array_last = copy(array_now)
            array_last = array_now
            array_now = [0] * (m+1)
        return array_last[-1]

    # 动归版本二， 建立完整的dp二维数组，这样空间上不如我上面写的高效。
    # 实际测试，时间空间都比上面的写法低了10%。当然，都比备忘录快的多。
    # 这是labuladong里贴的代码：
        # m, n = len(text1), len(text2)
        # # 构建 DP table 和 base case
        # dp = [[0] * (n + 1) for _ in range(m + 1)]
        # # 进行状态转移
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if text1[i - 1] == text2[j - 1]:
        #             # 找到一个 lcs 中的字符
        #             dp[i][j] = 1 + dp[i-1][j-1]
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
        # return dp[-1][-1]


