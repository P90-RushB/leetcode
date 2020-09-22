# 官方题解的方法一比较简单，我没想到…… 当然，也不太高效。 
# 思路是不反转，就斜着遍历，然后再隔行，翻转子数组。

# 下面是我的思路，和官方题解二一样，按照遍历顺序模拟出来。
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        # 看路径图就想出来了。
        # 首先，分成两种情况，超左下 和朝右上。
        # 当朝左下时，如果下个元素为空，就空元素位置的右边；如果还空，就右上角元素。
        # 当沿着右上或者左下遇到空，就准备反向了
        # 当朝右上时，如果遇到空，先向下，如果还空，就左下角元素。

        # 两个方向交替进行。

        if not matrix or not matrix[0]:
            return 
        m = len(matrix)
        n = len(matrix[0])

        i, j = 0, 0
        res = []

        def isnone(a, b):
            if a < 0 or a >=m or b < 0 or b >= n:
                return True
            return False

        up_right = True
        while True:
            if  not isnone(i,j):
                res.append(matrix[i][j])
                if up_right:
                    i -= 1
                    j += 1
                else:
                    i += 1
                    j -= 1
            else:
                if up_right:
                    i += 1
                    if isnone(i, j):
                        i+=1
                        j-=1
                        if isnone(i,j):
                            return res
                    up_right = not up_right
                else:
                    j += 1
                    if isnone(i,j):
                        i -= 1
                        j += 1
                        if isnone(i, j):
                            return res
                    up_right = not up_right

