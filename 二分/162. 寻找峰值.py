class Solution:
    # 我的方法，思路很清晰。首先，左右各加一个低于原来首尾的元素。
    # 在二分时，left和right的初始化为1和len(num-1)（因为额外加了俩元素）
    # 其他就是left < right 那个模板.
    def findPeakElement(self, nums: List[int]) -> int:
        # 题目说了左右边界也可以当作峰值
        # 当mid > mid + 1,则右边界左移，若小于，则左边界右移动
        if not nums: return -1
        nums.insert(0, nums[0] - 1)
        nums.append(nums[-1] -1)
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid - 1
            elif nums[mid] > nums[mid+1]:
                right = mid
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
        return -1
                