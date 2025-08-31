from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle by modifying the board in-place using an
        optimized backtracking algorithm with sets for O(1) validity checks.
        """
        # --- Optimization Setup ---
        # Create sets to keep track of numbers in each row, column, and 3x3 box.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # A list to store the coordinates of all empty cells to iterate over.
        empty_cells = []

        # --- Pre-processing Step ---
        # Populate the sets with initial numbers and find all empty cells.
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    empty_cells.append((r, c))
                else:
                    # Calculate the index for the 3x3 box.
                    box_index = (r // 3) * 3 + (c // 3)
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

        # --- Start the Backtracking Process ---
        # This function will modify the board directly.
        self.solve(board, empty_cells, 0, rows, cols, boxes)

    def solve(self, board, empty_cells, index, rows, cols, boxes) -> bool:
        """
        The main recursive function that implements optimized backtracking.
        'index' tracks which empty cell we are currently trying to fill.
        """
        # Base case: If the index matches the total number of empty cells,
        # it means we have successfully filled them all.
        if index == len(empty_cells):
            return True

        r, c = empty_cells[index]
        box_index = (r // 3) * 3 + (c // 3)

        # Try placing numbers '1' through '9'.
        for i in range(1, 10):
            num_str = str(i)
            
            # --- Optimized Validity Check (O(1) lookup time) ---
            if (num_str not in rows[r] and
                num_str not in cols[c] and
                num_str not in boxes[box_index]):
                
                # If the number is valid, place it on the board and update our sets.
                board[r][c] = num_str
                rows[r].add(num_str)
                cols[c].add(num_str)
                boxes[box_index].add(num_str)

                # Recursively try to solve for the next empty cell.
                if self.solve(board, empty_cells, index + 1, rows, cols, boxes):
                    return True

                # --- Backtrack ---
                # If the recursive call returned False, it was a dead end.
                # We must undo the move by resetting the cell and removing the number
                # from our tracking sets.
                board[r][c] = '.'
                rows[r].remove(num_str)
                cols[c].remove(num_str)
                boxes[box_index].remove(num_str)
        
        # If no number from 1-9 worked for this cell, return False
        # to trigger backtracking in the previous function call.
        return False

