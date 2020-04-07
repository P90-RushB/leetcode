class Solution:
    def reverseVowels(self, s: str) -> str:
        yuanyin = 'aeiouAEIOU'
        left = 0
        s = list(s)
        right = len(s) - 1
        while left < right:
            if s[left] in yuanyin and s[right] in yuanyin:
                s[left],s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] in yuanyin:
                right -= 1
            elif s[right] in yuanyin:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(s)

s = Solution()
res = s.reverseVowels('hello')
print(res)