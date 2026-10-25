class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        while l < n - 1:
            r = l + 1
            while r < n:
                if nums[l] + nums[r] == target:
                    return [l, r]
                r += 1
            l += 1