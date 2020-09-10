class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 最小数的特点， nums[target] < nums[target-1] and nums[target] < nums[target+1]
        # 怎么判断左移右移？ 当mid值大于等于nums[0], 明显是较大的那一半，left要右移，
        # 当mid值小于nums[-1]，很明显mid处于右边较小的那一半序列，mid要左移。

        # 官方题解看着简洁，但我写的感觉直观一点，就按我的吧。

        # 我的方法1. 还是二分找目标值，目标值的特点是小于左边值也小于右边值。
        # 但要注意，序列可能没反转，还是有序的，所以先判断以下nums[0] < nums[-1]成立
        # 的化，第一个数就是最小值。
        #否则，就开始二分，二分前前后各加一个数，就不会mid+1和mid-1判断时越界了。
        # 当mid的值小于nums[-2](也就是前后各加一个数之前的nums[-1])，说明mid处于
        # 右半部分较小的序列中，right左移。同理，当mid大于nums[1]，left要右移。

        # if not nums:
        #     return -1
        
        # if len(nums) == 1 or nums[0] < nums[-1]:
        #     return nums[0]
        
        # nums.insert(0, nums[0] + 1)
        # nums.append(nums[-1] + 1)
        # left = 1
        # right = len(nums) - 1
        # while left < right:
        #     mid = left + (right - left) // 2
        #     if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
        #         return nums[mid]
        #     elif nums[mid] >= nums[1]:
        #         left = mid + 1
        #     elif nums[mid] <= nums[-2]:
        #         right = mid
        # return -1


# 方法二也是我写的，和方法一思路一模一样，只不过不用前后加数字，直接对是否处于边缘进行判断。
        if not nums:
            return -1
        
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if (mid+1 == len(nums) or nums[mid] < nums[mid+1]) and \
                     (mid-1 < 0 or nums[mid] < nums[mid-1]):
                return nums[mid]
            elif nums[mid] >= nums[0]:
                left = mid + 1
            elif nums[mid] <= nums[-1]:
                right = mid
        return -1