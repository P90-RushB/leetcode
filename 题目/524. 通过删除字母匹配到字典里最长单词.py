class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:

        def have_or_not(tmp_str):
            nonlocal s
            idx = 0
            for i in s:
                if tmp_str[idx] == i:
                    idx += 1
                if idx == len(tmp_str):
                    return True
            return False

        res = ''
        for i in d:
            if have_or_not(i):
                if len(res) < len(i):
                    res = i
                elif len(res) == len(i):
                    #  按照题目要求，根据ascii码判断谁在字典更前，返回谁。
                    for m,n in zip(res, i):
                        if ord(m) < ord(n):
                            break
                        elif ord(m) > ord(n):
                            res = i
                            break
        return res