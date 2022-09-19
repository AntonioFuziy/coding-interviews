class Solution:
  def trap(self, height: List[int]) -> int: 
    ans = 0
    for i in range(1, len(height)-1):
      left_max = height[i]
      for j in range(i):
        left_max = max(left_max, height[j]) 

      right_max = height[i]
      for j in range(i+1, len(height)):
        right_max = max(right_max, height[j])
      ans += min(left_max, right_max) - height[i]
    return ans