# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            # Count this node if it is good
            count = 1 if node.val >= max_val else 0
            # Update the max value seen so far on the path
            max_val = max(max_val, node.val)
            # Recurse left and right
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count
        
        # Start DFS from root, with initial max value as root's value
        return dfs(root, root.val if root else float('-inf'))
        