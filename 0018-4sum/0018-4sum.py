class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        lst = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                p = j + 1
                k = len(nums) - 1

                while p < k:

                    total = nums[i] + nums[j] + nums[p] + nums[k]

                    if total == target:
                        lst.append([nums[i],nums[j],nums[p],nums[k]])

                        p += 1
                        k -= 1

                        while p < k and nums[p] == nums[p-1]:
                            p += 1

                        while k > p and nums[k] == nums[k+1]:
                            k -= 1

                    elif total > target:
                        k -= 1
                    else:
                        p += 1

        return lst                                        
                

     