# res=[[1],[2]]
# sub = []
# sub.append(res[0]+[4])
# res = sub
# print(sub,res)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[ [] ] 
        for i in nums:
            sub = [ ]
            for j in res:
                sub.append(j)
                sub.append(j+[i])
                
            res = sub
            
        return res
                    
                
                        
                         
                   
                    
                    
                    
                    
                    
    
                
        