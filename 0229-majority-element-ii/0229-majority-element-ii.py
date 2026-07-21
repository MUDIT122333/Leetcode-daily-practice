class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        freq = {}
        n = len(nums)
        nums1 = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
            if freq[num] > n//3 and num not in nums1:
                nums1.append(num) 
        return nums1