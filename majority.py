class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxi = 0
        damx = 0 
        ele = 0
        for i in nums:
            a = nums.count(i)
            maxi = max(maxi,a)
            if maxi > damx:
                damx = maxi
                ele = i
            
        return ele
            
            
        