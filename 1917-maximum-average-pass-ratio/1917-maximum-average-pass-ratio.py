import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        # Helper function to calculate the gain for a class
        def calculate_gain(p, t):
            # The increase in ratio by adding one student
            return (p + 1) / (t + 1) - p / t

        # Step 1: Create a max-heap (using negative gains with a min-heap)
        # The heap will store tuples: (-gain, pass_count, total_count)
        max_heap = []
        for p, t in classes:
            # We don't add classes that are already perfect (p==t) because their gain is 0
            if p < t:
                heapq.heappush(max_heap, (-calculate_gain(p, t), p, t))

        # Step 2: Distribute the extra students
        for _ in range(extraStudents):
            # If the heap is empty (all classes are perfect), we can't do anything.
            if not max_heap:
                break
            
            # Pop the class with the highest potential gain
            neg_gain, p, t = heapq.heappop(max_heap)
            
            # Update its student counts
            p_new, t_new = p + 1, t + 1
            
            # If the updated class can still be improved, calculate its new gain
            # and push it back onto the heap.
            if p_new < t_new:
                new_neg_gain = -calculate_gain(p_new, t_new)
                heapq.heappush(max_heap, (new_neg_gain, p_new, t_new))

        # Step 3: Calculate the final average ratio
        total_ratio = 0
        
        # Add the ratios from the classes that were modified and are now in the heap
        for neg_gain, p, t in max_heap:
            total_ratio += p / t
            
        # Count the number of classes that were already perfect (p==t)
        # and were never added to the heap. Their ratio is 1.
        perfect_classes = len(classes) - len(max_heap)
        total_ratio += perfect_classes
        
        return total_ratio / len(classes)