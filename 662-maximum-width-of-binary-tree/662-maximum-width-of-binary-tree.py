# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        mem = defaultdict(list)
        def helper(root,col,level):
            if root:
                mem[level].append(col)
                helper(root.left,col*2,level+1)
                helper(root.right,col*2+1,level+1)
        helper(root,0,0)
        return max(   [ (max(i)-min(i)+1)    for j,i in mem.items()  ]    )

        