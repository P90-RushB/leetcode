class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        s_have = [0] * n
        s_no = [0] * n
        s_have[0] = -prices[0]
        s_no[0] = 0

        for i in range(1, n):
            s_have[i] = max(s_have[i-1], s_no[i-1] - (prices[i]))
            s_no[i] = max(s_no[i-1], s_have[i-1]+(prices[i]-fee))
        return max(s_have[n-1], s_no[n-1])
