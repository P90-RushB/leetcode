class Solution:
    # 就是用堆，完事。
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = dic[i] + 1 if i in dic else 1
        
        import heapq
        h = []
        for i in dic.keys():
            heapq.heappush(h, (dic[i], i))
        res = ''
        n = len(h)
        for _ in range(n):
            tmp = heapq.heappop(h)
            res = tmp[1] * tmp[0] + res
        return res