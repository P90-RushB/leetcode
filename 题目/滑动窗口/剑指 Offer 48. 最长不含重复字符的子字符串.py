class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 我写的，和labuladong一毛一样
        
        # 双指针滑动窗口。 当window + right不重复时，right一直右移。
        # 当重复了，left开始左移。
        left, right = 0, 0
        window  = {}
        res = 0

        while right < len(s):
            window[s[right]] = window.get(s[right], 0 ) + 1

            while window[s[right]] > 1:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1

            res = max(right - left + 1, res)
            right += 1
        return res


