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
                
