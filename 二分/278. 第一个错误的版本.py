# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 这题如果看成二分类的第二类应用：找左边界，就略显麻烦了（毕竟要最后额外判断），
        # 这其实是二分的第一类应用：找目标值 目标值的特点是， target-1是合格的，target是不合格的。
        # 该值肯定存在。
        # 我习惯用left < right的形式：
        # 这题还是很有代表性的，如果一堆数中找左边界，完全可以不用第二类的模板，就按这种方式，用找target的模板。
        left = 1
        right = n + 1
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                # 对应标准模板中等于target的情况
                if not isBadVersion(mid-1):
                    return mid
                # 对应标准模板中大于target的情况
                else:
                    right = mid
            # 对应标准模板中小于target的情况
            else:
                left = mid + 1
        return -1