# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        OUTPUT = []
        def dfs(rt,path,summ):
            summ += rt.val
            path.append(rt.val)
            if rt.left:
                dfs(rt.left,path[:],summ)
            if rt.right:
                dfs(rt.right,path[:],summ)
            if not rt.left and not rt.right:
                if targetSum == summ:
                    # print(rt.val,summ)
                    OUTPUT.append(path)
        if root:
            dfs(root,[],0)
        return OUTPUT
                