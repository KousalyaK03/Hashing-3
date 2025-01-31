class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Approach:
        # - Use a sliding window to extract all 10-letter substrings.
        # - Store seen sequences in a HashSet.
        # - If a sequence is encountered again, store it in a result set.
        # - Convert the result set to a list and return.

        # Edge case: If the string length is less than 10, no repeated sequences can exist.
        if len(s) < 10:
            return []

        seen = set()  # Set to store seen sequences
        repeated = set()  # Set to store repeated sequences

        # Iterate through the string and extract all 10-character substrings
        for i in range(len(s) - 9):  # Stop at len(s) - 9 to get a full 10-letter substring
            sequence = s[i:i + 10]  # Extract 10-letter substring

            # If the sequence is already seen, add it to repeated set
            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)  # Otherwise, add it to seen set

        return list(repeated)  # Convert the set to a list before returning

# Time Complexity: O(N), where N is the length of s. We traverse the string once.
# Space Complexity: O(N), in the worst case, storing all substrings in the set.