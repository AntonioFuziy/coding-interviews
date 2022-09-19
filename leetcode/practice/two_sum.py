from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        if i != j:
          if target == (nums[i] + nums[j]):
            return [i,j]
            
    return result