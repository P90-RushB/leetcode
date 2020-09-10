class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 该题让重组队列，使得满足两个条件。
        # 方法一，用到额外空间，思路很简单
        # 首先，按照身高由大到小，同一身高的由小到大排序
        queue = []
        height_groups = defaultdict(list)

        for height, in_front in people:
            height_groups[height].append(in_front)

        all_heights = list(height_groups.keys())
        all_heights.sort(reverse=True)
        for height in all_heights:
            height_groups[height].sort()
            for in_front in height_groups[height]:
                queue.insert(in_front, [height,in_front])
        return queue