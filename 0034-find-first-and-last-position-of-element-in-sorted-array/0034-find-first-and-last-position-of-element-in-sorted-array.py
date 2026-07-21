class Solution:
    def lowerbound(self, nums, target):
        low = 0
        high = len(nums)-1
        index = -1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                index = mid 
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index
    
    def upperbound(self, nums, target):
        low = 0
        high = len(nums)-1
        index = -1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                index = mid 
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.lowerbound(nums, target)
        if first == -1:
            return [-1,-1]

        last = self.upperbound(nums, target)


        return [first, last]















