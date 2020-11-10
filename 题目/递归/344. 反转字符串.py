class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 方法1， 头尾双指针
        # n = len(s)
        # left = 0
        # right = n-1
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1
        
        # 方法2， 递归
        def helper(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            helper(left+1, right-1)
        helper(0, len(s)-1)
        