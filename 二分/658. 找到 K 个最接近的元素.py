class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
# 我的方法，思路简单，但细节不少。 首先，找到左边界，如果没有左边界，左边界模板返回的left索引代表的是
# 第一个大于target的数。然后对left和left-1进行判断，哪个与x的差绝对值最小，将其作为mid。
# 然后对mid左右，进行扩散，每次将与x差的绝对值最小的哪个索引加进res数组，最后排个序。

        # 先找到左边界，如果没有，就找到最后一个小于target的
        if not arr:
            return -1
        left = 0 
        right = len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                right = mid
            elif arr[mid] > x:
                right = mid
            elif arr[mid] < x:
                left = mid + 1
        # 说明x大于arr所有数
        if left == len(arr):
            return arr[-k:]
        
        res = []
        
        if arr[left] == x:
            mid = left
        # elif left == 0:
        #     return arr[:k]
        else:
            mid = left if left > 0 and (arr[left] - x < x - arr[left-1]) or left == 0 else left - 1
            
        res.append(arr[mid])
        
        left, right = 1, 1      
        for _ in range(k-1):
            tmp = 0
            if mid - left < 0:
                res.append(arr[mid+right])
                right += 1
            elif mid + right >= len(arr):
                res.append(arr[mid-left])
                left += 1
            elif arr[mid+right] - x < x - arr[mid-left]:
                res.append(arr[mid+right])
                right += 1
            else:
                res.append(arr[mid-left])
                left += 1
        return sorted(res)