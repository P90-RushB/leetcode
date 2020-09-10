动态规划题：
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        # 初始化结果
        res = 0
        # 最小最大股价都初始化为第一天股价
        min_v = prices[0]
        max_v = prices[0]
        # 遍历
        for i in prices:
            # 如果今天股价大于之前的最小股价,那至少说明能赚钱了
            if i >= min_v:
                # 如果当前股价大于了自最小股价到今天之前的最大股价,那说明真的可以更赚了
                # (否则,如果max_v更大,那就不用更新了)
                if max_v < i:
                    max_v = i
                    # 更新最大利润
                    res = max(res, max_v - min_v)

            # 如果今天股价比之前最小股价还低,那就更新min_v为今天的
            # 这里刚开始可能有点迷糊,只要记清楚,例如:
            # 第1天股票3快,第5天股价2块,那如果最高股价在1-5天之内,已经更新在res里了,
            # 而如果最高股价在第五天之后,最高股价-2 当然大于最高股价减3,也就是和第5天之前永远          # 没关系.
            else:
                min_v = i
                max_v = min_v
        return res

        # 简洁写法
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # 遍历，记录到当前为止的res值和到当前为止的最低谷
#         if len(prices) <= 1:
#             return 0

#         res = 0
#         lower = prices[0]
#         for i in prices[1:]:
#             res = max(res, i - lower)
#             if i < lower: lower = i
#         return res
