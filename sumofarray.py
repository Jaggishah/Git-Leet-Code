class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum =0 
        total = [nums[0]]
        for i in range(1,len(nums)):
            for j in range(i+1):
                sum+=nums[j]
            total.append(sum)
            sum = 0
        return total
                
            