class Solution:
    def waysToChange(self, n: int) -> int:

################### 这是我写的时候的思路：回溯，毕竟是暴力，超时了。应该dp #################
################### 属于dp里的背包问题 ###########################

        # 该题不同于找最少硬币数，求最值可以用动态规划，
        # 而该题要求所有的表示法，那就是回溯了，也就是n叉树遍历。
        # 而且是回溯里的组合问题。
        actions = [1, 5, 10, 25]
        # 因为是组合，这里可以仿照组合的写法，这里每次加的硬币只能更小
        # 因为大不了用1个硬币就能凑整。
        cnt = 0
        def backtrack(m, last_coin):
            nonlocal cnt
            if m < 0:
                return 
            elif m == 0:
                cnt += 1
                return 

            for i in actions:
                if i > m or i > last_coin:
                    continue
                
                backtrack(m-i, i)
        backtrack(n, 25)
        return cnt
###################################################################