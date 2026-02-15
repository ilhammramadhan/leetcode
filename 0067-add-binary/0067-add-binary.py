class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        
        # Run loop until both strings are processed AND no carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry  # Start with previous carry
            
            if i >= 0:
                total += int(a[i]) # Add bit from a
                i -= 1
            if j >= 0:
                total += int(b[j]) # Add bit from b
                j -= 1
            
            # total can be 0, 1, 2, or 3
            # Append the remainder (0 or 1) to result
            res.append(str(total % 2))
            
            # Update carry (0 or 1)
            carry = total // 2
            
        # The result is currently backwards, so reverse it and join
        return ''.join(reversed(res))