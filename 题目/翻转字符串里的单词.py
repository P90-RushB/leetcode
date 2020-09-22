耗了不少时间，硬磕出来了，以为官方题解有什么奇思妙想，然而，其实和我做法没啥区别。
当然，如果调用api，一行就行了： return ''.join(reversed(s.split()))

class Solution:
    def reverseWords(self, s: str) -> str:
        def helper(s):
        # 用栈就行了。
            res = []
            idx = 0
            for i in s:
                if i == ' ':
                    idx += 1
                else:
                    break

            now = idx
            while now < len(s):
                tmp = ''
                while now < len(s) and s[now] != ' ':
                    tmp += s[now]
                    now += 1
                res.append(tmp)
                
                while True:
                    if len(s) == now:
                        return res
                    else:
                        if s[now] == ' ':
                            now += 1
                        else:
                            break
        res = helper(s)
        res1 = ''
        if not res:
            return res1
        for k, v in enumerate(reversed(res)):
            res1 += v
            if k != len(res)-1:
                res1 += ' '
        return res1


            
