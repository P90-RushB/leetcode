class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # ologn解法用到了二分，还没看，先跳过.
        # o（n^2）解法，用dp，类似于暴力搜索的两个for，
        # dp[i]表示以i结尾的最长上升序列的长度
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)