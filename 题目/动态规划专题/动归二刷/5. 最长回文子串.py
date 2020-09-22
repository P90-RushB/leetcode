class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 方法1， 中心扩散
        # 中间两个数和中间一个数的回文，可以合并成一个函数，但做的时候是分开的，思路清晰。
        n = len(s)
        if n == 0:
            return ''
        res = (0, 0)

        def max_midone():
            res = (0, 0)
            for i in range(n):
                
                pianyi = 0
                while True:
                    if i-pianyi < 0 or i + pianyi >= n:
                        pianyi -= 1
                        break
                    if s[i-pianyi] != s[i+pianyi]:
                        pianyi -= 1
                        break

                    pianyi += 1
                    
                res = (i-pianyi, i+pianyi) if pianyi*2 > res[1]-res[0] else res
            return res

        res = max_midone()

        def max_midtwo():
            res = (0, 0)
            for i in range(n):
                pianyi = 0
                while True:
                    if i - pianyi < 0 or i + 1 + pianyi >= n:
                        pianyi -= 1
                        break
                    if s[i-pianyi] != s[i+1+pianyi]:
                        pianyi -= 1
                        break
                    pianyi += 1
                res = (i-pianyi, i+1+pianyi) if pianyi*2+1 > res[1] - res[0] else res
            return res

        res_new = max_midtwo()
        # 这里的 +1 只是因为 要取到元祖的第二个数那个索引
        return s[res[0]: res[1]+1] if res_new[1] - res_new[0] < res[1] - res[0] else \
                s[res_new[0]: res_new[1]+1] 


######################## 方法二 ##############################

# 废了老大劲了，终于算是自己写出来了哈哈。写出状态转移方程，会发现
# dp是一个二维矩阵，对角线右上部分才可能为true（i<j），每个状态依赖于
# 左，下，左下三个状态。 边界有两种情况：1.对角线：一定True. 2. 
# 
    # 动归 
    # 定义 dp[i,j] 字符串s中 i到j是否是回文字串（注意，不是子串）(包括j)。
    # 因为最后要的是最长串而不是其长度，所以dp不能定义成
    # i，j间的最长子串的长度。
    # 求出dp后，看dp[i,j]为true的j-i最大的，就是结果。
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        # 因为i <= j 所以只有矩阵的一个对角是有可能true的
        # 状态转移方程：if s[i] == s[j]: dp[i,j] = True if dp[i+1, j-1] == True else False
        #              elif s[i] != s[j]: dp[i,j] = False
        # 画个图就看出来，遍历是从对角线的每个元素开始，沿右上方遍历。
        # 从对角线的每个元素开始：
        for j in range(n):
            right = -1
            for i in range(0, n-j):
                right += 1
                if i == j+right:
                    continue
                
                if s[i] != s[j+right]:
                    pass
                    # if dp[i][j+right-1] or dp[i+1][j+right]:
                    #     dp[i][j+right] = True
                else:
                    if i+1 == j + right:
                        dp[i][j+right] = True

                    elif dp[i+1][j+right-1]:
                        dp[i][j+right] = True

        res = (0, 0)
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j] and j-i > res[1] - res[0]:
                    res = (i, j)
        return s[res[0]: res[1]+1]  

# 我又做的一次：
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 方法1， 中心扩散
        # n = len(s)
        # if n == 0:
        #     return ''
        # res = (0, 0)

        # def max_midone():
        #     res = (0, 0)
        #     for i in range(n):
                
        #         pianyi = 0
        #         while True:
        #             if i-pianyi < 0 or i + pianyi >= n:
        #                 pianyi -= 1
        #                 break
        #             if s[i-pianyi] != s[i+pianyi]:
        #                 pianyi -= 1
        #                 break

        #             pianyi += 1
                    
        #         res = (i-pianyi, i+pianyi) if pianyi*2 > res[1]-res[0] else res
        #     return res

        # res = max_midone()

        # def max_midtwo():
        #     res = (0, 0)
        #     for i in range(n):
        #         pianyi = 0
        #         while True:
        #             if i - pianyi < 0 or i + 1 + pianyi >= n:
        #                 pianyi -= 1
        #                 break
        #             if s[i-pianyi] != s[i+1+pianyi]:
        #                 pianyi -= 1
        #                 break
        #             pianyi += 1
        #         res = (i-pianyi, i+1+pianyi) if pianyi*2+1 > res[1] - res[0] else res
        #     return res

        # res_new = max_midtwo()
        # # 这里的 +1 只是因为 要取到元祖的第二个数那个索引
        # return s[res[0]: res[1]+1] if res_new[1] - res_new[0] < res[1] - res[0] else \
        #         s[res_new[0]: res_new[1]+1]

    # 方法二 dp
    # s中，索引i到j的子串是否是回文。这就是一个二维的dp了。因为i<=j,所以只有右上角可能为True.
    # 状态转移方程： dp[i][j] = True if s[i] == s[j] and dp[i+1]dp[j-1] == True
    # 边界：当s == 1 或 2 时，直接判断是不是回文。
        if not s:
            return ''
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        # 对角线为True，对应:一个字符是回文。
        for i in range(n):
            dp[i][i] = True
        # 对角线上面那条斜线的判断，对应：相邻两个字符，如果相等，是回文。
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True

        # dp的遍历方向，可以每次斜着遍历，逐渐向上，但是写起来比较麻烦。
        # 因此我用另一种遍历方式：从最后一行到第一行：对每一行，从左往右。
        for i in reversed(range(n-2)):
            for j in range(i+2, n):
                dp[i][j] = True if s[i] == s[j] and dp[i+1][j-1] else False
    
        max_dis = 0
        res = ''
        for i in range(n):
            for j in range(i, n):
                if j-i >= max_dis and dp[i][j]:
                    max_dis = j-i
                    res = s[i:j+1]
        return res