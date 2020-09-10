class Solution:
    # 简单
    def isPerfectSquare(self, num: int) -> bool:
        # 二分找target，target的特点是，target ** == num
        left = 1
        right = num + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid ** 2 == num:
                return True
            elif mid**2 < num:
                left = mid + 1
            elif mid**2 > num:
                right = mid
        if left**2 == num:
            return True
        return False