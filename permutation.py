class Solution:
    def __init__(self):
        self.res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums , [])
        return self.res
    
    def backtrack(self,nums , path):
        if not nums:
            self.res.append(path)
        for j in range(len(nums)):
            self.backtrack(nums[:j]+nums[j+1:],path+[nums[j]])