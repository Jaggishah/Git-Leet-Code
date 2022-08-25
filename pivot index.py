class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left,right = 0 , sum(nums)
        for idx,values in enumerate(nums):
            right-=values
            
            if left == right:
                return idx
            
            left+=values
            
        return -1
        
        