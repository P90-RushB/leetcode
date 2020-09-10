# 这种题虽然不是算法题，但写的全面又简洁真的需要经验…… 看的博客
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        m = len(a) - 1
        n = len(b) - 1
        carry = 0
        while m>=0 or n >= 0:
            p = int(a[m]) if m >= 0 else 0
            m -= 1
            q = int(b[n]) if n >= 0 else 0
            n -= 1
            sum = p + q + carry
            res = str(sum % 2) + res
            carry = int(sum / 2)
        return '1' + res if carry == 1 else res