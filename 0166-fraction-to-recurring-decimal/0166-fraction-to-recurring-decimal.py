class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle sign
        sign = ""
        if numerator * denominator < 0:
            sign = "-"
        
        # Use absolute values for calculation
        num = abs(numerator)
        den = abs(denominator)

        # Handle zero numerator
        if num == 0:
            return "0"
        
        # Calculate integer part
        integer_part = str(num // den)
        remainder = num % den

        # If remainder is zero, no decimal part
        if remainder == 0:
            return sign + integer_part

        result = [integer_part, "."]
        remainder_map = {}
        
        # Start of the long division for the decimal part
        while remainder != 0:
            # Check if this remainder has been seen before
            if remainder in remainder_map:
                # Found a repeating cycle!
                # Insert the opening parenthesis at the start of the repeating sequence
                # and the closing parenthesis at the end.
                start_index = remainder_map[remainder]
                result.insert(start_index, "(")
                result.append(")")
                break  # Exit the loop
            
            # Store the current remainder and the index where its digit will be placed
            remainder_map[remainder] = len(result)
            
            # Perform the next step of long division
            remainder *= 10
            digit = remainder // den
            result.append(str(digit))
            remainder %= den
            
        return sign + "".join(result)