class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 贪心找出最多不重叠区间，剩下的就是要移除的最少数量。
        # 贪心的正确方法：对end从小到大排序，对每个区间，剔除（代码中为跳过，一样）与该
        # 区间重叠的区间，判断重叠的最简单方法：既然已经按end从小到大排列，
        # 如果区间i+t 与区间i重叠，那么区间i+t的start一定小于区间i的end。
        n = len(intervals)
        if n == 0:
            return 0
        
        intervals.sort(key=lambda x:x[1])
        # 第一个区间,至少已经有一个不重叠区间了。
        c = 1
        # 当前不重叠区间的索引。
        now = 0
        for i in range(n):
            # 言外之意， if intervals[i][0] < intervals[now][1],啥也不干，跳过。
            if intervals[i][0] >= intervals[now][1]:
                c += 1
                now = i

        return n - c