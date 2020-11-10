class Solution:
    # 这题还可以用栈，还没看，可以看官方题解。
    # 我用的递归方法。思路就是：遍历，如果是字符，就加到res中。
    # 如果是数字，找完连续的一块数字 作为倍数，然后找接下来的[]内字符串的开始结束索引。
    # 然后对sub_str递归调用本函数，来解决。(因为子字符串内可能还是有[])
    def decodeString(self, s: str) -> str:
        # 递归
        # 遍历字符串，找到 数字+ [] 的始末索引， 正常字符串，
        # 对[] 内递归

        res = ''

        idx = 0
        while idx < len(s):
            if s[idx].isalpha():
                res += s[idx]
            elif s[idx].isdigit():
                times = s[idx]
                idx += 1
                while s[idx].isdigit():
                    times += s[idx]
                    idx += 1
                times = int(times)

                # 计数一下内部嵌套的左括号
                left_kuohao = 1
                start = idx + 1
                while left_kuohao > 0:
                    idx += 1
                    if s[idx] == '[':
                        left_kuohao += 1
                    elif s[idx] == ']':
                        left_kuohao -= 1

                tmp_str = self.decodeString(s[start:idx])

                res += times * tmp_str

            idx += 1
        return res
                

# 二刷，我写的栈方法，比上面的递归要简单些。
class Solution:
    def decodeString(self, s: str) -> str:
        # 用栈，当遇到右括号，开始弹栈，遇到左括号时，中间的就是要重复的；然后继续弹出，
        # 左括号到字母之间的数字，表示重复的次数。
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                tmp = ''
                while stack[-1] != '[':
                    tmp = stack.pop() + tmp
                # 弹出左括号
                stack.pop()
                tmp1 = 0
                pow_nums = 0
                while stack and stack[-1].isdigit():
                    tmp1 += int(stack.pop()) * 10 ** pow_nums
                    pow_nums += 1
                stack.append(tmp * tmp1)
        return ''.join(stack)
