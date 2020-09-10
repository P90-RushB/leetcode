class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分法的第一种最简单的形式 
        left = 0
        right = x
        while left <= right:
            mid = left + (right - left) // 2
            if mid**2 <= x and (mid + 1)**2 > x:
                return mid
            elif mid**2 > x:
                right = mid - 1
            elif mid**2 < x:
                left = mid + 1
        