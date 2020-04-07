class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 方法一，直接一行一行减

        # layer = 0
        # #  从第一层开始，如果硬币数n大于等于下一层应该有的硬币数，就继续
        # while n >= layer+1:
        #     n -= layer + 1
        #     layer += 1
        # return layer

        # 方法二,这是二分法的第二类应用：找最后一个小于target的数的序号。
        # 由于我用的模板是《=，mid+1，mid-1，这种，在结束时，
        # 如果用right作为返回值，由于返回的是mid -1，所以right已经代表了最后一个小于target的序号。
        # 而如果返回left，由于left = mid + 1，所以已经代表第一个大于target的序号。
        # 该题需要返回right
        # if n <= 1: return n
        # left, right = 1, n
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if mid * (mid + 1) / 2 <= n:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return right

        # 方法三，再来看一种数学解法O(1)，充分利用了等差数列的性质，我们建立等式,
        #  n = (1 + x) * x / 2, 我们用一元二次方程的求根公式可以得到 x = (-1 + sqrt(8 * n + 1)) / 2, 
        # 然后取整后就是能填满的行数
        return int((-1 + (8 * n + 1) ** 0.5) // 2)