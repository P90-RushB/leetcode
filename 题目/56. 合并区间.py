class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
         # 并不是重叠区间那种做法，那种是按end排序。
        # 合并区间，可以想成链子的每一环。 先按start排序，然后如果能连起来，就是一条链子上的，
        # 否则就是下一条新链子。
        if not intervals:
            return []
        intervals.sort(key= lambda x: x[0])
        res = [intervals[0]]
        for i in intervals:
            if i[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res 