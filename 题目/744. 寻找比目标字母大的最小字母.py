class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 这题就是标准的用二分找upper bound的题，也就是比target大的最小值。

        # 该题的特殊情况是，字母是循环的，如果target比letters里最大的还大，那就返回第一个数。
        if target >= letters[-1]:
            return  letters[0]

        # 题目说最少俩数，就少了特殊情况的判断。
        n = len(letters)
        left = 0
        right = n - 1
        # 我常用的二分模板。
        while left <= right:
            mid = left + (right - left) // 2
            ########### 关键 ############
            # 最关键的地方就是这里，由于要找的是upper bound，因此这里要用
            # if target >= letters[mid]:， else:
            # 或者 if target < letters[mid]:, else:
            # 这个等于号一定不能错。原理就是，left是一直递增的，也是最后要返回的upper bound，
            # 那么即使当target = letters[mid]， left 仍要+= 1，才是upper bound。
            # 这种题只要懂了原理，就直到怎么写。找lower bound也是类似。
            if target >= letters[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return letters[left]
