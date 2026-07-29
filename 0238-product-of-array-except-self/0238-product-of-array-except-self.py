class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1]*n
        prefix = 1
        for i in range(n):
            if i-1 >= 0:
                prefix *= nums[i-1]
            left[i] = prefix
        
        right = [1]*n
        suffix = 1
        for i in range(n-1, -1, -1):
            if i+1<=n-1:
                suffix *= nums[i+1]
            left[i] *= suffix
        
        return left



