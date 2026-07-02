class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        for first in range(len(nums)):
            value = target - nums[first]

            if value not in seen:
                seen[nums[first]] = first

            else:
                return first,seen[value]



        
        