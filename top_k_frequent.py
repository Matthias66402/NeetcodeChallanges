from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp_dict = {}
        for elem in nums:
            if elem not in temp_dict:
                temp_dict[elem] = 1
            else:
                temp_dict[elem] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in temp_dict.items():
            buckets[count].append(num)

        result = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
