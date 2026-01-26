class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # 1. Sort the array to bring close numbers together
        arr.sort()
        
        min_diff = float('inf')
        res = []
        
        # 2. Iterate through the sorted array once
        for i in range(len(arr) - 1):
            current_diff = arr[i+1] - arr[i]
            
            # If we find a NEW smaller difference
            if current_diff < min_diff:
                min_diff = current_diff
                # Reset the result list with this new closest pair
                res = [[arr[i], arr[i+1]]]
                
            # If the difference matches our current minimum
            elif current_diff == min_diff:
                res.append([arr[i], arr[i+1]])
                
        return res