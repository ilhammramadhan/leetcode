# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to calculate height and check balance simultaneously
        def check_height(node):
            # Base Case: An empty node has height 0
            if not node:
                return 0
            
            # Step 2: Check Left Subtree
            left_h = check_height(node.left)
            if left_h == -1: 
                return -1  # Propagate imbalance immediately
            
            # Step 3: Check Right Subtree
            right_h = check_height(node.right)
            if right_h == -1: 
                return -1  # Propagate imbalance immediately
            
            # Step 4: Check current node balance
            if abs(left_h - right_h) > 1:
                return -1  # Current node is unbalanced
            
            # Step 5: Return actual height to parent
            return 1 + max(left_h, right_h)

        # Initial call: If check_height returns -1, it's False. Otherwise True.
        return check_height(root) != -1