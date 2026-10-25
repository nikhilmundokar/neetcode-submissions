class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        i = 0
        prod = 1
        while i < n:
            prod *= nums[i]
            pref[i] = prod
            i += 1

        post = [1] * n
        j = n - 1
        prod = 1
        while j >= 0:
            prod *= nums[j]
            post[j] = prod
            j -= 1

        res = []
        i = 0
        while i < n:
            temp = 1
            if i != 0:
                temp *= pref[i - 1]
            if i != n - 1:
                temp *= post[i + 1]
            res.append(temp)
            i += 1
        return res