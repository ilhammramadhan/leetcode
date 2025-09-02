class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0  # Start our count at zero

        # Step 1: Iterate through all possible points for A and B
        for i in range(n):
            for j in range(n):
                # A and B must be different points
                if i == j:
                    continue

                x_a, y_a = points[i]
                x_b, y_b = points[j]

                # Step 2: Check if A is upper-left of B
                if x_a <= x_b and y_a >= y_b:
                    # This pair is a candidate. Assume it's valid until proven otherwise.
                    is_valid_pair = True

                    # Step 3: Check if any other point C is inside the rectangle
                    for k in range(n):
                        # C can't be A or B
                        if k == i or k == j:
                            continue

                        x_c, y_c = points[k]

                        # Check if C lies within the bounding box of A and B
                        if x_a <= x_c <= x_b and y_b <= y_c <= y_a:
                            # We found a point inside! This pair is not valid.
                            is_valid_pair = False
                            break  # No need to check other points for this (A, B) pair

                    # Step 4: If after checking all other points, the pair is still valid...
                    if is_valid_pair:
                        count += 1 # ...increment the count!

        return count