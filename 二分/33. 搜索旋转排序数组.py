class Solution:
    # 这题挺难，主要是怎么判断该往左走还是右走。注释是官方题解，
    # 下面我用同样的思路，用left < right 的形式重新写了一次。
    def search(self, nums: List[int], target: int) -> int:

#         if not nums:
#             return -1
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid
#             if nums[0] <= nums[mid]:
#                 if nums[0] <= target < nums[mid]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             else:
#                 if nums[mid] < target <= nums[len(nums) - 1]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#         return -1
        
        # 官方题解一语惊醒梦中人
        # 二分 难点在于怎么判断该从二分后的左边还是右边找。
        # 当从mid分成左右两半之后，一定有一半是有序的，判断是否有序的方法，如果这半部分首小于尾，当然就有序的。
        #然后就可以判断target在哪边。
        
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] <= nums[-1]:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid
        return -1