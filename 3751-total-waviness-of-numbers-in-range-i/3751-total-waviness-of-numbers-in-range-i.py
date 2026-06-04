class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        
        # Iterate through every number in the inclusive range
        for num in range(num1, num2 + 1):
            s = str(num)
            n = len(s)
            
            # Any number with fewer than 3 digits has a waviness of 0
            if n < 3:
                continue
                
            # Check middle digits for peaks and valleys
            for i in range(1, n - 1):
                # Check for Peak
                if s[i] > s[i-1] and s[i] > s[i+1]:
                    total_waviness += 1
                # Check for Valley
                elif s[i] < s[i-1] and s[i] < s[i+1]:
                    total_waviness += 1
                    
        return total_waviness