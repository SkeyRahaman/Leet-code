# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "NULL"
        output = []
        q = deque([root])
        while q:
            ptr = q.popleft()
            if ptr:
                output.append(str(ptr.val))
                q.append(ptr.left)
                q.append(ptr.right)
            else:
                output.append("NULL")
        # print(output)
        return ",".join(output)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "NULL":return
        data = collections.deque(data.split(","))
        d1 = int(data.popleft())
        root = TreeNode(d1)
        q = deque([root])
        while data:
            ptr = q.popleft()
            l = data.popleft()
            r = data.popleft()
            if l != "NULL":
                ptr.left = TreeNode(int(l))
                q.append(ptr.left)
            if r != "NULL":
                ptr.right = TreeNode(int(r))
                q.append(ptr.right)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
