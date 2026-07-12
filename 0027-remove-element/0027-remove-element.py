# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:


#         i = 0
#         if len(nums) == 1 and nums[i]==val:
#             return 0

#         j = len(nums)-1
#         while i<j:
#             if nums[i] == val :
#                 if nums[j] != val:
#                     nums[i], nums[j] = nums[j], nums[i]
#                     i+=1
#                     j-=1
#                 else:
#                     j-=1
#             else:
#                 if nums[j] == val:
#                     j-=1
#                     i+=1
#         return i
       
#             # j+=1

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # write pointer

        for j in range(len(nums)):  # read pointer
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i