class Solution:
    # 因为python中对list传的是引用，代码里需要拷贝新的副本，要用copy
    from copy import copy
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # 规律，如果知道[1,2]的所有子集，[1,2]子集的每个解都加一个3,就是[1,2，3]
        # 比[1,2]多的解，这就是递归的核心了。
        if not nums:
            a = [[]]
            return a
        n = nums.pop()
        res = self.subsets(nums)
        for i in range(len(res)):
            tmp = copy(res[i])
            tmp.append(n)
            res.append(tmp)
        return res

        # 回溯算法。
        # track = []
        # res = []
        # from copy import copy
        # def backtrack(start):
        #     res.append(copy(track))
        #     for i in range(start, len(nums)):
        #         track.append(nums[i])
        #         backtrack(i+1)
        #         track.pop()

        # backtrack(0)
        # return res


############## 我再刷的时候，写的麻烦了………… ################

from copy import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 方法一，动归
        # dp[1,2,3] = dp[1,2] + dp[1,2]的每个解 加上3
        # last = [[]]
        # now = last
        # for n in range(0, len(nums)):
        #     cnt = len(last)
        #     now = last * 2
        #     for i in range(cnt, cnt * 2):
        #         now[i] = copy(last[i-cnt])
        #         now[i].append(nums[n])
        #     last = now
        # return now

        # 方法二 回溯
        # 和全排列一样，用回溯，简单说，就是n叉树的遍历，在遍历过程中，在前序和后序阶段，
        # 进行选择动作和撤销动作的操作。
        # 回溯算法模板：
        # res = []
        # def backtrack(路径，选择列表):
        #     if 路径满足条件：
        #         res.add(路径)
        #         return
        #     for 动作 in 选择列表：
        #         选择动作
        #         backtrack（）
        #         撤销动作
        
        # 对于子集问题，其实可以看做，对于回溯的限制是：每次选择的动作，只能比路径
        # 最后一个数的索引要大。 所以，在代码中，应该存的是索引，这样好进行比较。
        res = []
        track = []
        def backtrack():
            for i in range(len(nums)):
                if track and track[-1] >= i:
                    continue
                track.append(i)
                res.append(copy(track))
                backtrack()
                track.pop()
        backtrack()

        for i in res:
            for t in range(len(i)):
                i[t] = nums[i[t]]
        res.append([])
        return res



        
