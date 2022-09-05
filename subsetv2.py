class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[[]]
        for i in range(len(nums)):
            sub=[]
            for j in res:
               
                sub.append(j+[nums[i]])
                
            res.extend(sub)
      
        local=[]
        for k in res:
            if k not in local:
                local.append(k)
        return local