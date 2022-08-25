class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n =len(nums)
        from collections import Counter
        count = Counter(nums)
        for key,value in count.items():
            if value>n//2:
                return key
            
            
        