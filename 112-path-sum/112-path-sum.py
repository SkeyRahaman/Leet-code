# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,t):
            
            
            if not root.right and not root.left:
                if t == root.val:
                    return True
                else:
                    return False
                
                
                
            x = False
            if root.left:
                x = dfs(root.left,t-root.val)
            if root.right and not x:
                x = dfs(root.right,t-root.val)
            return x
            
            
            
        if root:
            return dfs(root,targetSum)
        else:
            return False

        