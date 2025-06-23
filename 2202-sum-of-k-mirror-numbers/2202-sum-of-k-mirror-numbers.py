class Solution:
    def kMirror(self, k: int, n: int) -> int:
        """
        Calculates the sum of the n smallest k-mirror numbers.

        A k-mirror number is a positive integer that is a palindrome in both base-10 and base-k.
        """

        def is_palindrome(s: str) -> bool:
            """Checks if a string is a palindrome."""
            return s == s[::-1]

        def to_base_k(num: int, base: int) -> str:
            """Converts a decimal number to its base-k string representation."""
            if num == 0:
                return "0"
            
            res = ""
            while num > 0:
                res = str(num % base) + res
                num //= base
            return res

        k_mirror_numbers = []
        total_sum = 0
        length = 1

        while len(k_mirror_numbers) < n:
            # Generate palindromes of a certain length
            start = 10**((length - 1) // 2)
            end = 10**((length + 1) // 2)

            for i in range(start, end):
                # Construct the first half of the palindrome
                s_i = str(i)
                
                # Create the full palindrome (even length)
                # For length l, we take a number of length l/2 and append its reverse
                if length % 2 == 0:
                    palindrome_str = s_i + s_i[::-1]
                # Create the full palindrome (odd length)
                # For length l, we take a number of length (l+1)/2 and append the reverse of its prefix
                else:
                    palindrome_str = s_i + s_i[:-1][::-1]

                num = int(palindrome_str)
                base_k_str = to_base_k(num, k)

                if is_palindrome(base_k_str):
                    k_mirror_numbers.append(num)
                    total_sum += num
                    if len(k_mirror_numbers) == n:
                        return total_sum
            length += 1
            
        return total_sum