class Solution:
    def generate(self, numrows: int) -> List[List[int]]:
        if numrows == 0:
            return 0
        if numrows == 1:
            return [[1]]
        
        row = [[1]]
        for i in range(1,numrows):
            ele = [1]
            if numrows>2:
                for j in range(1,i):
                    a = row[i-1][j-1]+row[i-1][j]
                    ele.append(a)
                    


            ele.append(1)
            row.append(ele)
            
        return row
            
                
            
            
            
        
        