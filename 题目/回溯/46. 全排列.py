class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 全排列，回溯算法
        # 回溯算法模板：
        # result = []
        # def backtrack(路径， 选择列表)：
        #     if 满足结束条件：
        #         result.add(路径)
        #         return
            
        #     for 选择 in 选择列表：
        #         做选择
        #         backtrack（路径， 选择列表）
        #         撤销选择

        # from copy import copy
        # res = []
        # track = []

        def backtrack():
            
            # 递归出口
            if len(track) == len(nums):
                res.append(copy(track))

            for i in nums:

                if i in track:
                    continue

                track.append(i)
                backtrack()
                track.pop()
        
        backtrack()
        return res