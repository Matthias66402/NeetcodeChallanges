class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


nums = [1, 2, 3, 4]
answer = Solution().hasDuplicate(nums)
print(f"answer: {answer}")