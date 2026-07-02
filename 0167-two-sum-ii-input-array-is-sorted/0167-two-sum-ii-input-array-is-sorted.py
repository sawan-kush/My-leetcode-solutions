class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       
       seen = {}
       for first in range(len(numbers)):
           value = target - numbers[first]

           if value not in seen:
              seen[numbers[first]] = first
           else:
               return seen[value] + 1, first + 1      



        