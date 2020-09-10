class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # dp[i]表示以第i个元组为结尾，的最长长度
        # 状态转移方程 dp[i] = max(dp[i], dp[j]+1) 对所有的j < i 且满足j[1] < i[0]
        # 需要先排序，这样遍历到i时之前的情况都考虑过了，才行。
        # 而最令人疑惑的反而是，到底按第一个数还是第二个数来排？实际上，都可以。
        # 下面这个x[1]改成x[0]结果也是对的。
        # 为什么呢？按0还是1索引来排，只对一种情况有影响：
        # p[a,b] p[c,d] a<c<d<b,也就是p[c,d]区间完全在p[a,b]之内。
        # 那无论两者顺序如何，在代码if部分都判断不通过，两者不会有max比较，所以怎么排序都行。
        pairs.sort(key=lambda x:x[1])
        n = len(pairs)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)