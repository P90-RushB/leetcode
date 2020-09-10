class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 回溯。其中k限制了多叉树的高度（只能k层高）
        # 与全排列的另一个区别：组合不能有重复的，在实际编写中，
        # 可以按照顺序，即第一个数要最小，依次增大，这样2，3就是一个解，3，2就不会
        # 存到结果中，从而达到要求
        from copy import copy
        res = []
        track = []

        def backtrack():
            if len(track) == k:
                res.append(copy(track))
                return 

            for i in range(1, n+1):
                if i in track or (track and i < track[-1]):
                    continue
                
                track.append(i)
                backtrack()
                track.pop()
        backtrack()
        return res


################## 二刷时写的，思路是一样的，写法略有不同 ####################
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 回溯 因为是组合，没顺序。 可以看成每次加的数都要更大（或者按索引只能更大，都行）
        # 目的只是为了剔除重复
        # 比 子集 还要多考虑的一个，是有k个数的限制，也就是n叉数的深度。
        from copy import copy
        res = []
        track = []
        def backtrack(i):
            if len(track) == k:
                res.append(copy(track))
                return 
            for j in range(i, n+1):
                track.append(j)
                backtrack(j+1)
                track.pop()
        
        backtrack(1)
        return res