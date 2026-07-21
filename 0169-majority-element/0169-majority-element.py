class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        n = len(nums)
        for nm in nums:
            if freq[nm] > n/2:
                return nm
        