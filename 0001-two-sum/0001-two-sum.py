class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        freq_map = {}
        for i in range(len(nums)):
            need = target - nums[i]

            if need in freq_map:
                return [i, freq_map[need]]
            freq_map[nums[i]] = i
            


            