class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid is less than or equal to target, 
            # we need to look at the right side (larger values)
            if letters[mid] <= target:
                left = mid + 1
            # If mid is greater, it's a candidate, 
            # but we try to find a smaller one to the left
            else:
                right = mid
        
        # If left reaches the end of the array, wrap around to 0
        return letters[left % len(letters)]