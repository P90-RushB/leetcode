class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 动态规划
        # 用dp[i,j]代表到达i，j点的路径数。
        # 对于第一行和第一列，只能分别往右走和往下走，都只有一条路径
        # 即 dp[0][:] == 1   dp[:][0] == 1
        # 剩下的格子，用dp[i,j] = dp[i][j-1] + dp[i-1][j]
        # 这题当然可以在空间上再优化，懒得搞了。
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]