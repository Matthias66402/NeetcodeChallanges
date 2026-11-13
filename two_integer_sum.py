from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # Zahl -> Index
        for i, num in enumerate(nums):
            partner = target - num
            if partner in seen:
                return [seen[partner], i]
            seen[num] = i
        return []



nums = [3,4,5,6]
target = 7

print(Solution().twoSum(nums, target))



# nums = [3,4,5,6], target = 7
# Output = [0,1]