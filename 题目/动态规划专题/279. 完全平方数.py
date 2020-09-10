
class Solution:
    def numSquares(self, n: int) -> int:
        # if n <= 2:
        #     return n
        # dp[i]表示正整数i的最少的组成完全平方数的个数。
        # 对数字n，用j，遍历1到n，
        # 如果j**2是完全平方数，那么j**2有可能是组成结果的数之一。
        # 用j**2 + dp[i-j]来更新dp[i]
        # dp = [-1] * (n + 1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     for j in range(1, int(i**0.5)+1):
        #         if j **2 == i:
        #             dp[i] = 1
        #             break

        #         dp[i] = min(dp[i], dp[i-j**2] + 1) 
        
        # dp 超时，要用公式算……
        # 我上面写的dp也是对的，也是超时。
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(n):
            j = 1
            while i + j**2 <= n:
                dp[i + j**2] = min(dp[i + j**2], dp[i] + 1)
                j += 1
        return dp[n]
        
