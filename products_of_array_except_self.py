from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        result = [1] * length

        # 1. Durchlauf von links: result[i] = Produkt aller Zahlen links von i
        left = 1
        for i in range(length):
            result[i] = left
            left *= nums[i]

        # 2. Durchlauf von rechts: mit dem Produkt aller Zahlen rechts von i multiplizieren
        right = 1
        for i in range(length - 1, -1, -1):
            result[i] *= right
            right *= nums[i]

        return result


nums = [1, 2, 4, 6]
result = Solution().productExceptSelf(nums)
print(result)
assert result == [48, 24, 12, 8]
