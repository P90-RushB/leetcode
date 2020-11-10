class Solution:
    def trap(self, height):

        # 方法0， 暴力迭代。思路，对每个索引，这个位置能盛的水的高度，取决于该位置左边
        # 最高值pre_max 和右边最高值 post_max 的小者。遍历每个格子，算该格子能盛的高度。

        # 方法1，是对方法0的优化， o（n）。 首先倒着遍历，记录每个位置，其后面最大的数有多高。
        # 然后正着遍历，不断更新到当前索引时，左边的最大值。然后，思路和方法0一样。
        array = [-1] * len(height)
        maxv = -1
        for i in range(len(height)-1, -1, -1):
            array[i] = maxv
            maxv = max(maxv, height[i])
        
        pre_maxv = -1
        res = 0
        for i in range(len(height)):
            lower = min(pre_maxv, array[i])
            if lower > height[i]:
                res += lower - height[i]
            pre_maxv = max(pre_maxv, height[i])
        return res


s = Solution()
res = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(res)

# 方法二 单调栈。
class Solution:
    def trap(self, height):
        # 单调栈
        # 这个算格子的方法是一行一行来的。
        
        ans = 0
        cur = 0
        s = []
        while cur < len(height):
            while s and height[cur] > height[s[-1]]:
                top = s.pop()
                if not s:
                    break
                dis = cur - s[-1] - 1
                bounded_height = min(height[cur], height[s[-1]]) - height[top]

                ans += dis * bounded_height

            s.append(cur)
            cur += 1

        return ans