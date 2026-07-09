class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}
        for i in range(len(nums)):

            need = target - nums[i]
            if need in hash_map:
                return [i, hash_map[need]]
            hash_map[nums[i]] = i
            

