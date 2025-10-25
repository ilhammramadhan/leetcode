class Solution:
    def totalMoney(self, n: int) -> int:
        
        # 1. Initialize the total amount of money saved.
        total_money = 0
        
        # 2. We will loop n times, once for each day. 
        #    We use 'day' as an index from 0 to n-1.
        #    - day 0 = 1st day (Monday of week 0)
        #    - day 6 = 7th day (Sunday of week 0)
        #    - day 7 = 8th day (Monday of week 1)
        for day in range(n):
            
            # 3. Find the current week number.
            #    Integer division by 7 tells us how many full weeks have passed.
            #    - Days 0-6:  day // 7 = 0 (This is Week 0)
            #    - Days 7-13: day // 7 = 1 (This is Week 1)
            week_number = day // 7
            
            # 4. Find the specific day within the week.
            #    The modulo operator gives us the remainder.
            #    - Day 0: 0 % 7 = 0 (Monday)
            #    - Day 1: 1 % 7 = 1 (Tuesday)
            #    - ...
            #    - Day 7: 7 % 7 = 0 (Monday)
            day_of_week = day % 7
            
            # 5. Calculate the deposit amount for this specific day.
            
            #    First, find the "base" deposit for this week's Monday.
            #    - Week 0: Starts with $1
            #    - Week 1: Starts with $2
            #    - The rule is: (week_number + 1)
            monday_deposit = week_number + 1
            
            #    Now, find the actual deposit for the current day.
            #    It's the Monday deposit plus the day of the week.
            #    - Example (Day 0): $1 (monday_deposit) + 0 (day_of_week) = $1
            #    - Example (Day 3): $1 (monday_deposit) + 3 (day_of_week) = $4
            #    - Example (Day 9): 
            #        - week_number = 9 // 7 = 1
            #        - day_of_week = 9 % 7 = 2
            #        - monday_deposit = 1 + 1 = $2
            #        - deposit_today = $2 + 2 = $4
            deposit_today = monday_deposit + day_of_week
            
            # 6. Add this day's deposit to our running total.
            total_money += deposit_today
            
        # 7. After the loop has run for all n days, return the final total.
        return total_money