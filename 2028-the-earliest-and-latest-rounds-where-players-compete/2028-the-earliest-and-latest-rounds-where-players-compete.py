class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        """
        Calculates the earliest and latest rounds for the meeting of two players
        by directly simulating the tournament's pairing rules.
        """
        
        # lru_cache handles the memoization. The state is the sorted tuple of remaining players.
        @lru_cache(None)
        def solve(players: tuple) -> list[int]:
            m = len(players)
            
            # Find the current positions of the two special players.
            p1_pos = players.index(firstPlayer) + 1
            p2_pos = players.index(secondPlayer) + 1

            # Base Case: The players compete in this round if their positions sum to m + 1.
            if p1_pos + p2_pos == m + 1:
                return [1, 1]

            # --- Recursive Step: Simulate the Round ---
            
            fixed_winners = set()
            choosable_matches = []
            
            # Identify the fixed winners and matches where we can choose the outcome.
            for i in range(m // 2):
                player_a = players[i]
                player_b = players[m - 1 - i]
                
                # If a match involves a special player, the outcome is fixed.
                if player_a in (firstPlayer, secondPlayer) or player_b in (firstPlayer, secondPlayer):
                    if player_a == firstPlayer or player_b == firstPlayer:
                        fixed_winners.add(firstPlayer)
                    if player_a == secondPlayer or player_b == secondPlayer:
                        fixed_winners.add(secondPlayer)
                else:
                    # Otherwise, we can choose the winner of this match.
                    choosable_matches.append((player_a, player_b))

            # If the number of players is odd, the middle player advances automatically.
            if m % 2 == 1:
                fixed_winners.add(players[m // 2])

            min_rounds = float('inf')
            max_rounds = float('-inf')

            # Explore every possible outcome of the choosable matches (2^C possibilities).
            num_choosable = len(choosable_matches)
            for i in range(1 << num_choosable):
                # Start with the winners whose outcomes are fixed.
                current_winners = set(fixed_winners)
                
                # Use a bitmask to determine the winner for each choosable match.
                for j in range(num_choosable):
                    if (i >> j) & 1:
                        current_winners.add(choosable_matches[j][0]) # Pick first player in the pair
                    else:
                        current_winners.add(choosable_matches[j][1]) # Pick second player in the pair
                
                # Create the sorted tuple of players for the next round.
                next_players = tuple(sorted(list(current_winners)))
                
                # Recursively solve for the next state.
                sub_result = solve(next_players)
                
                min_rounds = min(min_rounds, sub_result[0])
                max_rounds = max(max_rounds, sub_result[1])

            # The result for this state is 1 (for the current round) + the result from subproblems.
            return [min_rounds + 1, max_rounds + 1]

        # Start the simulation with the initial list of all players.
        initial_players = tuple(range(1, n + 1))
        return solve(initial_players)