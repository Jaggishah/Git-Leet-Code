class Solution:
    def myPow(self, x: float, n: int) -> float:
        def jaggi(base = x,expo = abs(n)):
            if expo == 0:
                return 1
            
            elif expo%2==0:
                return jaggi(base * base , expo//2)
            
            else:
                return base * jaggi(base * base , (expo -1)//2)
            
        f = jaggi()
        
        return float(f) if n >0 else 1/f
            
            
        
        
     
                
            
            
        