class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        
        # TrieNode class definition
        class TrieNode:
            def __init__(self, name=""):
                self.name = name
                self.children = {}
                self.key = ""
                self.is_deleted = False

        # 1. Build the Trie
        root = TrieNode()
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode(folder)
                node = node.children[folder]

        # 2. Identify Duplicates (using a helper function)
        seen_keys = {}
        self._get_folder_keys(root, seen_keys)

        # 3. Collect Remaining Paths (using another helper function)
        result = []
        self._collect_paths(root, [], result)
        
        return result

    def _get_folder_keys(self, node: 'TrieNode', seen_keys: dict):
        if not node.children:
            return
        
        child_structure_parts = []
        for child_node in node.children.values():
            self._get_folder_keys(child_node, seen_keys)
            # This part creates the signature for each child branch
            child_structure_parts.append(child_node.name + child_node.key)
            
        # Sort to ensure order doesn't matter
        child_structure_parts.sort()
        node.key = "(" + "".join(child_structure_parts) + ")"

        if node.key in seen_keys:
            node.is_deleted = True
            seen_keys[node.key].is_deleted = True
        else:
            seen_keys[node.key] = node

    def _collect_paths(self, node: 'TrieNode', current_path: List[str], result: List[List[str]]):
        if node.is_deleted:
            return
        
        if current_path:
            result.append(current_path)
            
        for child_name, child_node in node.children.items():
            self._collect_paths(child_node, current_path + [child_name], result)