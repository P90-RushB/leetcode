class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 贪心，只要当前比前一天大，就加上。
        
        n = len(prices)
        if n < 2:
            return 0
        res = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res


        # 看了贪心，发现自己这个方法太麻烦了……
        # if not prices:
        #     return 0
        # if len(prices) == 1:
        #     return 0

        # # 如果一直涨,就不卖,到跌之前那天买.
        # # 如果一直跌,不买,直到涨之前的那一天买.
        
        # min_v = prices[0]
        # res = 0
        # prices.append(prices[-1]-1)
        # n = len(prices)
        # # 上一次的状态是在涨还是跌.
        # last_status = (prices[1] - prices[0]) > 0
        # for i in range(n-1):
        #     # 涨的情况
        #     if prices[i] <prices[i+1]:
        #         if last_status == 1:
        #             pass
        #         else:
        #             min_v = prices[i]
        #             last_status = 1
        #     else: # 跌的情况
        #         if last_status == 0:
        #             min_v = prices[i]
        #         else:
        #             res += prices[i] - min_v
        #             last_status = 0
        # return res