class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # If "01" is in the string, there is more than one segment of 1s.
        # Therefore, we return True only if "01" is NOT in s.
        return "01" not in s