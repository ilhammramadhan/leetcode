class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        """
        Calculates the total number of laser beams in the bank.

        The logic is to iterate through the rows, keeping track of the
        device count in the *previous row that had devices*.
        When we find a new row with devices, we multiply its
        device count by the previous count and add it to the total.
        """
        
        total_beams = 0
        prev_device_count = 0

        # Iterate through each row in the bank floor plan
        for row_str in bank:
            # Count the number of security devices ('1's) in the current row
            curr_device_count = row_str.count('1')

            # If the current row is empty (no devices), we skip it.
            # It's just a gap. We don't update prev_device_count.
            if curr_device_count > 0:
                # This row has devices.
                # If we have a 'previous' row with devices (prev_device_count > 0),
                # it means we can form beams between the previous device-row
                # and this current device-row.
                
                # The number of beams is prev_count * curr_count.
                total_beams += (prev_device_count * curr_device_count)
                
                # Now, this current row becomes the 'previous' row
                # for the next non-empty row we find.
                prev_device_count = curr_device_count

        # After checking all rows, return the total.
        return total_beams