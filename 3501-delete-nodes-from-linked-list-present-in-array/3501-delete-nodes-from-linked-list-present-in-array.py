# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Step 1: Create a hash set for efficient O(1) lookups.
        nums_set = set(nums)
        
        # Step 2: Create a dummy node to handle head-deletion edge cases.
        dummy = ListNode(0)
        dummy.next = head
        
        # Step 3: Initialize 'prev' (last kept node) and 'curr' (current node).
        prev = dummy
        curr = head
        
        # Step 4: Iterate and rewire the list.
        while curr:
            if curr.val in nums_set:
                # Case 1: Delete 'curr'.
                # Bypass 'curr' by pointing 'prev.next' to 'curr.next'.
                # We don't advance 'prev' because the next node might also need deletion.
                prev.next = curr.next
            else:
                # Case 2: Keep 'curr'.
                # 'curr' is now the "last kept node", so advance 'prev'.
                prev = curr
            
            # Advance 'curr' in all cases to continue the loop.
            curr = curr.next
            
        # Step 5: Return the new head, which is dummy.next.
        return dummy.next