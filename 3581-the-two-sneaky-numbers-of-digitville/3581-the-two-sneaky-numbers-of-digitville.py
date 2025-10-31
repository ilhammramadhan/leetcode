from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # 1. Prepare your tools
        seen = set()
        duplicates = []
        
        # 2. Interview every number in the list
        for num in nums:
            # 3. Check your notepad (the 'seen' set)
            if num in seen:
                # Case 1: Already seen? It's a culprit.
                duplicates.append(num)
            else:
                # Case 2: First time? Add it to the notepad.
                seen.add(num)
                
        # 4. Present the findings
        return duplicates