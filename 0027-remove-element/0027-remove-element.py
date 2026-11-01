class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # write pointer

        for j in range(len(nums)):  # read pointer
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i