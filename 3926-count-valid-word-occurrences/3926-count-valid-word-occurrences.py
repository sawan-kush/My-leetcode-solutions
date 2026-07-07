from collections import Counter
from typing import List

class Solution:
    def countWordOccurrences(self, chunks: List[str], queries: List[str]) -> List[int]:

        s = "".join(chunks)
        n = len(s)

        freq = Counter()
        i = 0

        while i < n:

            if not s[i].islower():
                i += 1
                continue

            j = i

            while j < n:

                if s[j].islower():
                    j += 1

                elif (
                    s[j] == '-'
                    and j > 0
                    and j + 1 < n
                    and s[j - 1].islower()
                    and s[j + 1].islower()
                ):
                    j += 1

                else:
                    break

            freq[s[i:j]] += 1
            i = j

        return [freq[q] for q in queries]