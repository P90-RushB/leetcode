#################### 该题更好的方式是线段树 ############
# 线段树讲解 视频： https://www.bilibili.com/video/av47331849?t=1907


# 动归
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # 我写的主要是看到题之后的思路
        # 首先，求最值，就很有可能要用动态规划。
        # 先想想，如果不用动态规划，暴力解决要怎么做：
        # 遍历每个数字，对每个数字，再从该数字开始遍历，照递增子序列，后面每个数字，
        # 如果是增的，就可以加，也可以不加，这样复杂度其实是指数级的，肯定不行。
        # 暴力解法里明显有重叠子问题。
        # 那么如果用动态规划，
        # 第一步：确定 状态是什么：就是以某个节点为结尾的最长递增序列， 状态维度为1
        # 所以dp数组的定义就是 dp[i]： 以i节点结尾的最长递增序列
        # 第二步: 明确选择是什么： dp[i] = max(dp[j] 与 num[i]组成的递增序列长度) 0<=j<i
        # 这也就是状态转移方程
        # 第三步： 明确base case是什么：i == 0时，dp[i] = nums[i]
        
        n = len(nums)
        if n == 0:
            return 0
        
        # dp[i] 是一个元祖（m,n）表示以i结尾的最长序列长度为m，个数为n个
        dp = [(1,1)] * n
        for i in range(n):
            if i == 0:
                dp[i] = (1, 1)
            else:
                longest = 1
                for j in range(i):
                    if nums[j] < nums[i]:
                        if dp[i][0] < dp[j][0] + 1:
                            dp[i] = (dp[j][0] + 1, dp[j][1])
                        elif dp[i][0] == dp[j][0] + 1:
                            dp[i] = (dp[i][0], dp[i][1] + dp[j][1])
                        else:
                            pass
        longest = max(dp)
        cnt = 0
        for i in dp:
            if longest[0] == i[0]:
                cnt += i[1]
        return cnt
