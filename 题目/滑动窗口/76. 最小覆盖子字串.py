class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 这题是滑动窗口题，见labuladong
        # 思路， 双指针left，right。开始都在0索引。right右移，直到left-right包含
        # 解。 然后left右移，直到不满足解。然后重复. 过程中更新结果。
        left, right = 0, 0
        res = s
        minLen = float('inf')

        window  = {}
        needs = {}
        for i in t:
            needs[i] = needs.get(i, 0) + 1

        match = 0

        while right < len(s):
            c1 = s[right]
            if c1 in needs:
                window[c1] = window.get(c1, 0) + 1
                if (window[c1] == needs[c1]):
                    match += 1
            right += 1

            while match == len(needs):
                if right - left < minLen:
                    start = left
                    minLen = right - left
                c2 = s[left]
                if c2 in needs:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                    if window[c2] == 0:
                        del window[c2]
                left += 1
        return '' if  minLen == float('inf') else s[start:start+minLen]
                    
                    