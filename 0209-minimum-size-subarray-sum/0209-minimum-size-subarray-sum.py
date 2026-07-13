class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if target in nums:
            return 1

        window_sum = 0
        min_len = float("inf")
        l = 0
        for r in range(len(nums)):       
            window_sum += nums[r]


            while window_sum >= target:
                min_len = min(min_len,r - l + 1)
                window_sum -= nums[l]
                l += 1


        return 0 if min_len == float("inf") else min_len
                    