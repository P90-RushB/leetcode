class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 简单，一行一行来。
        if numRows == 0:
            return []
        pre = [1]
        res = [pre]
        for i in range(1, numRows):
            now = [1] * (len(pre) + 1)
            for j in range(1, len(now)-1):
                now[j] = pre[j-1] + pre[j]
            res.append(now)
            pre = now
        return res

# 方法2 递归
        # 方法1， 递归
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        res = self.generate(numRows-1)
        tmp = [1] * numRows
        for i in range(1, numRows-1):
            tmp[i] = res[numRows-2][i-1] + res[numRows-2][i]
        res.append(tmp)

        return res
