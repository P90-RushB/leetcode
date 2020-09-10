class Solution:
    # （也可以用bfs来做），这题是一个标准的动态规划题，而且有助于理解强化学习
    # 思路：建立一个与grid同样大小的二维数组
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        v_array = [[0] * n for _ in range(m)]

        v_array[0][0] = grid[0][0]

        for i in range(1, n):
            v_array[0][i] = grid[0][i] + v_array[0][i-1]
        
        for i in range(1, m):
            v_array[i][0] = grid[i][0] + v_array[i-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                v_array[i][j] = min(v_array[i-1][j], v_array[i][j-1]) + grid[i][j]
        return v_array[m-1][n-1]