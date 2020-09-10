class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 双指针滑动窗口并不能用，因为数字范围包括负数

        ##################### 方法1，前缀和，未优化  o（n2）#################
        # 解题思路：用前缀和的数组。
        # n = len(nums)
        # # 这里要在开头多加一个0，这是因为每个数本身也是个序列，并且可能数本身就等于k，所以
        # # 前面多加一个为0的假节点
        # sum_arr = [0] * (n+1)

        # for i in range(1, n+1):
        #     sum_arr[i] = sum_arr[i-1] + nums[i-1]
        
        # # 得到的前缀和数组，sum_arr[i]表示前i个数的和（从0开始算，比如前0个数，前1个数） 
        # # 那么，sum_arr[i] - sum_arr[j] 是否等于 k 就可以判断是否符合。
        # res = 0
        # for i in range(1, n+1):
        #     for j in range(i):
        #         if sum_arr[i] - sum_arr[j] == k:
        #             res += 1
        # return res

############################ 方法2， 前缀和 + 字典优化 o（n） #####################

        # 以上，利用前缀和，虽然避免了每次都计算和，但仍然是on2的解法。
        # 优化方式：看上面的两个for循环，内部的for，其实做的事情是：
        # 对于某个sum_arr[i], 遍历从0 到i-1的索引，看是否有j满足：
        # sum_arr[j] == sum_arr[i] - k。 每满足一个，res就加1.
        # 由于j的范围永远是0 到i，因此可以在遍历i的过程中，建立一个字典，
        # 记录0-i中每个索引的索引和的值出现的次数。这样就可以不用第二个for了。

        # 和前面一样
        n = len(nums)
        sum_arr = [0] * (n+1)
        for i in range(1, n+1):
            sum_arr[i] = sum_arr[i-1] + nums[i-1]

        # 优化
        res = 0
        dic = {}
        # 这里不太好想：n+1长度数组的第0位为0，因此初始时前缀和为0的个数为1.
        # 这并不会出错。假设k = 0，因为只有sum_arr[i] - k在字典中才会加，那么开头的0
        # 并不会使结果变多。
        dic[0] = 1
        for i in range(1, n+1):
            if sum_arr[i] - k in dic:
                res += dic[(sum_arr[i] - k)]   
            dic[sum_arr[i]] = dic.get(sum_arr[i], 0) + 1
        return res
        
        # n = len(nums)
        # dic = {}
        # dic[0] = 1
        # ans, sum_i = 0, 0
        # for i in range(n):
        #     sum_i += nums[i]
        #     sum_j = sum_i - k
        #     if sum_j in dic:
        #         ans += dic[sum_j]
        #     dic[sum_i] = dic.get(sum_i, 0) + 1
        # return ans