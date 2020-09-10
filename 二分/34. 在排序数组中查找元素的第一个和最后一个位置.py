class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 同时找开头和结尾。
        # 我的思路：先找开头（或结尾），然后找遍历找另一个
        # 先找左边界。
        if not nums:
            return [-1,-1]
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        
        # 线性找右边界
        # pianyi = -1
        # for i in range(left, len(nums)):
        #     if nums[i] == nums[left]:
        #         pianyi += 1
        #     else:
        #         break
        # return [left, left + pianyi]
                
        # 二分找右边界，起始点从左边界开始最好。
        left_res = left
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        # 这种情况不会出现，因为都有左边界了，肯定有右边界。
        if left == 0:
            right_res = -1
        right_res = left - 1 if nums[left-1]==target else -1
        return [left_res, right_res]
    