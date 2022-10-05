# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val,root)
        
        
        def add_node(q1,val):
            while q1:
                node = q1.popleft()
                N1 = TreeNode(val)
                node.left , N1.left = N1, node.left
                N2 = TreeNode(val)
                node.right, N2.right = N2, node.right
                    
            
        q1 = []
        q2 = [root]
        d = 1
        while q2:
            d += 1
            q1 = deque(q2[:])
            q2 = []
            if d == depth:
                add_node(q1,val)
                break
            else:
                while q1:
                    node = q1.popleft()
                    if node.left:
                        q2.append(node.left)
                    if node.right:
                        q2.append(node.right)
        return root
            