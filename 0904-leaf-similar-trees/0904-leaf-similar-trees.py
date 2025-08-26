# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getLeaves(self, root):
        leaves = []

        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:  # leaf node
                leaves.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return leaves

    def leafSimilar(self, root1, root2):
        return self.getLeaves(root1) == self.getLeaves(root2)
