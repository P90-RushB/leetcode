from collections import deque
class Codec:
    # 看的手机python的方法。思路还是比较清晰的。
    # 在序列化时，前序遍历存入list。
    # 在反序列化时，从头取数据（用deque比list高效），递归建树。
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = []
        def preorder(node):
            if not node:
                nodes.append('null')
            else:
                nodes.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return ','.join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node_list = deque(data.split(','))
        def rebuild():
            if not node_list:
                return None
            
            node = node_list.popleft()
            if node == 'null':
                return None
            node = TreeNode(node)
            node.left = rebuild()
            node.right = rebuild()
            return node
        return rebuild()