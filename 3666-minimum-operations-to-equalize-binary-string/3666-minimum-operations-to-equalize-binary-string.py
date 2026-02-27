from collections import deque
import bisect

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z_start = s.count('0')
        if z_start == 0: return 0
        
        # Separate unvisited counts into even and odd to handle the step-2 jump
        unvisited_even = sorted([i for i in range(0, n + 1, 2) if i != z_start])
        unvisited_odd = sorted([i for i in range(1, n + 1, 2) if i != z_start])
        
        queue = deque([(z_start, 0)])
        
        while queue:
            curr_z, dist = queue.popleft()
            
            # Theoretical min and max zeros we can have after one flip of k bits:
            # i = number of zeros flipped to ones.
            # max_i = min(curr_z, k)
            # min_i = max(0, k - (n - curr_z))
            
            # next_z = curr_z + k - 2*i
            # To get the SMALLEST next_z, we use MAX_I
            # To get the LARGEST next_z, we use MIN_I
            
            low = curr_z + k - 2 * min(curr_z, k)
            high = curr_z + k - 2 * max(0, k - (n - curr_z))
            
            # The next_z values will always have the same parity (low % 2)
            target_list = unvisited_even if low % 2 == 0 else unvisited_odd
            
            # Find the range of indices in the target_list that fall between [low, high]
            left_idx = bisect.bisect_left(target_list, low)
            right_idx = bisect.bisect_right(target_list, high)
            
            # Elements to visit
            to_visit = target_list[left_idx:right_idx]
            
            for next_z in to_visit:
                if next_z == 0:
                    return dist + 1
                queue.append((next_z, dist + 1))
            
            # Crucial optimization: Remove visited elements from the unvisited list 
            # so we never look at them again.
            del target_list[left_idx:right_idx]
                    
        return -1