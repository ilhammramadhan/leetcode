class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        # Total operations needed
        total_operations = 0
        
        # The "height" of the array at the previous position.
        # We start at 0, representing the initial all-zero array.
        previous_value = 0
        
        # Iterate through each number (current_value) in the target array
        for current_value in target:
            
            # The core logic: we only need to add new operations
            # if the current target value is GREATER than the previous one.
            # This represents an "uphill climb" in the skyline.
            if current_value > previous_value:
                
                # The number of new operations required is the
                # difference between the current value and the
                # value we already built up from the previous steps.
                new_operations = current_value - previous_value
                total_operations += new_operations
            
            # If current_value <= previous_value, it's a "downhill" or
            # "flat" step. The operations we've already counted are 
            # sufficient. We don't need to add anything.
            
            # Update the previous_value for the next iteration
            previous_value = current_value
            
        return total_operations