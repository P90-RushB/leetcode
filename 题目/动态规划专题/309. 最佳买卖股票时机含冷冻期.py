class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划。把prices数组扫一遍，每天无非4种情况：买入、卖出、冷冻、啥也不干。
        # 用buy，sell，rest三个数组，
        # buy[i]表示截至到第i天，最后一个操作是买，到第i天的最大收益（注意，
        # 由于还有一个动作是啥也不干，所以不一定是第i天买。sell，rest也一样）
        # sell[i]表示截至到第i天，最后一个操作是卖，到第i天的最大收益。
        # rest[i]表示截至到第i天，最后一个操作是冷冻，到第i天的最大收益。
        # 那么，递归式：
        # buy[i] 等于： 截至i-1天最后操作是买并且第i天啥也不干 与 截至第i-1天
        # 最后操作是冷冻，并且第i天是买 两者最大值。
        # buy[i] = max(buy[i-1], rest[i-1] - prices[i])
        # 同样的道理，就好理解sell了。
        # sell[i] = max(sell[i-1], buy[i-1] + prices[i])

        # 我们还可以做进一步优化，由于i只依赖于i-1和i-2，
        # 所以我们可以在O(1)的空间复杂度完成算法，

        #pre_buy初始化为无穷小，是因为第一次算buy时，pre_buy要小于
        # pre_rest - price,毕竟买股票不能不花钱把……
        if len(prices) <= 1:
            return 0
        pre_buy, pre_sell, pre_rest = float('-inf'), 0, 0
        buy, sell, rest = None, None, None
        for i, price in enumerate(prices):
            buy = max(pre_buy, pre_rest - price)
            sell = max(pre_sell, pre_buy + price)
            rest = max(pre_rest, pre_sell)

            pre_buy = buy
            pre_sell = sell
            pre_rest = rest
        return max(buy, sell, rest)