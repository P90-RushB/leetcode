from collections import deque
# 单调队列。 （和优先级队列（二叉堆）的区别在于，单调队列是靠丢掉之前较小或较大的数来保持有序O（n）复杂度，而
# 优先级队列靠堆排序，不丢东西，但logn）
class dandiaoQ:

    def __init__(self):
        self.data = deque()
    
    def push(self, n):
        while self.data and self.data[-1] < n:
            self.data.pop()
        self.data.append(n)
    
    def max(self):
        return self.data[0]

    def pop(self, n):
        if self.data[0] == n:
            self.data.popleft()

class Solution:
    def maxSlidingWindow(self, nums, k):
        # 单调队列：以单调递减队列为例，
        # 这种队列，队尾push一个数之后，所有比他小的数，都会被自动pop掉。
        # 听这意思，push入队函数中很明显需要有从尾部pop的功能（在push函数中 while判断
        # 来pop队尾元素），所以单调队列也是
        # 基于双向队列实现（链表）的，在python中，可以使用deque这种
        # 双向队列结构。 该数据结构还需要一个max方法，由于是单调递减，max
        # 可以直接拿队首元素作为max。 还需要一个pop方法，pop从队首
        # 弹出元素，与普通队列区别在于，需要传入队首值n，
        # 因为存在情况：先入队push，然后pop，在push时队首n可能已经因为小于push的值，而被
        # 自动pop掉了，这时就不需要再pop了。
        res = []
        window = dandiaoQ()
        for i in range(len(nums)):
            if i < k - 1:
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i - k + 1])
        return res