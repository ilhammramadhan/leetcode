class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # Step 1: Process the inputs
        words = text.split(' ')  # Split text into a list of words
        broken_set = set(brokenLetters) # Convert broken letters to a set for fast lookups

        # Step 2 & 3: Initialize counter, iterate, check, and count
        typeable_count = 0  # Initialize the counter for valid words

        for word in words:
            # Assume the word is not broken initially
            is_broken = False 
            
            # Check each letter in the word
            for letter in word:
                # If a letter is in the broken set, mark the word as broken
                if letter in broken_set:
                    is_broken = True
                    break # No need to check other letters in this word
            
            # If the word was never marked as broken, it's typeable
            if not is_broken:
                typeable_count += 1
                
        return typeable_count