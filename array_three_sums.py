from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        sorted_list = sorted([nums[i], nums[j], nums[k]])
                        if sorted_list not in result:
                            result.append([nums[i], nums[j], nums[k]])
        return result


class BestSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result


nums = [-1,0,1,2,-1,-4]

result = Solution().threeSum(nums)
print(result)

result = BestSolution().threeSum(nums.copy())
print(result)