from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        
        # Step 1: Look at each word in our queries array
        for query in queries:
            # Step 2: Compare the current query against words in the dictionary
            for word in dictionary:
                differences = 0
                
                # Step 3: Compare them character by character
                for i in range(len(query)):
                    if query[i] != word[i]:
                        differences += 1
                        
                    # Step 4: Early stopping - if it takes more than 2 edits, stop checking this word
                    if differences > 2:
                        break
                
                # Step 5: If we found a valid match (<= 2 edits), save it and move to the next query
                if differences <= 2:
                    result.append(query)
                    break # We found a match, no need to check the rest of the dictionary
                    
        return result