import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        
        # Doubly Linked List nodes
        # [value, prev_idx, next_idx, exists]
        list_nodes = [[nums[i], i - 1, i + 1, True] for i in range(n)]
        list_nodes[n-1][2] = -1 # End of list
        
        # Priority Queue stores: (sum, left_index)
        pq = []
        for i in range(n - 1):
            heapq.heappush(pq, (nums[i] + nums[i+1], i))
            
        def is_sorted():
            curr = 0
            # Find the first existing node
            while curr < n and not list_nodes[curr][3]:
                curr += 1
            
            while curr != -1:
                nxt = list_nodes[curr][2]
                while nxt != -1 and not list_nodes[nxt][3]:
                    nxt = list_nodes[nxt][2]
                if nxt != -1 and list_nodes[curr][0] > list_nodes[nxt][0]:
                    return False
                curr = nxt
            return True

        # To avoid O(N) sorted check, we track violations
        violations = 0
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                violations += 1
                
        ops = 0
        
        while violations > 0:
            # 1. Get the true leftmost minimum sum
            while pq:
                s, left_idx = heapq.heappop(pq)
                
                # Check if this pair is still valid and adjacent
                if not list_nodes[left_idx][3]: continue
                right_idx = list_nodes[left_idx][2]
                if right_idx == -1 or not list_nodes[right_idx][3]: continue
                
                # Verify the sum is still current (in case nodes changed)
                if list_nodes[left_idx][0] + list_nodes[right_idx][0] != s:
                    continue
                
                # If we made it here, this is the leftmost minimum pair
                # --- MERGE PROCESS ---
                
                # Remove old violations involving left, right, and their neighbors
                # Neighbor L_Prev
                lp_idx = list_nodes[left_idx][1]
                if lp_idx != -1:
                    if list_nodes[lp_idx][0] > list_nodes[left_idx][0]: violations -= 1
                
                # The pair itself
                if list_nodes[left_idx][0] > list_nodes[right_idx][0]: violations -= 1
                
                # Neighbor R_Next
                rn_idx = list_nodes[right_idx][2]
                if rn_idx != -1:
                    if list_nodes[right_idx][0] > list_nodes[rn_idx][0]: violations -= 1
                
                # Perform the merge: left_idx absorbs the sum, right_idx is deleted
                list_nodes[left_idx][0] = s
                list_nodes[right_idx][3] = False # Mark as deleted
                
                # Update pointers
                new_next_idx = list_nodes[right_idx][2]
                list_nodes[left_idx][2] = new_next_idx
                if new_next_idx != -1:
                    list_nodes[new_next_idx][1] = left_idx
                
                # Add new violations
                if lp_idx != -1:
                    if list_nodes[lp_idx][0] > list_nodes[left_idx][0]: violations += 1
                if new_next_idx != -1:
                    if list_nodes[left_idx][0] > list_nodes[new_next_idx][0]: violations += 1
                
                ops += 1
                
                # If sorted, exit early
                if violations == 0: return ops
                
                # Push new potential pairs to heap
                if lp_idx != -1:
                    heapq.heappush(pq, (list_nodes[lp_idx][0] + list_nodes[left_idx][0], lp_idx))
                if new_next_idx != -1:
                    heapq.heappush(pq, (list_nodes[left_idx][0] + list_nodes[new_next_idx][0], left_idx))
                
                break # Move to next operation
                
        return ops