class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
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