from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left + 1, right + 1]  # 1-indexed
            if current < target:
                left += 1   # Summe zu klein -> größere Zahl links nehmen
            else:
                right -= 1  # Summe zu groß -> kleinere Zahl rechts nehmen
        return []


numbers = [1, 2, 3, 4]
target = 3

solution = Solution().twoSum(numbers, target)
print(solution)  # [1, 2]
