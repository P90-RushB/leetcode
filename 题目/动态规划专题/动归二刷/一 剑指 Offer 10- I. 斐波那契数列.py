class Solution:
    def fib(self, n: int) -> int:

        # 重叠子问题: 算fib(n)时,子问题fib(n-i)会重复计算很多次.

        # 方法一:暴力递归，超时
        # if n <= 1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)

        # 方法二:加备忘录
        # dic = {}
        # def helper(m):
        #     if m <= 1:
        #         return m
        #     if m in dic:
        #         return dic[m]
        #     dic[m] = (helper(m-1) + helper(m-2)) % 1000000007
        #     return dic[m]
        # return helper(n)

        # 方法三, 动归
        # 重叠子问题: 算fib(n)时,子问题fib(n-i)会重复计算很多次.
        # 状态转移方程：fib(n) = n if n <= 1 else fib(n-1) + fib(n-2)
        if n <= 1:
            return n
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, (a + b) % 1000000007
        return b
            


