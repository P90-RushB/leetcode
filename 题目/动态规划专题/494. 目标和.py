class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 我写的递归，是对的，但是超时。应该用动态规划……
        cnt = 0
        n = len(nums)

        def helper(start_idx, S):
            nonlocal cnt
            if start_idx == n-1:
                # 这里正负都加1，这是因为如果最后一个数是0，+-0都可以。
                if -nums[start_idx] == S:
                    cnt += 1
                if nums[start_idx] == S:
                    cnt += 1
            else:
                helper(start_idx+1, S - nums[start_idx])
                helper(start_idx+1, S + nums[start_idx])
        helper(0, S)
        return cnt