# 竟然并没有什么更巧妙的解法，就是记录为0的坐标，然后清零就完了，折算不上中等啊……
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先暴力
        if not len(matrix) or not len(matrix[0]):
            return
        m = len(matrix)
        n = len(matrix[0])
        res = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    res.append((i,j))
        for t in res:
            for p in range(m):
                matrix[p][t[1]] = 0
            for q in range(n):
                matrix[t[0]][q] = 0

        return 