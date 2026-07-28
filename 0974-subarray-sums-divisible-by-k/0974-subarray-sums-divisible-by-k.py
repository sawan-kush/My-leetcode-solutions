class Solution:
    from collections import defaultdict
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        prefix = 0
        ans = 0

        for num in nums:
            prefix += num

            remainder = prefix % k
            ans += count[remainder]
            count[remainder] += 1

        return ans    


        