class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 花里胡哨，这不还是最多不重叠子区间问题。
        # 求出不重叠的有多少个，只要把这些区间都射爆了，剩下的都是重叠的，顺带就爆了。
        # 最多不重叠子区间问题和435题一样，唯一区别是区间端点，气球也爆炸
        #详细分析见：
        # https://github.com/labuladong/fucking-algorithm/blob/master/动态规划系列/贪心算法之区间调度问题.md
        n = len(points)
        if n == 0:
            return 0
        
        points.sort(key=lambda x:x[1])

        c = 1
        now = 0
        for i in range(n):
            if points[i][0] > points[now][1]:
                c += 1
                now = i
        return c