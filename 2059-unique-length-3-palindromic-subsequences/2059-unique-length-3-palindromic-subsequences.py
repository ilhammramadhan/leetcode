class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # 1. Get the set of unique characters present in the string
        #    to act as the outer shell (the 'X' in XYX)
        unique_chars = set(s)
        
        total_palindromes = 0
        
        # 2. Iterate through each unique character
        for char in unique_chars:
            # Find the very first occurrence of this character
            first_index = s.find(char)
            
            # Find the very last occurrence of this character
            last_index = s.rfind(char)
            
            # 3. If the character appears at least twice with space in between
            if last_index > first_index + 1:
                # Extract the substring between the first and last occurrence
                middle_substring = s[first_index + 1 : last_index]
                
                # 4. Count unique characters in the middle substring
                unique_middles = set(middle_substring)
                total_palindromes += len(unique_middles)
            
            # Edge case: If indices are adjacent (e.g., "aa"), 
            # the slice is empty, set length is 0, which is correct.
                
        return total_palindromes