class Solution:
    # 这题应该难度是中等，而不是标的简单。因为应该要用二分，logn的解法，线性扫描不能算过。
    # 这题其实是二分的第三类应用：找右边界应用的变形：找第一个大于target的数。
    # 很简单，找右边界时返回left-1，而找第一个大于target的数，返回left即可，而且不管target
    # 是否存在，left都代表第一个大于target的数
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 小写字母的ascii为97-122
        # 该题为找右边界再往右挪一位
        toint = [ord(i) for i in letters] 
        target = ord(target)
        
        left = 0
        right = len(toint)
        while left < right:
            mid = left + (right-left) // 2
            if toint[mid] == target:
                left = mid + 1
            elif toint[mid] < target:
                left = mid + 1
            elif toint[mid] > target:
                right = mid
        # target 比任何数都小。
        if left == 0:
            return chr(toint[0])
        # if toint[left-1] == target:
        res = toint[left] if left<len(toint) else toint[0]
        return chr(res)
