import collections

class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        # Step 1: Pre-processing and Grouping
        counts = collections.Counter(power)
        unique_powers = sorted(counts.keys())
        
        n = len(unique_powers)
        dp = [0] * n

        # Step 2 & 3: Base Case and Iteration
        # Base case: For the first spell type, we must take it.
        dp[0] = unique_powers[0] * counts[unique_powers[0]]

        for i in range(1, n):
            current_power = unique_powers[i]
            current_damage = current_power * counts[current_power]

            # Option 1: Skip the current spell type.
            # The max damage is the same as the max damage from the previous spell type.
            damage_if_skip = dp[i-1]
            
            # Option 2: Take the current spell type.
            damage_if_take = current_damage
            
            # Find the last compatible spell. We need to find the index 'j' of a spell
            # where unique_powers[j] < current_power - 2.
            # We can search backwards for simplicity, but binary search is more optimal.
            
            # This is a simple linear search backwards.
            prev_compatible_damage = 0
            for j in range(i - 1, -1, -1):
                if unique_powers[j] < current_power - 2:
                    prev_compatible_damage = dp[j]
                    break # Found the latest one
            
            damage_if_take += prev_compatible_damage

            # The dp value for this state is the max of the two choices.
            dp[i] = max(damage_if_skip, damage_if_take)
            
        # The final answer is the maximum damage possible considering all spell types.
        return dp[-1]