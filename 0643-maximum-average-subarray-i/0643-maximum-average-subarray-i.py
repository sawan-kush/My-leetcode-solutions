class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        window_avg = sum(nums[:k])
        max_avg = window_avg / k

        for i in range(k, len(nums)):
            window_avg += nums[i] - nums[i-k]
            max_avg = max(window_avg / k, max_avg)
            
        return max_avg    







        






            




        