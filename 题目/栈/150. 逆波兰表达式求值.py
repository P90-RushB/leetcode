class Solution:
    # 简简单单，就是栈的应用。
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i in ['+','-','*','/']:
                b = int(s.pop())
                a = int(s.pop())
                if i == '+':
                    s.append(a+b)
                elif i == '-':
                    s.append(a-b)
                elif i == '*':
                    s.append(a*b)
                else:
                    s.append(a/b)
            else:
                s.append(i)
        return int(s[-1])