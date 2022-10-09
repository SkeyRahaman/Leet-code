# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        v =  set()
        def dfs(root):
            if not root:
                return False
            if root.val in v :
                return True
            v.add(k - root.val)
            return dfs(root.right) or dfs(root.left)
        return dfs(root)