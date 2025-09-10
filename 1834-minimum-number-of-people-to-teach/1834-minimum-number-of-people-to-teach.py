from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Step 1.1: Convert language lists to sets for efficient lookups.
        # Note: User IDs are 1-based, list indices are 0-based.
        # languages_sets[i] corresponds to user i+1.
        languages_sets = [set(lang) for lang in languages]
        m = len(languages)

        # Step 1.2 & 1.3: Identify all unique users in non-communicating friendships.
        unconnected_users = set()
        for u, v in friendships:
            # Adjust for 0-based indexing
            user1_idx = u - 1
            user2_idx = v - 1
            
            # Check for common languages using set intersection.
            # The '&' operator performs set intersection.
            if not (languages_sets[user1_idx] & languages_sets[user2_idx]):
                unconnected_users.add(u)
                unconnected_users.add(v)
        
        # Edge case: If everyone can already communicate, no teaching is needed.
        if not unconnected_users:
            return 0

        # Step 2: Find the most popular language among the unconnected users.
        # We create a frequency map for languages 1 to n.
        # The array is of size n+1 for convenient 1-based indexing of languages.
        lang_counts = [0] * (n + 1)
        
        for user_id in unconnected_users:
            user_idx = user_id - 1
            # For each language this user knows, increment its popularity count.
            for lang in languages_sets[user_idx]:
                lang_counts[lang] += 1
        
        # Step 3: Calculate the result.
        # The best language to teach is the one most known among the group.
        # max(lang_counts) gives us the count of the most popular language.
        max_known = max(lang_counts)
        
        # The number of people to teach is the total number of people needing help
        # minus the number of people who ALREADY know the most popular language.
        return len(unconnected_users) - max_known