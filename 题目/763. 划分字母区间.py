class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # 思路很巧妙，还得看 博客。
        res = []
        n = len(S)
        start = 0
        last = 0
        dic = {}
        for i in range(n):
            dic[S[i]] = i

        for i in range(n):
            last = max(last, dic[S[i]])
            if i == last:
                res.append(i - start + 1)
                start = i + 1
        return res