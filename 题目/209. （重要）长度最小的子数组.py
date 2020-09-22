class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 方法一，暴力循环。on2
        # n = len(nums)
        # cnt = float('inf')
        # tmp_sum = 0
        # tmp_cnt = 0

        # for i in range(n):
        #     for j in range(i, n):
        #         tmp_sum += nums[j]
        #         tmp_cnt += 1
        #         if tmp_sum >= s:
        #             cnt = min(cnt, tmp_cnt)
        #             break
        #     tmp_sum = 0
        #     tmp_cnt = 0
        # if cnt == float('inf'):
        #     return 0
        # return cnt

    # 方法二双指针
        n = len(nums)
        if not nums:
            return 0
        
        slow, fast = 0, 0
        res = 0
        cnt = float('inf')

        while res < s and fast < n:
            res += nums[fast]
            while res >= s and slow <= fast:
                res -= nums[slow]
                cnt = min(cnt, fast - slow + 1)
                slow += 1
            fast += 1
        return 0 if cnt == float('inf') else cnt