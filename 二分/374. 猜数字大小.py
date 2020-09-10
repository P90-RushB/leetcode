class Solution:
    def guessNumber(self, n: int) -> int:
        # left = 1
        # right = n
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     res = guess(mid)
        #     if res == 0:
        #         return mid
        #     elif res == -1:
        #         right = mid - 1
        #     elif res == 1:
        #         left = mid + 1
        
        
        # left < right的形式
        left = 1
        ############################ 万分重要 ######################
        # 因为left < right 的形式，right是开区间娶不到，所以right 应该等于n + 1
        right = n+1
        while left < right:
            mid = left + (right - left) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid
            elif guess(mid) == 1:
                left = mid + 1
        return -1
        