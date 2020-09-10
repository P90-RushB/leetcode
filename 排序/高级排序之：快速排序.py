# 还是直接看原版解释，写的挺好。
# https://github.com/PegasusWang/python_data_structures_and_algorithms/blob/master/docs/13_高级排序算法

# 快排还是分治的思想，每次找一个数（可以直接用第一个数），按小于该数和大于该数分成两部分，然后递归对两部分快排。
# 递归出口就是只剩一个了，就不用排了，然后把左半部分，该值，右半部分拼起来。

# 按照上述思想， 一个最简单（但是不高效），可以说是直接翻译出来的快排代码如下：

# 快排训练
import random


########################## 不高效的快排 #############################
# def quick_sort(seq):
#     if not seq or len(seq) < 2:
#         return seq
#     else:
#         head = seq[0]
#         left = [seq[i] for i in range(len(seq)) if i !=0 and seq[i] <= head]
#         right = [seq[i] for i in range(len(seq)) if i !=0 and seq[i] > head]

#         return quick_sort(left) + [head] + quick_sort(right)

# def quick_sort_test():
#     seq = list(range(10)) * 2
#     random.shuffle(seq)
#     print('before sort:', seq)
#     # 上面这个因为不是原地排序而是新建数组，所以这里要有返回值。
#     after_sort = quick_sort(seq)
#     print('after sort:', after_sort)
#     assert after_sort == sorted(seq)

# quick_sort_test()

############################### 不高效的快排， 结束 ########################


############################### 真正的快排 #################################

# 下面开始真正的快排，原地排，且每轮只用一次遍历而不像上面，为了得到基准值坐标要遍历一次，得到右边又要一次。
#  这种原地排序不仅要传入数组，还要传入目前要排的在seq中的起始和终止位置。开始时left=0,right = len(seq)-1
def quick_sort_inplace(seq, left, right):
    if left < right:
        # partition函数会将seq[left]放到一个位置，该位置左边的数都小于seq[left],右边的值都大于seq[left],并返回该位置
        pivot = partition(seq, left, right)
        quick_sort_inplace(seq, left,pivot)
        quick_sort_inplace(seq, pivot+1, right)

# 该函数是快排的核心函数，将数组seq的left到right这段数据进行操作，最终：原来的seq[left]的值在操作后，被移到left
# 至right之间的一个新位置，新位置坐标的值都小于该值，右边的值都大于该值，并返回新位置
# 只遍历一次数组就完成partition
def partition(seq, left, right):
    head_idx = left
    head = seq[head_idx]
    left += 1

    while True:
        # 从左找到一个比pivot大的
        while left <= right and seq[left] < head:
            left += 1
        while left <= right and seq[right] >= head:
            right -= 1
        if right < left:
            break
        else:
            # python163的这里的示例图画的很好，看下就懂了
            # 由于while right >= left ，看好，是大于等于
            # 所以当if left > right 不满足时，right 已经
            # 处于left的左边了，而left的左边都是小于基准值的。
            # right这时候指向的是最后一个小于基准值的元素。
            # 把该元素和开头第一个元素（基准值）互换，就完成了
            # 基准值左侧都小于基准值，基准值右侧都大于基准值。
            seq[left], seq[right] = seq[right], seq[left]

    seq[head_idx], seq[right] = seq[right], seq[head_idx]
    return right

def test_partition():
    l = [4, 1, 2, 8]
    assert partition(l, 0, len(l)-1) == 2
    l = [1, 2, 3, 4]
    assert partition(l, 0, len(l)-1) == 0
    l = [4, 3, 2, 1]
    assert partition(l, 0, len(l)-1)

test_partition()

def test_sort(method):
    seq = list(range(10))  

    random.shuffle(seq)
    print('before sort:',seq)
    origin_seq = seq.copy()
    method(seq, 0, len(seq)-1)
    print('after sort:', seq)
    print('乱的数组：', origin_seq)
    assert seq == sorted(origin_seq) 

test_sort(quick_sort_inplace)

# 利用partition函数，还可以解决数组中第k大/小的数的查找，平均klogn复杂度
# 根据胡枢轴元素的位置和K的大小，决定向枢轴元素左侧或in者右侧元素
# 进行进一步划分。这样最坏时间复杂度为O(K*N)。平均时间复杂度为O(K*logK)
# leetcode的215. 数组中的第K个最大元素
# 求第k大和第k小，对应着在partition中两个while的写法：
# 如果求第k大：
#     while left <= right and seq[left] > head:
#         left += 1
#     while left <= right and seq[right] <= head:
#         right -= 1
# 如果求第k小：
#     while left <= right and seq[left] < head:
#         left += 1
#     while left <= right and seq[right] >= head:
#         right -= 1

class Solution:
    def findKthLargest(self, nums, k):
        # 最好方法，利用快排中的partition函数，双指针思想。
        def partition(seq, left, right):
            head_idx = left
            head = seq[head_idx]
            left += 1
            while True:
                while left <= right and seq[left] > head:
                    left += 1
                while left <= right and seq[right] <= head:
                    right -= 1
                if left > right:
                    break
                else:
                    seq[left], seq[right] = seq[right], seq[left]
            seq[right], seq[head_idx] = seq[head_idx], seq[right]
            return right

        left = 0
        right = len(nums) - 1
        while True:
            tmp = partition(nums, left, right)
            if tmp == k-1:
                return nums[tmp]
            elif tmp < k-1:
                # 这里注意不要多此一举，就错了。 比如当前排好位置的序号tmp<k-1,
                # 可能直觉觉得left后移之后，第k大也要变成第k-tmp大，其实是错的。
                # 因为和快排原地排序一样，这个left，right都是针对原数组的位置。
                # 所以不需要对k改变。这里不能多加一个：k = k - tmp
                left = tmp + 1   
            else:
                right = tmp -1
        return None

s = Solution()
res = s.findKthLargest([7,6,5,4,3,2,1], 5)
print(res)



############### 一个与partition函数思想相似，的双指针问题 ###############
################### 荷兰国旗问题 leetcode 75. 颜色分类 ##################
# partition函数解决的是数组第一个数如何放到：左边都小于该数，右边都大于该数的位置。

# 而荷兰国旗问题能解决：
# 虽然说的是三色国旗，但其实可以看成小于目标值，目标值，和大于目标值三部分，
# 这样，就能：给一个指定的数，能左边小于该数，右边小于该数 ，on复杂度，很厉害。

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 很巧妙，有空再看。
        left = 0
        cur = 0
        right = len(nums) - 1
        while cur <= right:
            # 如果当前遍历到的是0，应该放到左侧，则把该值扔给left，户换。
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                cur += 1
                left += 1
            # 若是目标值（1），则继续往后遍历
            elif nums[cur] == 1:
                cur += 1
            # 如果大于目标值（题目里是2），则把该值扔给right
            else:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1

