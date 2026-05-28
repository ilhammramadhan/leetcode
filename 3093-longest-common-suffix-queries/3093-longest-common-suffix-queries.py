from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1  # Will store the index of the "best" string

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        # Helper function to decide if a new string index is better than the current one
        def is_better(new_idx: int, current_best_idx: int) -> bool:
            if current_best_idx == -1:
                return True
            
            len_new = len(wordsContainer[new_idx])
            len_best = len(wordsContainer[current_best_idx])
            
            if len_new < len_best:
                return True
            elif len_new == len_best and new_idx < current_best_idx:
                return True
            
            return False

        # Step 1: Build the Trie by inserting strings backwards
        for i, word in enumerate(wordsContainer):
            curr = root
            
            # Check if this word is the best default (empty suffix match)
            if is_better(i, curr.best_index):
                curr.best_index = i
                
            # Traverse the word backwards
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
                
                # Update the node's best index if the current word is better
                if is_better(i, curr.best_index):
                    curr.best_index = i

        # Step 2: Process each query
        ans = []
        for query in wordsQuery:
            curr = root
            
            # Traverse the query backwards
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    # No more matching characters, break out early
                    break
            
            # Append the best index found at the deepest matching node
            ans.append(curr.best_index)
            
        return ans