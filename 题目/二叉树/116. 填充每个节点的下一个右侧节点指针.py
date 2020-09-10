class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 这题和117题可以是一样的解法。不过这题是完美二叉树，可以用递归更简单的解决，先放着。
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
########################### 二刷，我终于算是会了用队列实现bfs了…… #######################
# 精髓就在：
# while q:
#     n = len(q)
#     for i in range(n):

######### 当然，对于bfs的套路，不是只有上面这种模板，还有其他两种，可以看该题的官方题解。

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        root.next = None
        from collections import deque

        q = deque()
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i != n-1:
                    node.next = q[0]
                else:
                    node.next = None
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root


###################### 官方题解的方法二： 每层都利用上一层已经建立的next指针。 很巧妙 #####################
# 方法二，递归，很巧妙。
        if not root:
            return root
        
        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root
        
        # Once we reach the final level, we are done
        while leftmost.left:
            
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the 
            # corresponding links for the next level
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # Progress along the list (nodes on the current level)
                head = head.next
            
            # Move onto the next level
            leftmost = leftmost.left
        
        return root 