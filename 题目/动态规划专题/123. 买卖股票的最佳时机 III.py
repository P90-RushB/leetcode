class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 这里我们需要两个递推公式来分别更新两个变量local和global
        # 定义local[i][j]为在到达第i天时最多可进行j次交易并且最后
        # 一次交易在最后一天卖出的最大利润，此为局部最优。
        # 定义global[i][j]为在到达第i天时最多可进行j次交易的最大利润，此为全局最优。
        # 递推式：

        # local[i][j] = max(global[i - 1][j - 1] + max(diff, 0), local[i - 1][j] + diff)
        # 局部最优值是比较前一天并少交易一次的全局最优加上大于0的差值，
        # 和前一天的局部最优加上差值中取较大值
        # 关于local[i][j],详细理解： local表明第i天必须卖，但这最后一笔是啥时候买的，有三种可能：
        #（1）今天买的，那当天买当天卖，利润就是0了，对应 global[i - 1][j - 1] + 0
        # (2) 昨天买的，那最后一笔利润就是今天减昨天（用diff表示），则该情况对应：global[i - 1][j - 1] + diff
        # (3) 更早之前买的，这种情况local[i][j]怎么算呢？一定要注意local表示第j天卖出最后一笔，
        # 那么可以利用j-1天卖出最后一笔 加上 第j天-第j-1天的差价（也就是diff，无论正负都要加）

        # global[i][j] = max(local[i][j], global[i - 1][j])
        # 全局最优比较局部最优和前一天的全局最优

        # 然后，上面思路理清了，边界条件还得看半天…… 真难

        n = len(prices)
        if n == 0:
            return 0
        g = [[0] * 3 for _ in range(n)]
        l = [[0] * 3 for _ in range(n)]

        for i in range(1, n):
            diff = prices[i] - prices[i-1]
            for j in range(1, 3):
                l[i][j] = max(g[i-1][j-1] + max(diff, 0), l[i-1][j] + diff)
                g[i][j] = max(l[i][j], g[i-1][j])
        return g[n-1][2]