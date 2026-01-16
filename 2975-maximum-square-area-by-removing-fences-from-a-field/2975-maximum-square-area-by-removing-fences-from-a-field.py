class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # Add the boundary fences 1 and m/n
        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])
        
        # Calculate all possible horizontal distances
        h_gaps = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_gaps.add(h[j] - h[i])
        
        max_side = -1
        
        # Check vertical distances against horizontal distances
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                gap = v[j] - v[i]
                if gap in h_gaps:
                    max_side = max(max_side, gap)
        
        if max_side == -1:
            return -1
        
        # Return area modulo 10^9 + 7
        return (max_side * max_side) % (10**9 + 7)