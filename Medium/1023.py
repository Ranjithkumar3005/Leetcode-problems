from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        dum = []

        for query in queries:
            c = 0  # Index for pattern
            match = True

            for char in query:
                # If we've matched all of pattern, remaining chars must be lowercase
                if c == len(pattern):
                    if char.isupper():
                        match = False
                        break
                # If current char doesn't match pattern[c] but is uppercase
                elif char != pattern[c] and char.isupper():
                    match = False
                    break
                # If current char matches pattern[c], move to the next pattern character
                elif char == pattern[c]:
                    c += 1

            # After loop, check if we matched entire pattern
            if match and c == len(pattern):
                dum.append(True)
            else:
                dum.append(False)

        return dum
