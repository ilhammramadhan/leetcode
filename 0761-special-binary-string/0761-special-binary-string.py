class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # Base case: if the string is empty or very short, no swaps possible
        if not s:
            return ""
        
        count = 0  # To track the balance of 1s and 0s
        i = 0      # Start index of a special substring
        res = []   # To store the processed special substrings
        
        for j, char in enumerate(s):
            # Update balance: +1 for '1', -1 for '0'
            count += 1 if char == '1' else -1
            
            # When count hits 0, we've found a complete 'Special Substring'
            if count == 0:
                # 1. Strip the outer layers: 
                #    A special string always starts with '1' and ends with '0'.
                #    We recursively process the "inner" part: s[i+1 : j]
                inner_part = self.makeLargestSpecial(s[i+1:j])
                
                # 2. Re-wrap the processed inner part with the '1' and '0'
                res.append("1" + inner_part + "0")
                
                # 3. Move the start pointer to the beginning of the next substring
                i = j + 1
        
        # 4. Sort the special substrings in descending order to get 
        #    the lexicographically largest result, then join them.
        res.sort(reverse=True)
        return "".join(res)