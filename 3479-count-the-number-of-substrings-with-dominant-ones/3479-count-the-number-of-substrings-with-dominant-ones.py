import bisect

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        
        # 1. Pre-calculate the indices of all '0's.
        #    This lets us "jump" from one zero to the next.
        zeros_idx = [idx for idx, char in enumerate(s) if char == '0']
        
        # Get the number of zeros
        m = len(zeros_idx)
        
        # 2. Add a "sentinel" value at the end.
        #    This represents the "zero" at the end of the string.
        #    It simplifies boundary checks.
        zeros_idx.append(n)

        # 3. Iterate through every possible start index `i`.
        for i in range(n):
            
            # `ones` and `zeros` count for the substring s[i..j]
            ones = 0
            
            # 4. Find the first zero at or after index `i`.
            #    `p` will be the index *in zeros_idx* of this first zero.
            #    bisect_left finds this efficiently.
            p = bisect.bisect_left(zeros_idx, i)
            
            # 5. Handle the first block: substrings with `zeros = 0`.
            #    These are all substrings s[i..j] that are all '1's.
            #    This block of '1's starts at `i` and ends right before
            #    the first zero (at zeros_idx[p]).
            
            first_zero_pos = zeros_idx[p]
            num_initial_ones = first_zero_pos - i
            
            # All substrings s[i..i], s[i..i+1], ..., s[i..first_zero_pos-1]
            # have zeros=0 and ones >= 1.
            # The condition ones >= 0*0 is always true.
            # There are `num_initial_ones` such substrings.
            count += num_initial_ones
            
            # Update our `ones` count for this starting `i`.
            ones = num_initial_ones

            # 6. Now, iterate through the zeros, one by one, starting from p.
            #    `k_idx` is the index in `zeros_idx`.
            for k_idx in range(p, m):
                # `zeros` is the number of zeros we have seen *so far*
                # for this `i`.
                zeros = (k_idx - p + 1)
                
                # 7. This is the O(sqrt(n)) optimization.
                #    If zeros*zeros > n, no future substring
                #    starting at `i` can ever be valid.
                if zeros * zeros > n:
                    break
                    
                # 8. Check the substring ending *at* this new zero.
                #    The substring is s[i ... zeros_idx[k_idx]].
                #    The `ones` count is still from the previous block.
                if ones >= zeros * zeros:
                    count += 1
                    
                # 9. Find the next block of '1's.
                #    It's between the zero we just processed (zeros_idx[k_idx])
                #    and the *next* zero (zeros_idx[k_idx + 1]).
                start_of_ones_block = zeros_idx[k_idx] + 1
                end_of_ones_block = zeros_idx[k_idx + 1] - 1
                
                # Length of this block of '1's
                L = end_of_ones_block - start_of_ones_block + 1

                if L > 0:
                    # 10. We need to find how many '1's we *need*
                    #     to make the condition true.
                    needed_ones = (zeros * zeros) - ones
                    
                    if needed_ones <= 0:
                        # We already have enough ones.
                        # All `L` substrings ending in this '1's block are valid.
                        count += L
                    elif needed_ones <= L:
                        # We need `needed_ones` more.
                        # The substrings that add `needed_ones`, `needed_ones+1`, ..., `L`
                        # '1's are valid.
                        # This gives (L - needed_ones + 1) valid substrings.
                        count += (L - needed_ones + 1)
                    
                    # 11. Add all the '1's from this block to our
                    #     running `ones` total for the next iteration.
                    ones += L
                    
        return count