class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 1. Create a set to store the unique substrings we find
        seen_codes = set()
        
        # 2. Determine how many unique codes we need to find (2 to the power of k)
        required_count = 1 << k  # This is a bitwise way of saying 2^k
        
        # 3. Iterate through the string with a sliding window of length k
        # We stop at len(s) - k + 1 to ensure we have enough characters left for a full window
        for i in range(len(s) - k + 1):
            # Extract the substring of length k
            current_code = s[i : i + k]
            
            # Add it to our set
            seen_codes.add(current_code)
            
            # Optimization: If we've already found all possible codes, we can stop early
            if len(seen_codes) == required_count:
                return True
                
        # 4. After checking the whole string, see if our set size matches the goal
        return len(seen_codes) == required_count