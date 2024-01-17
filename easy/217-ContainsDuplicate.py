# 217. Contains Duplicate

# O(n log n) solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # O(n log n);
        for i in range(len(nums) - 1):
          if (nums[i] == nums[i+1]):
            return True
        return False

# O(n) solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
          if num in seen:
            return True
          seen.add(num)
        return False