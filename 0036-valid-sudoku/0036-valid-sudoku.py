import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize data structures to track seen numbers.
        # defaultdict(set) creates a new set for a key if it doesn't exist.
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        boxes = collections.defaultdict(set)  # key will be a tuple: (r // 3, c // 3)

        # Iterate through each cell of the 9x9 board.
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                # If the cell is empty, skip it.
                if num == ".":
                    continue

                # --- VALIDATION CHECKS ---
                # 1. Check if the number is already in the current row's set.
                # 2. Check if the number is already in the current column's set.
                # 3. Check if the number is already in the current 3x3 box's set.
                box_key = (r // 3, c // 3)
                if (num in rows[r] or
                    num in cols[c] or
                    num in boxes[box_key]):
                    # If a duplicate is found, the board is invalid.
                    return False

                # --- UPDATE SETS ---
                # If no duplicates were found, add the number to all three sets for tracking.
                cols[c].add(num)
                rows[r].add(num)
                boxes[box_key].add(num)

        # If the entire board is traversed without finding any duplicates, it is valid.
        return True