class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # 方法一， 暴力解法，毕竟easy难度，还是过了。
        # res = [-1] * len(nums1)
        # for idx, i in enumerate(nums1):
        #     start_find = False
        #     for j in nums2:
        #         if j == i:
        #             start_find = True
        #         if start_find and j > i:
        #             res[idx] = j
        #             break
        # return res

        # 方法二 o(n)解法，单调栈。 labuladong的逻辑，从后往前
        # 首先不管nums1,用单调栈把nums2的每个数的下一个最大数找到。
        # s = []
        # dic = {}

        # for i in range(len(nums2)-1, -1, -1):
        #     while s and nums2[i] >= s[-1]:
        #         s.pop()

        #     if s:
        #         dic[nums2[i]] = s[-1]

            
        #     s.append(nums2[i])
        
        # res = [-1] * len(nums1)
        # for k,v in enumerate(nums1):
        #     if v in dic:
        #         res[k] = dic[v]
        # return res

    # 方法三 o（n）， 仍然是单调栈，但是是官方题解的方法，是顺序遍历的。
    # 仍然是先不管nums1, 顺序，用一个栈，只压栈更小元素。
    # 如果当前遍历到的数大于栈顶，那栈顶那个数的下一个更大数就是当前这个数，存到字典里。
    # 既然找到了，就弹栈。
        s = []
        dic = {}
        for i in nums2:
            while s and s[-1] <= i:
                dic[s.pop()] = i
            s.append(i)

        res = [-1] * len(nums1)
        for k,v in enumerate(nums1):
            if v in dic:
                res[k] = dic[v]
        return res

        
