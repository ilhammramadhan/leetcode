class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        Given a list of folders, returns the folders after removing all sub-folders.

        The method works by first sorting the folder paths alphabetically. This clever step
        ensures that any parent folder (e.g., "/a") will appear immediately before its
        sub-folders (e.g., "/a/b", "/a/c") in the list.

        With the list sorted, we can iterate through it and build our result. We keep track
        of the last valid parent folder we've added. If the current folder path starts with
        the last parent's path followed by a '/', it's a sub-folder and we can safely
        ignore it. Otherwise, it's a new, distinct parent folder, and we add it to our
        result list.
        """
        
        # Sort the folder list alphabetically. This is the key step.
        # A parent folder like "/a" will now be guaranteed to come before
        # any of its sub-folders like "/a/b".
        folder.sort()
        
        # Initialize the result list. We can add the first folder from the
        # sorted list, as it cannot be a sub-folder of anything that came before it.
        result = [folder[0]]
        
        # Iterate through the rest of the sorted list, starting from the second folder.
        for i in range(1, len(folder)):
            # Get the last valid parent folder added to our result.
            last_parent = result[-1]
            
            # Check if the current folder is a sub-folder of the last parent.
            # A true sub-folder must start with the parent's path AND be
            # immediately followed by a '/'.
            # For example, "/a/b" starts with "/a/".
            # This check correctly handles cases like "/a/b/c" vs "/a/b/ca".
            if not folder[i].startswith(last_parent + '/'):
                # If it's not a sub-folder, it's a new top-level folder.
                # Add it to our result.
                result.append(folder[i])
                
        return result