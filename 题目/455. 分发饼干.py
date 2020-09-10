class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(s)
        idx = 0
        cnt = 0
        for i in g:
            while idx < n and s[idx] < i:
                idx += 1
            if idx == n:
                return cnt
            else:
                cnt += 1
                idx += 1
        return cnt