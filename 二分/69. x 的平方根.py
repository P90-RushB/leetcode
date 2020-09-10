class Solution:
    # 题很简单，属于二分的第一类，查找目标值。我用left < right这种形式解决，所有二分变种我都喜欢用这种。
    # 为什么这题是查找目标值呢？ 这个目标一定存在，只不过不是数值来表示，而是
    # 存在target， target**2 <=x and (target+1)**2 > x
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        # 直接从1到x，二分
        left = 1
        right = x
        while left < right:
            mid = left + (right - left) // 2
            v1 = mid **2
            v2 = (mid+1) ** 2
            if v1 <= x and v2 > x:
                return mid
            elif v1 > x:
                right = mid
            elif v1 < x:
                left = mid + 1
        return -1
        