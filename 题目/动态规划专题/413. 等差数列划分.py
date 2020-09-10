class Solution:
    # 这题可以看github上的解释：
    # dp[i] 表示以 A[i] 为结尾的等差递增子区间的个数。
# 当 A[i] - A[i-1] == A[i-1] - A[i-2]，那么 [A[i-2], A[i-1], A[i]] 
# 构成一个等差递增子区间。
# 而且在以 A[i-1] 为结尾的递增子区间的后面再加上一个 A[i]，
# 一样可以构成新的递增子区间。
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0

        dp = [0] * (len(A)-2)
        dp[0] = 1 if A[2] - A[1] == A[1] - A[0] else 0
        res = dp[0]
        for i in range(3, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i-2] = dp[i-2-1] + 1
            res += dp[i-2]
        return res