class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = 0
        seen = {}

        ans = 0

        seen[0] = 1

        for num in nums:
            prefix += num

            needed = prefix - k

            if needed in seen:
                ans += seen[needed]

            if prefix not in seen:
                seen[prefix] = 1
            else:
                seen[prefix] += 1

        return ans                 
        