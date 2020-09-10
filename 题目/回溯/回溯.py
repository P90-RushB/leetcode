# 回溯算法的总结：
# https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3%E4%BF%AE%E8%AE%A2%E7%89%88.md

# 总结： 回溯算法就是n叉树的遍历问题。关键就是在前序遍历和后序遍历的位置做一些操作，算法框架如下：
def backtrack(...):
    for 选择 in 选择列表:
        做选择
        backtrack(...)
        撤销选择
写 backtrack 函数时，需要维护走过的「路径」和当前可以做的「选择列表」，当触发「结束条件」时，将「路径」记入结果集。

其实想想看，回溯算法和动态规划是不是有点像呢？我们在动态规划系列文章中多次强调，动态规划的三个需要明确的点就是「状态」「选择」和「base case」，是不是就对应着走过的「路径」，当前的「选择列表」和「结束条件」？

某种程度上说，动态规划的暴力求解阶段就是回溯算法。只是有的问题具有重叠子问题性质，可以用 dp table 或者备忘录优化，将递归树大幅剪枝，这就变成了动态规划。而今天的两个问题，都没有重叠子问题，也就是回溯算法问题了，复杂度非常高是不可避免的。

# 全排列问题：
# 输入一组不重复的数字，返回它们的全排列
# from copy import copy
# res = []
# def permute(nums):
#     # 记录 路径
#     track = []
#     backtrack(nums, track)
#     return res

# def backtrack(nums, track):

#     if len(track) == len(nums):
#         res.append(copy(track))
#         return 
    
#     for i in range(len(nums)):
#         if nums[i] in track:
#             continue
#         track.append(nums[i])
#         backtrack(nums, track)
#         track.pop()

# permute([1,2,4])
# print(res)


# 我的回溯
from copy import copy
def permute(nums):
    res = []
    track = []

    def helper():

        # 递归出口。 当track数字满了，说明到了一条路径的底。
        if len(track) == len(nums):
            res.append(copy(track))
            return 

        for i in nums:
            if i in track:
                continue
            
            # 做一次选择
            track.append(i)

            helper()

            track.pop()

    helper()

    return res

res = permute([1,2,4])
print(res)