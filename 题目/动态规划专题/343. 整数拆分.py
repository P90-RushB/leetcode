class Solution:
    def integerBreak(self, n: int) -> int:
        # 看博客，方法1
        # dp[i]表示数字i拆分为至少两个正整数之和的最大乘积
        # 最基本情况是i=1时，等于1，i=2时，只能拆成1+1，dp[2]也是1.
        dp = [1] * (n+1)
        # 对于3到n，有如下递推式
        # dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
        # 外层的max就是在不断更新dp[i]的值，更新的依据就是第二个式子：
        # max(j * (i - j), j * dp[i - j]),
        # 这个式子应该整体理解：内层for是遍历1到i，则因为i要拆分，则肯定有j会作为拆分的
        # 一个数，当拆分出j后，剩下的数要么不拆分：对应j * (i - j),
        # 要么对剩下的i-j继续拆分，对应j * dp[i - j]，这就包含了所有情况。
        #举个例子，当i - j = 2， 2 就不应该继续拆分，因为2 > 1* 1
        for i in range(3, n+1):
            for j in range(1, i):

                # 正确
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))
                # 下面注释掉的就是错的了。
                dp[i] = max(dp[i], j * dp[i - j])
                
        return dp[n]
            