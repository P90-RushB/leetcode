# 这题没啥说的，简单。 
class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.dp = [0] * len(nums)
        self.dp[0] = nums[0]
        for i in range(1, len(nums)):
            self.dp[i] = self.dp[i-1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] if i == 0 else self.dp[j] - self.dp[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)