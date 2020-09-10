class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # labuladong模板
        # 这才是正确解法。下面我写的，复杂度并不低。这个解法中真正的On复杂度。
        # 我下面的解法，每次往右滑动时，都遍历了needs的每个字母,检查window是否与其相等。
        # 这其实就on2了,不可取。
        res = []
        left, right = 0, 0
        needs = {}
        window = {}
        for i in p:
            needs[i] = needs.get(i, 0) + 1
        match = 0

        while right < len(s):
            c1 = s[right]
            if c1 in needs:
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            while match == len(needs):
                if (right - left == len(p)):
                    res.append(left)
                c2 = s[left]
                if (c2 in needs):
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                    if window[c2] == 0:
                        del window[c2]
                left += 1
            
        return res


        # # 双指针
        # if len(s) < len(p):
        #     return None
        # left = 0
        # right = left + len(p) - 1
        # res = []
        
        # window = {}
        # for i in range(left, right + 1):
        #     window[s[i]] = window.get(s[i], 0) + 1

        # needs = {}
        # for i in p:
        #     needs[i] = needs.get(i, 0) + 1
        
        # def check():
        #     for i in needs:
        #         if window.get(i, 0) != needs[i]:
        #             return False
        #     return True

        # while left < len(s) - len(p) + 1:
        #     if check():
        #         res.append(left)

        #     window[s[left]] -= 1
        #     if window[s[left]] == 0:
        #         del window[s[left]]
        #     left += 1

        #     right += 1
        #     if right == len(s):
        #         break
        #     window[s[right]] = window.get(s[right], 0) + 1

        # return res