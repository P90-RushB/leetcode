class Solution:
    def reverseWords(self, s: str) -> str:
        # 直接用栈
        if not s:
            return ''
        stack = []
        res = ''
        for k,v in enumerate(s):
            if v == ' ':
                while stack:
                    res += stack.pop()
                res += ' '
            else:
                stack.append(v)
                if k == len(s)-1:
                    while stack:
                        res += stack.pop()
                    return res
