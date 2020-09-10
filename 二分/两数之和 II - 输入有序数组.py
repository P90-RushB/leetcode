class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # 字典方法和暴力解法就不说了…… 
        
        # 方法一，二分。
        # 遍历，对每个数i，target - i作为目标，做一次二分查找。复杂度nlongn
        
        # 二分查找目标。传入目标和左索引，右索引一直等于len(numbers)-1
        # 如果找到，返回索引，找不到返回-1
#         def helper(tar, left):
#             right = len(numbers)
#             while left < right:
#                 mid = left + (right - left) // 2
#                 if numbers[mid] == tar:
#                     return mid
#                 elif numbers[mid] < tar:
#                     left = mid + 1
#                 elif numbers[mid] > tar:
#                     right = mid
#             return -1
            
#         for i in range(len(numbers)-1):
#             other = target - numbers[i]
#             second = helper(other, i+1)
#             if second != -1:
#                 return [i+1, second+1]
#         return -1
    
    # 方法二， 双指针。
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
        return -1
    