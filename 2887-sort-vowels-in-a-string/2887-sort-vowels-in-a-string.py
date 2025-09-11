class Solution:
    def sortVowels(self, s: str) -> str:
        # Step 1: Identify and Collect All Vowels
        vowels_list = []
        VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for char in s:
            if char in VOWELS:
                vowels_list.append(char)
        
        # Step 2: Sort the Collected Vowels
        vowels_list.sort()
        
        # Step 3: Build the Result String
        s_list = list(s)
        vowel_idx = 0
        for i in range(len(s_list)):
            # If the character is a vowel, replace it with the next sorted vowel
            if s_list[i] in VOWELS:
                s_list[i] = vowels_list[vowel_idx]
                vowel_idx += 1
                
        # Join the list of characters back into a string
        return "".join(s_list)