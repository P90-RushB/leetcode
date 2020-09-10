class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 这玩意不就是层序遍历完事了
        if not root:
            return None
        cur = [root]
        post = []
        while cur:
            for i in cur:
                if i.left:
                    post.append(i.left)
                if i.right:
                    post.append(i.right)
                
            if post:
                for i in range(len(post)):
                    if i == len(post) - 1:
                        post[i].next = None
                    else:
                        post[i].next = post[i+1]
            cur = post
            post = []
        return root