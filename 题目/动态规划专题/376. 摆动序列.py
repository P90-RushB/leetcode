class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 还是没想出来，看的博客。
        n = len(nums)
        if n == 0: return 0
        p = [1] * n
        q = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    p[i] = max(p[i], q[j] + 1)
                elif nums[i] < nums[j]:
                    q[i] = max(q[i], p[j] + 1)
        return max(p[-1], q[-1])
