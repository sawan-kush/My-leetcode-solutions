from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for ch in word:
                value = ord(ch) - ord('a')
                count[value] += 1

            groups[tuple(count)].append(word)

        return list(groups.values())    




        