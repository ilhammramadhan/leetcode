class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        # Step 1: Loop through all valid hours (0-11)
        for h in range(12):
            # Step 1: Loop through all valid minutes (0-59)
            for m in range(60):
                
                # Step 2: Count the 1s (LEDs) in both hour and minute
                # bin(h) converts h to binary (e.g., 5 -> '0b101')
                # .count('1') counts the number of '1's in that string
                total_leds = bin(h).count('1') + bin(m).count('1')
                
                # Step 3: Check if the total LEDs match the input
                if total_leds == turnedOn:
                    
                    # Step 4: Format the time string correctly
                    # {m:02d} ensures minutes like '5' become '05'
                    time_str = f"{h}:{m:02d}"
                    result.append(time_str)
                    
        return result