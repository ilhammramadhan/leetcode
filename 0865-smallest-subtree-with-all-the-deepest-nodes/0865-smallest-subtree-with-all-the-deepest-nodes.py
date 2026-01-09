class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            # Base Case: return (depth, candidate_node)
            if not node:
                return 0, None
            
            # Post-order traversal: Get info from children first
            l_depth, l_candidate = dfs(node.left)
            r_depth, r_candidate = dfs(node.right)
            
            # Logic: If depths are equal, the current node is the LCA
            if l_depth == r_depth:
                return l_depth + 1, node
            
            # If left is deeper, the answer must be in the left subtree
            if l_depth > r_depth:
                return l_depth + 1, l_candidate
            
            # If right is deeper, the answer must be in the right subtree
            else:
                return r_depth + 1, r_candidate

        # We only need the candidate node from the final result
        return dfs(root)[1]