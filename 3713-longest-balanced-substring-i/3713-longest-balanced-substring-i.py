class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        # 1. Outer loop: Pick the starting point (i)
        for i in range(n):
            # Create a dictionary to count frequencies for the current window starting at i
            counts = {}
            
            # 2. Inner loop: Pick the ending point (j), extending the substring one char at a time
            for j in range(i, n):
                char = s[j]
                
                # Update frequency of the current character
                counts[char] = counts.get(char, 0) + 1
                
                # 3. Check if balanced
                # We get all the frequency values from the dictionary
                freq_values = list(counts.values())
                
                # Use a set to remove duplicates. 
                # If the set size is 1, it means all distinct characters 
                # have the same frequency.
                if len(set(freq_values)) == 1:
                    current_len = j - i + 1
                    if current_len > max_len:
                        max_len = current_len
                        
        return max_len