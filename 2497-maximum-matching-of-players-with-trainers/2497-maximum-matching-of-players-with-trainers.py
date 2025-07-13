class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Step 1: Sort both arrays to enable a greedy approach.
        # Sorting allows us to match the weakest players with the weakest possible trainers first.
        players.sort()
        trainers.sort()
        
        # Step 2: Initialize pointers for both arrays and a counter for matches.
        player_ptr = 0  # Points to the current player
        trainer_ptr = 0 # Points to the current trainer
        count = 0       # Stores the number of successful matches
        
        # Get the lengths of the arrays for the loop condition.
        num_players = len(players)
        num_trainers = len(trainers)
        
        # Step 3: Iterate while there are still players and trainers to consider.
        while player_ptr < num_players and trainer_ptr < num_trainers:
            # Check if the current player can be matched with the current trainer.
            if players[player_ptr] <= trainers[trainer_ptr]:
                # Successful Match!
                # This player's ability is within the trainer's capacity.
                count += 1
                player_ptr += 1  # Move to the next player.
                trainer_ptr += 1 # This trainer is now used, so move to the next.
            else:
                # No Match. The current trainer is not strong enough for the current player.
                # Since the arrays are sorted, this trainer won't be strong enough for any subsequent players either.
                # So, we discard this trainer and check if the next trainer can handle the current player.
                trainer_ptr += 1
                
        # Step 4: Return the total count of matches found.
        return count