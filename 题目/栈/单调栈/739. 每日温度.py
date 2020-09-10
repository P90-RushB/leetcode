class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
    # 单调栈解法 找最近的最大/最小值，很适合用单调栈来解决。
    # 跟模板的区别仅仅在于，因为这题要返回的列表存的是相对位置，在
    # 单调栈中应该存的是最近的更大值的索引而不是数值……
        n = len(T)
        res = [0] * n
        s = []
        for i in range(n-1, -1, -1):
            while s and T[s[-1]] <= T[i]:
                s.pop()
            if s:
                res[i] = s[-1] - i
            s.append(i)
        return res