class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 看的labuladong ， 暴力递归加备忘录

        # # 方法1 暴力递归
        # if not p:
        #     return not s

        # # . 可以匹配任意一个字符，可以出现在包括开头的任意位置，
        # # 而 *是
        # first = bool(s) and p[0] in {s[0], '.'}

        # # 如果发现了 *
        # if len(p) >= 2 and p[1] == '*':
        #     return self.isMatch(s, p[2:]) or \
        #             first and self.isMatch(s[1:], p)
        
        # else:
        #     return first and self.isMatch(s[1:], p[1:])

    # 方法2 暴力递归加备忘录
        memo = dict()
        def dp(i, j):
            if (i, j) in memo: return memo[(i,j)]
            if j == len(p): return i == len(s)

            first = i < len(s) and p[j] in {s[i], '.'}

            if j <= len(p) - 2 and p[j+1] == '*':
                ans = dp(i, j + 2) or first and dp(i + 1, j)
            
            else:
                ans = first and dp(i + 1, j + 1)
            
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)