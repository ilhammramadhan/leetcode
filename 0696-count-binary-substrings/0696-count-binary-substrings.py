class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # 'groups' will store the lengths of consecutive characters
        # e.g., "00110" -> [2, 2, 1]
        groups = []
        if not s:
            return 0
        
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count) # Don't forget the last group!
        
        ans = 0
        # For every adjacent pair of groups, take the minimum length
        for i in range(1, len(groups)):
            ans += min(groups[i], groups[i-1])
            
        return ans