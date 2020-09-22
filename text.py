class Solution:
    def minSubArrayLen(self, s, nums):

        n = len(nums)
        cnt = float('inf')
        tmp_sum = 0
        tmp_cnt = 0

        for i in range(n):
            for j in range(i, n):
                tmp_sum += nums[j]
                tmp_cnt += 1
                if tmp_sum > s:
                    cnt = min(cnt, tmp_cnt)
                    break
            tmp_sum = 0
            tmp_cnt = 0
        if cnt == float('inf'):
            return 0
        return cnt

s = Solution()
res = s.minSubArrayLen(7, [2,3,1,2,4,3])
print(res)

                