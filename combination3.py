class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = [ ]
        
        def back(path,start,k,n):
            if k == 0 and n == 0:
                res.append(path)
                
            if k == 0  or n <= 0 :
                return
            for i in range(start,10):
                back(path+[i],i+1,k-1,n-i)
                
        back([],1,k,n)
        return res
        
                
        