第一道题斐波那契数列严格来说并不算动态规划题，因为没有涉及求最值，
只是演示dp算法设计螺旋上升的过程。下面这个凑零钱问题，一定要透彻掌握：

先看下题目：给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，每种硬币的数量无限，再给一个总金额 amount，
问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回 -1 。算法的函数签名如下：
// coins 中是可选硬币面值，amount 是目标金额
int coinChange(int[] coins, int amount);
比如说 k = 3，面值分别为 1，2，5，总金额 amount = 11。那么最少需要 3 枚硬币凑出，即 11 = 5 + 5 + 1。

###################### 重点 #######################
列出正确的状态转移方程？

1. 确定「状态」，也就是原问题和子问题中变化的变量。由于硬币数量无限，所以唯一的状态就是目标金额 amount。

2. 确定 dp 函数的定义：当前的目标金额是 n，至少需要 dp(n) 个硬币凑出该金额。

3. 确定「选择」并择优，也就是对于每个状态，可以做出什么选择改变当前状态。具体到这个问题，无论当的目标金额是多少，
    选择就是从面额列表 coins 中选择一个硬币，然后目标金额就会减少：

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 方法1， 暴力递归
        # 其实就是n叉树递归。 以amount为根节点，每次可以选择coins里的任意数值，
        # 到达下个状态。遍历n叉树，就可以统计出最少硬币个数。
        # if amount < 0:
        #     return -1
        # if amount == 0:
        #     return 0

        # res = float('inf')
        # for i in coins:
        #     tmp = self.coinChange(coins, amount - i)
        #     if tmp == -1:
        #         continue
        #     res = min(res, tmp+1)
        # return -1 if res == float('inf') else res

        # 方法二 ，暴力递归加个备忘录就行了
        # dic = {}
        # def helper(amount):
        #     if amount < 0:
        #         return -1
        #     if amount == 0:
        #         return 0
        #     res = float('inf')
        #     for i in coins:
        #         if amount - i not in dic:
        #             dic[amount - i] = helper(amount - i)
        #         tmp = dic[amount - i]
        #         if tmp == -1:
        #             continue
        #         res = min(res, tmp + 1)
        #     return -1 if res == float('inf') else res
        
        # return helper(amount)

        # 方法三，动归。 暴力递归解法其实就对应着状态转移方程：
        # if amount < 0: d[amount] = -1
        # elif amount == 0: dp[amount] = 0
        # else dp[amount] = min(dp[amount -i]) + 1 for i in coins
        if amount < 0:
            return -1
        elif amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i-j < 0:
                    continue
                dp[i] = min(dp[i-j] + 1, dp[i])
        return -1 if dp[amount] == float('inf') else dp[amount]





