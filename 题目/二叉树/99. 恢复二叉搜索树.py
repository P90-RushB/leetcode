class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        li1 = []
        li2 = []
        def help(node):
            nonlocal li1, li2
            if not node:
                return 

            help(node.left)
            li1.append(node)
            li2.append(node.val)
            help(node.right)

        help(root)

        first = second = None
        for i in range(len(li2)-1):
            if li2[i] -li2[i+1] > 0:
                if first == None:
                    first = i
                else:
                    second = i+1
        xianglin = False
        if not second:
            xianglin = True
            second = li1[first+1]
        else:
            second = li1[second]
        first = li1[first]

        first.val, second.val = second.val, first.val