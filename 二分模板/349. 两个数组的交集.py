class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # 方法1，用集合，不说了。 on时间复杂度，on空间复杂度。
        # ht = set()
        # for i in nums1:
        #     ht.add(i)
        
        # res = []
        # for i in nums2:
        #     if i in ht:
        #         res.append(i)
        #         ht.remove(i)

        # return res
    
    # 方法二，先给两个数组排序，然后用两个指针分别指向两个数组的开头，然后比较两个数组的大小，把小的数字的指针      # 向后移，如果两个指针指的数字相等，那么看结果res是否为空，如果为空或者是最后一个数字和当前数字不等的话，       #将该数字加入结果res中  on取决于排序，一般用nlogn的排序就好。
        # nums1.sort()
        # nums2.sort()
        # i, j = 0, 0

        # res = []
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums1[i] > nums2[j]:
        #         j += 1
        #     else:
        #         if not res or nums1[i] != res[-1]:
        #             res.append(nums1[i])
        #         i += 1
        #         j += 1
        # return res


    # 方法三 ，我们还可以使用二分查找法来做，思路是将一个数组排序，然后遍历另一个数组，
    # 把遍历到的每个数字在排序号的数组中用二分查找法搜索，如果能找到则放入结果set中，
    # 这里我们用到了set的去重复的特性，最后我们将set转为vector即可，每个元素二分on为logn，最终时间复杂度
    # 和方法二一样，nlogn，但实际上海涌到了set，空间复杂度on，所以这题二分并不是最好的方法，只是可以用。
        nums1.sort()


        def binary_search(target):
            left = 0
            right = len(nums1) -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums1[mid] == target:
                    return True
                elif nums1[mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
            return False
                

        res = set()
        for i in nums2:
            if binary_search(i):
                res.add(i)
        return list(res)
