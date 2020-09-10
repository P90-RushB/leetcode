###################### 一个模板解决前中后层序遍历 ####################
# 这种方法对于前中后层序遍历通用，那它的缺点就是每个节点都两次出入栈（这也是能够前中后统一起来的原因），
# 因为后序比较特殊，是需要两次出入栈的（根节点拿出来看看，再放回去）。对于前中序，该方法通用但可能略低效，
# 不过，也就低一点点点。
# 本方法出自leetcode 94 中序遍历 题解中的henry的解法。

# 其核心思想如下：

# 使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色。
# 如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子节点依次入栈。
# 如果遇到的节点为灰色，则将节点的值输出。

# 解释一下为什么需要“右子节点、自身、左子节点依次入栈”

# 我们有一棵二叉树：

#                中
#               /  \
#              左   右
# 前序遍历：中，左，右
# 中序遍历：左，中，右
# 后序遍历：左，右，中

# 本题需要中序遍历。

# 栈是一种 先进后出的结构，出栈顺序为左，中，右
# 那么入栈顺序必须调整为倒序，也就是右，中，左

# 同理，如果是前序遍历，入栈顺序为 右，左，中；后序遍历，入栈顺序中，右，左

########## 通用之中序 ###########
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        s = [(WHITE, root)]
        res = []
        while s:
            color, node = s.pop()
            if not node:
                continue
            if color == WHITE:
                s.append((WHITE, node.right))
                s.append((GRAY, node))
                s.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res
# 前序和后序遍历只需要调换三个append的顺序即可，简单至极。

##### 用该方法解决层次遍历 #####
# 只需要再多加一个标志：level。但这种用dfs的方式来得到层序，算不上层次遍历，但思路很有意思。
# 实际做层序还是用bfs的好。
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        WHITE, GRAY = 0, 1
        s = [(WHITE, root, 0)]
        res = []
        while s:
            color, node, level = s.pop()
            if node:   
                if color == WHITE:
                    # 这里顺序是右，左，根，因为要先搞根那一层，这样在res里生成每一层的空列表。
                    # 然后在同一层，出栈左，右。
                    s.append((WHITE, node.right, level+1))
                    s.append((WHITE, node.left, level+1))
                    s.append((GRAY, node, level))
                else:
                    if level == len(res):
                        res.append([])
                    res[level].append(node.val)
        return res



###############################  下面是常见的，更高效的但不能互相通用 前中后层序的 遍历 #######################


################################### 前序 #############################

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        ################# 递归
        # res = []
        # def help(node):
        #     nonlocal res
        #     if not node:
        #         return 
        #     res.append(node.val)
        #     help(node.left)
        #     help(node.right)
        # help(root)
        # return res
    
        ################## 迭代
        if not root:
            return []
        
        res = []
        
        p = root
        stack = []
        while p or stack:
            while p:
                res.append(p.val)
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                p = p.right
        return res

######################################################### 中序
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        #################### 递归
        # res = []
        # def help(node):
        #     nonlocal res
        #     if node:
        #         help(node.left)
        #         res.append(node.val)
        #         help(node.right)
        # help(root)
        # return res
        
        ############################## 迭代

        if not root:
            return []
        res = []
        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                res.append(p.val)
                p = p.right
                
        return res

######################################################### 后序
# leetcode 102题。 该题特殊要求是每层单独放一个list里，返回一个二维的list,这样
# 用队列实现时要稍微麻烦些。 
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        ###################### 递归
        # if not root:
        #     return []
        # res = []
        # def help(node):
        #     nonlocal res
        #     if node:
        #         help(node.left)
        #         help(node.right)
        #         res.append(node.val)
        # help(root)
        # return res
        
        ############################ 迭代
        if not root:
            return []
        cur, last = root, None
        stack = []
        res = []
        while cur:
            stack.append(cur)
            cur = cur.left
        
        while stack:
            cur = stack.pop()
            if not cur.right or cur.right == last:
                res.append(cur.val)
                last = cur
            else:
                stack.append(cur)
                cur = cur.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
        return res


###################################################### 层序
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        ##################### 用栈实现
        if not root:
            return []
        
        cur = [root]
        post = []
        res = []
        while cur:
            tmp = []
            for i in cur:
                tmp.append(i.val)
                if i.left:
                    post.append(i.left)
                if i.right:
                    post.append(i.right)
            if tmp:
                res.append(tmp)
            cur = post
            post = []
        return res

    ################################## 用队列实现
    # 队列 102题要每层单独一个list，用队列要麻烦一些：
    # 首先，普通的队列实现的层序遍历：
        # if not root:
        #     return []
        # res = []
        # queue = [root]
        # while queue:
        #     q = queue.pop(0)
        #     res.append(q.val)
        #     if q.left:
        #         queue.append(q.left)
        #     if q.right:
        #         queue.append(q.right)

    # 针对本题，每层放一个list里：
        if not root:
            return []
        
        res = [] # 放最终结果
        tmp_res = [] # 放每层的结果
        queue = [root] # 队列，每层过后重置为下层所有节点的queue
        tmp = [] # 临时保存下一层所有节点，一次性给queue重置时用。
        while queue or tmp:
            if queue:
                q = queue.pop(0)
                tmp_res.append(q.val)
                if q.left:
                    tmp.append(q.left)
                if q.right:
                    tmp.append(q.right)
            else:
                queue = tmp
                tmp = []
                res.append(tmp_res)
                tmp_res = []
        # 最后一次的tmp_res得手动赋值过来
        res.append(tmp_res)
        return res

    # 我用栈（list）又做一遍写的形式，差不多：
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        pre = [root]
        now = []
        res = [[root.val]]
        while pre:
            tmp = []
            for i in pre:
                if i.left:
                    now.append(i.left)
                    tmp.append(i.left.val)
                if i.right:
                    now.append(i.right)
                    tmp.append(i.right.val)
            if not tmp:
                break
            res.append(tmp)
            pre = now
            now = []

        return res
            
