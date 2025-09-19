class Spreadsheet:
    def __init__(self, rows: int):
        # A 2D list to represent the spreadsheet grid.
        # Dimensions are rows x 26 columns ('A' through 'Z').
        # All cells are initialized to 0.
        self.rows = rows
        self.grid = [[0] * 26 for _ in range(rows)]

    def _parse_cell(self, cell: str) -> tuple[int, int]:
        """Helper to parse a cell string like 'A1' into 0-indexed (row, col) coordinates."""
        col_char = cell[0]
        row_str = cell[1:]
        
        col = ord(col_char) - ord('A')
        row = int(row_str) - 1
        
        return row, col

    def setCell(self, cell: str, value: int) -> None:
        row, col = self._parse_cell(cell)
        self.grid[row][col] = value

    def resetCell(self, cell: str) -> None:
        row, col = self._parse_cell(cell)
        self.grid[row][col] = 0

    def getValue(self, formula: str) -> int:
        # Remove the leading '=' and split the formula by '+'
        operands = formula[1:].split('+')
        
        total_sum = 0
        for op in operands:
            if op.isdigit():
                # If the operand is a number
                total_sum += int(op)
            else:
                # If the operand is a cell reference
                row, col = self._parse_cell(op)
                total_sum += self.grid[row][col]
                
        return total_sum