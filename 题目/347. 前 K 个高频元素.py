class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 还有一种解法用桶排序，还没看。

        # 只限制了时间复杂度，并没有限制空间，这里就可以：
        # 先用字典，得到每个数字出现的次数。
        # 然后用堆来解决前k大（最小堆），这里用到了python的堆的一个特性：
        # 当堆里存的是一个元组，是按照元组第一个元素排序的。
        dic = {}
        for i in nums:
            dic[i] = dic[i] + 1 if i in dic else 1
        
        import heapq
        h = []
        for i in dic.keys():
            if len(h) < k:
                heapq.heappush(h, (dic[i],i))
            elif dic[i] > h[0][0]:
                heapq.heapreplace(h, (dic[i], i))
        
        return [i[1] for i in h]