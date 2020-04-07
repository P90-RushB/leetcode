class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 重点在于怎么利用双指针，避免重复计算。
        # 由于题目中最多只能删一个字符，这就是重点，
        # 这意味着双指针来判断回文时，一旦遇到左右不等，只需要左或者右挪一位，
        # 再进行剩下部分的回文判断，如果挪了一次了，剩下的还不等，那肯定不是回文了。
        # 否则，就是回文。
        left = 0
        right = len(s) - 1

        # 该函数用来判断数组s的left到right位置内是否是回文。
        def isValid(left, right):
            nonlocal s
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # 
        while (left < right):
            if s[left] != s[right]:
                return isValid(left, right-1) \
                or isValid(left+1, right)
            left += 1
            right -= 1
        return True