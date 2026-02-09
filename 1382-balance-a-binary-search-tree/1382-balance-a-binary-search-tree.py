# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # --- Phase 1: In-order traversal to get sorted values ---
        sorted_vals = []
        
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            sorted_vals.append(node.val)
            inorder_traversal(node.right)
            
        inorder_traversal(root)
        
        # --- Phase 2: Rebuild balanced BST from sorted list ---
        def build_balanced_bst(left, right):
            # Base case: if pointers cross, no elements left
            if left > right:
                return None
            
            # Pick the middle element to start the tree/subtree
            mid = (left + right) // 2
            current_root = TreeNode(sorted_vals[mid])
            
            # Recursively build left and right subtrees
            # Left child uses the left half of the list
            current_root.left = build_balanced_bst(left, mid - 1)
            # Right child uses the right half of the list
            current_root.right = build_balanced_bst(mid + 1, right)
            
            return current_root
            
        # Start the build process using the full range of the list
        return build_balanced_bst(0, len(sorted_vals) - 1)