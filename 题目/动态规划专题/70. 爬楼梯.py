# 爬楼梯可算是我第一次正式了解动态规划的题。
# 递归和动态规划都是将原问题拆成多个子问题然后求解，他们之间最本质的区别是，动态规划保存了子问题的解，避免重复计算。
# 在空间上略微弱于动态规划，但比普通递归强的多的是在普通递归的基础上加上
# 备忘录（用一个字典来记录已经计算过的值，避免重复计算）

class Solution:
    def climbStairs(self, n: int) -> int:
        # 到n阶的可能数 = 到n-1阶的可能数（再加1台阶，可能数不变） + 到n-2阶的可能数（再加2台阶，可能数不变）
        if n == 1:
            return 1
        if n == 2:
            return 2

        # 如果用递归，在n=38时就已经超时了。
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        # 用动态规划，从底层慢慢往结果靠近。靠近过程中的中间变量已经包含了更早的所有情况（有点马尔可夫）
        m = 3
        front1 = 1
        front2 = 2
        while m <= n:
            res = front1 + front2
            front1 = front2
            front2 = res
            m += 1
        return res