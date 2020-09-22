class Solution:
    # 我竟然硬磕出了这道题，微软一个面试题。 不过花的时间挺久……
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        inter = 0
        while n//2 - inter >= 0:
            # 这里的减一，是因为不需要遍历到n，因为末尾的n是竖着看的0， 已经交换过了。
            for i in range(inter, n-inter-1):
                tmp = matrix[inter][i]

                tmp, matrix[i][n-1-inter] = matrix[i][n-1-inter], tmp 

                tmp, matrix[n-1-inter][n-1-i] = matrix[n-1-inter][n-1-i], tmp

                tmp, matrix[n-1-i][inter] = matrix[n-1-i][inter], tmp

                tmp, matrix[inter][i] = matrix[inter][i], tmp

            inter += 1