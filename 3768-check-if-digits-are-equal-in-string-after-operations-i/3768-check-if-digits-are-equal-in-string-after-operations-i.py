class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Step 1: Keep looping as long as the string has more than 2 digits.
        while len(s) > 2:
            
            # Step 2: Create a temporary list to build the next version of the string.
            next_s = []
            
            # Step 3: Iterate through the string to get all consecutive pairs.
            # We stop at len(s) - 1 because the last pair starts at index len(s) - 2.
            for i in range(len(s) - 1):
                
                # Step 4: Get the two digits as integers and calculate the new digit.
                digit1 = int(s[i])
                digit2 = int(s[i+1])
                new_digit = (digit1 + digit2) % 10
                
                # Step 5: Add the new digit (as a string) to our list.
                next_s.append(str(new_digit))
            
            # Step 6: Replace the old string 's' with the new one we just built.
            # "".join(['2', '9', '2']) becomes "292"
            s = "".join(next_s)
        
        # Step 7: The loop is finished. 's' now has exactly 2 digits.
        # Return True if the first and second digits are the same, otherwise False.
        return s[0] == s[1]