#  class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         k = len(nums)
#         j = 0
#         for i in range(k):
#             if nums[i]!=0:
#                 nums[j]=nums[i]
#                 j+=1
            
#         while(j < k):
#             nums[j]=0
#             j+=1
                                                                                 