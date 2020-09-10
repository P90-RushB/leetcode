class Solution:
    def rob(self, nums: List[int]) -> int:

    ###################### 方法一 ##################
        # 暴力递归。 把这种超时的方法写在前面，也是提醒自己，递归一定要会，
        # 如果一看题就会用dp，递归却写不出来，那根基太不稳了。
        # 递归思路：从第一家开始，要么偷要么不偷，不偷就递归到下家，偷的话就递归到下下家
        # 超时就对啦

        # # 递归1 写法非常简洁，来自labuladong
        # def helper(start):
        #     if start >= len(nums):
        #         return 0
        #     res = max(helper(start+1), nums[start] + helper(start+2))
        # return helper(0)

        # # 递归2，我写的，相较之下，冗长的多。这就是代码功底的差距啊。
        # def helper(i):
        #     if len(nums) == 0:
        #         return 0
        #     if i == len(nums) - 1:
        #         return nums[-1]
        #     if i == len(nums) - 2:
        #         return max(nums[-1], nums[-2])
            
        #     return max(helper(i+1), helper(i+2) + nums[i])

        # return helper(0)

    # 方法二 对递归加个备忘录
        memo = {}
        def helper(start):
            if start >= len(nums):
                return 0
            if start + 1 not in memo:
                memo[start+1] = helper(start+1)
            if start + 2 not in memo:
                memo[start+2] = helper(start + 2)
            
            return max(memo[start+1], nums[start] + memo[start+2])
        return helper(0)


#################### 方法三 dp ######################
        # d[i]  代表前i家能偷到的最高金额。
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        n = len(nums)
        if n == 0:
            return 0
        if n <=2:
            return max(nums)

        pre2 = nums[0]
        pre1 = max(nums[0], nums[1])
        res = 0
        for i in range(2, n):
            res = max(pre1, pre2 + nums[i])
            pre2 = pre1
            pre1 = res
        return res