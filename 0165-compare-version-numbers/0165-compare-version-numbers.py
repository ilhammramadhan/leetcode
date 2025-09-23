class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Step 1: Split the strings into lists of revision numbers.
        v1_revisions = version1.split('.')
        v2_revisions = version2.split('.')
        
        len1 = len(v1_revisions)
        len2 = len(v2_revisions)
        
        # Step 2: Determine the maximum number of revisions to check.
        max_len = max(len1, len2)
        
        # Step 3: Iterate and compare each revision from left to right.
        for i in range(max_len):
            # Get the revision value for version1, defaulting to 0 if it doesn't exist.
            # int() handles leading zeros like "01" -> 1.
            rev1 = int(v1_revisions[i]) if i < len1 else 0
            
            # Get the revision value for version2, defaulting to 0 if it doesn't exist.
            rev2 = int(v2_revisions[i]) if i < len2 else 0
            
            # Compare the integer values of the revisions.
            if rev1 > rev2:
                return 1  # version1 is greater
            elif rev1 < rev2:
                return -1 # version2 is greater
        
        # Step 4: If the loop completes, the versions are equal.
        return 0