class Solution:
    # 看博客。
    # 这题虽然不好想，但与198打家劫舍1相比，并没有方法上的不同，都是普通的
    # 动态规划，这题不同在于要想到怎么处理循环：可以取max（0到n-2， 1到n-1）
    # 就变成了打家劫舍1的题，没有了循环。
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=1:
            return 0 if len(nums) == 0 else nums[0]
        
        # 打家劫舍1 题目的方法
        def rob_no_circle(i, j):
            # dp[n] = max(dp[n-1], dp[n-2]+nums[n])
            if j - i == 0:
                return nums[i]
            if j - i == 1:
                return max(nums[i], nums[j])
            count = j - i + 1
            front1 = nums[i]
            front2 = max(nums[i], nums[i+1])
            res = None
            # 这里的2代表从i到j数组的第三个位置,从第三个位置开始，算递推式。
            for k in range(2+i, count+i):
                res = max(front1 + nums[k], front2)
                front1 = front2
                front2 = res
            return res

        return max(rob_no_circle(0,len(nums)-2), rob_no_circle(1, len(nums)-1))