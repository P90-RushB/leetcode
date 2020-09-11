class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count=1

class KthLargest:
# 探索中二叉树一节里提到该题，看的题解中的一个。其实应该用堆，更常见。
    def insertIntoBST(self, cur, val):
        if not cur:
            cur = TreeNode(val)
            return cur
        if cur.val < val:
            cur.right = self.insertIntoBST(cur.right, val)
        else:
            cur.left = self.insertIntoBST(cur.left, val)
        cur.count += 1
        return cur

    def __init__(self, k: int, nums: List[int]):
        self.root = None
        self.k = k
        self.kLarge = None
        for i in nums:
            self.root = self.insertIntoBST(self.root, i)

    def findKHelper(self, cur, k):
        curCnt = 1
        if cur.right:
            curCnt += cur.right.count
        if k == curCnt:
            return cur
        elif k < curCnt: # 第k大在右子树
            return self.findKHelper(cur.right, k)
        else:
            return self.findKHelper(cur.left, k-curCnt)

    def add(self, val: int) -> int:
        # self.kLarge没有值或者当前值大于self.kLarge才插入。
        if self.kLarge and val > self.kLarge or not self.kLarge:
            self.root = self.insertIntoBST(self.root, val)
        self.kLarge = self.findKHelper(self.root, self.k).val
        return self.kLarge


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)