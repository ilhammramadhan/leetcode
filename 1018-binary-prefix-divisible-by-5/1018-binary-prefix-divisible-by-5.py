from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        remainder = 0
        
        for bit in nums:
            # Update the remainder using the formula: (prev * 2 + bit) % 5
            remainder = (remainder * 2 + bit) % 5
            
            # Check divisibility: if remainder is 0, it is divisible by 5
            if remainder == 0:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer