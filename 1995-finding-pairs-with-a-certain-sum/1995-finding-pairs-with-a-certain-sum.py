class FindSumPairs:
    """
    A data structure to find pairs of numbers from two lists that sum up to a target value.
    It supports efficiently updating the second list.
    """

    def __init__(self, nums1: List[int], nums2: List[int]):
        """
        Initializes the data structure.
        - Stores nums1 and nums2.
        - Creates a frequency map (Counter) for nums2 for fast lookups.
        
        Time Complexity: O(len(nums1) + len(nums2))
        """
        self.nums1 = nums1
        self.nums2 = nums2
        # Use a Counter to store the frequency of each number in nums2.
        # This is the key optimization for the `count` method.
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        """
        Adds a value to an element in nums2 and updates the frequency map.
        
        Time Complexity: O(1) on average for hash map operations.
        """
        # Get the original value at the index before it's changed.
        old_val = self.nums2[index]
        
        # Decrement the frequency count of the old value.
        self.freq[old_val] -= 1
        
        # Perform the addition to update the value in the nums2 array.
        new_val = old_val + val
        self.nums2[index] = new_val
        
        # Increment the frequency count of the new value.
        self.freq[new_val] += 1

    def count(self, tot: int) -> int:
        """
        Counts the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.
        
        Time Complexity: O(len(nums1)) because we iterate through nums1 and perform
                         a constant time hash map lookup for each element.
        """
        total_pairs = 0
        # Iterate through each number in the first list.
        for num1 in self.nums1:
            # For each num1, calculate the complement needed to reach the total.
            target = tot - num1
            
            # Use the frequency map to find how many times this complement
            # exists in nums2. self.freq.get(target, 0) returns 0 if target is not in the map.
            total_pairs += self.freq.get(target, 0)
            
        return total_pairs